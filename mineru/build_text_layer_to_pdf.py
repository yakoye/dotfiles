import json
import io
import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
# 引入字符串宽度测量工具
from reportlab.pdfbase.pdfmetrics import stringWidth

# --- 准备工作：---
# 安装依赖：
# pip install pypdf reportlab
#
# 注册中文字体 
# 请确保路径下有这个字体文件，或者指向系统中文字体路径
# 例如 Windows: "C:/Windows/Fonts/simhei.ttf"

# ================= 1. 注册中文字体 =================
font_path = "SimHei.ttf"
try:
    pdfmetrics.registerFont(TTFont('SimHei', font_path))
    CHINESE_FONT = "SimHei"
except Exception as e:
    print(f"⚠️ 警告：未找到中文字体 {font_path}，将使用默认英文字体！中文可能会乱码。")
    CHINESE_FONT = "Helvetica"

# ================= 2. 深度提取文本逻辑 (跨页路由分发版) =================
def extract_texts_from_block(block, root_bbox=None, current_page=0):
    """
    递归深入 MinerU 的 json 提取真正的文字。
    【核心升级】：增加 current_page 参数，不再删除越界文本，而是给它们重新分配正确的目标页码。
    """
    extracted = []
    
    # 记录最外层父块的边界（用于坐标回跃检测）
    if root_bbox is None:
        root_bbox = block.get("bbox", block.get("bbox_fs", []))

    def get_target_page(item_data, item_bbox):
        """路由裁判：决定这段文字该画在哪一页"""
        # 1. 官方明示：如果 JSON 带有 cross_page 标签，直接发配到下一页
        if item_data.get("cross_page") is True:
            return current_page + 1
            
        # 2. 物理坐标回跃检测：MinerU 的 Y 坐标是往下递增的。
        # 如果一个子句子的 Y 坐标突然比父段落的顶部还要高出很多（< root_bbox[1] - 150），
        # 绝对说明它折行翻页到了下一页的顶部。
        if item_bbox and len(item_bbox) == 4 and root_bbox and len(root_bbox) == 4:
            if item_bbox[1] < root_bbox[1] - 150:
                return current_page + 1
                
        # 默认留在当前页
        return current_page

    # 1. 如果存在子 blocks（如表格、多列排版），递归深入
    if "blocks" in block and isinstance(block["blocks"], list):
        for sub_block in block["blocks"]:
            extracted.extend(extract_texts_from_block(sub_block, root_bbox, current_page))
            
    # 2. 如果存在 lines 层级，递归处理
    lines = block.get("lines", [])
    if lines:
        for line in lines:
            extracted.extend(extract_texts_from_block(line, root_bbox, current_page))
            
    # 3. 如果存在 spans 层级，执行页码判定后抓取
    spans = block.get("spans", [])
    if spans:
        for span in spans:
            text = span.get("content", span.get("text", "")).strip()
            bbox = span.get("bbox", [])
            if text and len(bbox) == 4:
                # ★ 核心改动：获取目标页码并一并返回
                target_page = get_target_page(span, bbox)
                extracted.append((text, bbox, target_page))
                
    # 4. 如果当前节点既没有 blocks、没有 lines、也没有 spans，尝试直接抓取（兜底）
    if not block.get("blocks") and not block.get("lines") and not block.get("spans"):
        text = block.get("content", block.get("text", "")).strip()
        bbox = block.get("bbox", [])
        if text and len(bbox) == 4:
            target_page = get_target_page(block, bbox)
            extracted.append((text, bbox, target_page))
            
    return extracted

# ================= 3. 主程序（全局文本池版） =================
def build_searchable_pdf():
    # ========== 请修改为你的文件路径 ==========
    pdf_path = "哈萨比斯谷歌AI之脑_1_origin.pdf"
    json_path = "哈萨比斯谷歌AI之脑_1_middle.json"
    output_path = "哈萨比斯谷歌AI之脑_1_ocr_final.pdf" 
    # ==========================================

    if not os.path.exists(pdf_path) or not os.path.exists(json_path):
        print("❌ 找不到原始 PDF 或 JSON 文件！请检查路径。")
        return

    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    pages_data = data.get("pdf_info", [])
    total_pdf_pages = len(reader.pages)
    
    print(f"⏳ 开始全量处理，原 PDF 共 {total_pdf_pages} 页...")

    # ================= 阶段 1：构建精准的页码映射字典 =================
    page_data_map = {}
    for idx, p_data in enumerate(pages_data):
        p_idx = p_data.get("page_idx", p_data.get("page_no"))
        if p_idx is not None:
            page_data_map[int(p_idx)] = p_data
        else:
            page_data_map[idx] = p_data 

    if page_data_map and min(page_data_map.keys()) == 1:
        page_data_map = {k - 1: v for k, v in page_data_map.items()}

    # ================= 阶段 2：预读并构建全局文本池 =================
    print("⏳ 正在预读并分发跨页文本...")
    global_spans = {}  # 数据结构: {页码: [(text, bbox), ...]}
    
    for p_idx, page_data in page_data_map.items():
        blocks = page_data.get("para_blocks", [])
        if not blocks: 
            blocks = page_data.get("preproc_blocks", [])
            
        for block in blocks:
            # 提取文本，并且拿到它们真正属于的页码 (target_page)
            items = extract_texts_from_block(block, current_page=p_idx)
            for text, bbox, target_page in items:
                if target_page not in global_spans:
                    global_spans[target_page] = []
                # 将文本丢入对应页码的池子里（跨页文本此时被成功转移给下一页）
                global_spans[target_page].append((text, bbox))

    # ================= 阶段 3：正式渲染图层 =================
    print("⏳ 正在生成透明图层并合并...")
    for i in range(total_pdf_pages):
        original_page = reader.pages[i]
        
        # ★ 从全局池中捞出属于这一页的所有文字（包含了上一页送过来的折行文本）
        text_items = global_spans.get(i, [])

        # 如果这一页真的连一个字都没有，直接合并原页并跳过
        if not text_items:
            writer.add_page(original_page)
            print(f"👉 第 {i + 1}/{total_pdf_pages} 页：无文本内容，安全跳过。")
            continue

        page_data = page_data_map.get(i, {})
        pdf_w = float(original_page.mediabox.width)
        pdf_h = float(original_page.mediabox.height)

        # 获取缩放基准，如果当前页 JSON 丢失，找其他页的尺寸借用以保证缩放比例不崩
        page_size_data = page_data.get("page_size")
        if not page_size_data:
            for pd in page_data_map.values():
                if "page_size" in pd:
                    page_size_data = pd["page_size"]
                    break
            if not page_size_data:
                page_size_data = [pdf_w, pdf_h]

        layout_w = page_size_data[0] if page_size_data[0] else pdf_w
        layout_h = page_size_data[1] if page_size_data[1] else pdf_h
        
        scale_x = pdf_w / layout_w
        scale_y = pdf_h / layout_h

        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=(pdf_w, pdf_h))

        count = 0
        seen_items = set() 
        
        for text, bbox in text_items:
            # 过滤重合度高的重复元素（防御 MinerU 输出脏数据）
            item_key = (text, tuple(bbox))
            if item_key in seen_items:
                continue
            seen_items.add(item_key)

            x0 = bbox[0] * scale_x
            y0 = bbox[1] * scale_y
            x1 = bbox[2] * scale_x
            y1 = bbox[3] * scale_y
            
            w = x1 - x0
            h = y1 - y0 
            
            # 防崩溃保护：如果异常框导致宽或高为 0，引发后续计算崩溃
            if w <= 0.1 or h <= 0.1:
                continue
            
            rx = x0
            # 【纵向对齐】：基线补偿 (0.15 经验值抬高)
            ry = pdf_h - y1 + h * 0.15
            font_size = max(4, h * 0.8)

            textob = c.beginText()               
            textob.setTextOrigin(rx, ry)         
            textob.setFont(CHINESE_FONT, font_size) 
            
            # 【横向对齐】：两端对齐计算
            text_natural_width = stringWidth(text, CHINESE_FONT, font_size)
            if len(text) > 1:
                char_space = (w - text_natural_width) / (len(text) - 1)
                # 保护机制：防止极端的 OCR 框导致文字无限拉长或挤成一团黑
                char_space = max(-font_size * 0.3, min(char_space, font_size * 2))
            else:
                char_space = 0
                
            textob.setCharSpace(char_space)

            # 双重隐形策略：完全透明 + PDF 隐身渲染模式 3
            c.setFillColor(Color(0, 0, 0, alpha=0)) 
            textob.setTextRenderMode(3)             
            
            # 写入画布
            textob.textOut(text)                 
            c.drawText(textob)                   
            count += 1

        c.showPage() 
        c.save()
        packet.seek(0)
        
        text_layer_pdf = PdfReader(packet)
        if len(text_layer_pdf.pages) > 0:
            text_page = text_layer_pdf.pages[0]
            original_page.merge_page(text_page)
        
        writer.add_page(original_page)
        print(f"👉 第 {i + 1}/{total_pdf_pages} 页：成功写入 {count} 段隐形文字。")

    print("⏳ 正在保存最终的 PDF 文件，请稍候...")
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✅ 全量处理完成！完美的双层可搜索 PDF 已生成：{output_path}")

if __name__ == "__main__":
    build_searchable_pdf()