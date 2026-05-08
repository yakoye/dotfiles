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
    增加 current_page 参数，实现跨页文本的精准路由分发。
    """
    extracted = []
    
    # 记录最外层父块的边界（用于坐标回跃检测）
    if root_bbox is None:
        root_bbox = block.get("bbox", block.get("bbox_fs", []))

    def get_target_page(item_data, item_bbox):
        """路由裁判：决定这段文字该画在哪一页"""
        # 1. 如果带有 cross_page 标签，直接发配到下一页
        if item_data.get("cross_page") is True:
            return current_page + 1
            
        # 2. 物理坐标回跃检测：
        # 如果子句子的 Y0 坐标比父段落的顶部 Y0 还要高出 150 像素以上，
        # 说明这行字其实已经翻页到了下一页的顶部。
        if item_bbox and len(item_bbox) == 4 and root_bbox and len(root_bbox) == 4:
            if item_bbox[1] < root_bbox[1] - 150:
                return current_page + 1
                
        # 默认留在当前页
        return current_page

    # 1. 递归深入子 blocks
    if "blocks" in block and isinstance(block["blocks"], list):
        for sub_block in block["blocks"]:
            extracted.extend(extract_texts_from_block(sub_block, root_bbox, current_page))
            
    # 2. 递归处理 lines 层级
    lines = block.get("lines", [])
    if lines:
        for line in lines:
            extracted.extend(extract_texts_from_block(line, root_bbox, current_page))
            
    # 3. 处理 spans 层级
    spans = block.get("spans", [])
    if spans:
        for span in spans:
            text = span.get("content", span.get("text", "")).strip()
            bbox = span.get("bbox", [])
            if text and len(bbox) == 4:
                target_page = get_target_page(span, bbox)
                extracted.append((text, bbox, target_page))
                
    # 4. 兜底抓取
    if not block.get("blocks") and not block.get("lines") and not block.get("spans"):
        text = block.get("content", block.get("text", "")).strip()
        bbox = block.get("bbox", [])
        if text and len(bbox) == 4:
            target_page = get_target_page(block, bbox)
            extracted.append((text, bbox, target_page))
            
    return extracted

# ================= 3. 主程序（全量合并版） =================
def build_searchable_pdf():
    # ========== 请根据实际情况修改路径 ==========
    pdf_path = "哈萨比斯谷歌AI之脑_6394_origin.pdf"
    json_path = "哈萨比斯谷歌AI之脑_6394_middle.json"
    output_path = "哈萨比斯谷歌AI之脑_6394_ocr_final.pdf" 
    # ==========================================

    if not os.path.exists(pdf_path) or not os.path.exists(json_path):
        print("❌ 找不到原始 PDF 或 JSON 文件！请检查路径。")
        return

    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    pages_info = data.get("pdf_info", [])
    total_pdf_pages = len(reader.pages)
    print(f"⏳ 开始处理，PDF共 {total_pdf_pages} 页...")

    # --- 阶段 1：页码映射对齐 ---
    page_data_map = {}
    for idx, p_data in enumerate(pages_info):
        p_idx = p_data.get("page_idx", p_data.get("page_no"))
        if p_idx is not None:
            page_data_map[int(p_idx)] = p_data
        else:
            page_data_map[idx] = p_data 

    # 对齐 0-based 索引
    if page_data_map and min(page_data_map.keys()) == 1:
        page_data_map = {k - 1: v for k, v in page_data_map.items()}

    # --- 阶段 2：预读全局池 (加入 discarded_blocks) ---
    print("⏳ 正在扫描全文（含正文、页眉、页脚、跨页分拣）...")
    global_spans = {}  # {页码: [(text, bbox), ...]}
    
    for p_idx, page_data in page_data_map.items():
        # 【核心改进】：合并正文块与舍弃块（页眉页脚在此处）
        blocks = page_data.get("para_blocks", [])
        if not blocks: 
            blocks = page_data.get("preproc_blocks", [])
        
        # 加上页眉、页脚、脚注所在的 discarded_blocks
        all_sources = blocks + page_data.get("discarded_blocks", [])
            
        for block in all_sources:
            items = extract_texts_from_block(block, current_page=p_idx)
            for text, bbox, target_page in items:
                if target_page not in global_spans:
                    global_spans[target_page] = []
                global_spans[target_page].append((text, bbox))

    # --- 阶段 3：图层绘制与合并 ---
    print("⏳ 正在渲染并合并图层...")
    for i in range(total_pdf_pages):
        original_page = reader.pages[i]
        text_items = global_spans.get(i, [])

        if not text_items:
            writer.add_page(original_page)
            print(f"👉 第 {i + 1}/{total_pdf_pages} 页：无内容，直接合并。")
            continue

        pdf_w = float(original_page.mediabox.width)
        pdf_h = float(original_page.mediabox.height)

        # 比例适配
        page_data = page_data_map.get(i, {})
        page_size_data = page_data.get("page_size", [pdf_w, pdf_h])
        layout_w = page_size_data[0] if page_size_data[0] else pdf_w
        layout_h = page_size_data[1] if page_size_data[1] else pdf_h
        scale_x = pdf_w / layout_w
        scale_y = pdf_h / layout_h

        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=(pdf_w, pdf_h))

        count = 0
        seen_items = set() 
        
        for text, bbox in text_items:
            item_key = (text, tuple(bbox))
            if item_key in seen_items:
                continue
            seen_items.add(item_key)

            x0, y0, x1, y1 = [b * scale_x if j%2==0 else b * scale_y for j, b in enumerate(bbox)]
            w, h = x1 - x0, y1 - y0 
            
            if w <= 0.1 or h <= 0.1: continue
            
            rx = x0
            ry = pdf_h - y1 + h * 0.15 # 纵向对齐补偿
            font_size = max(4, h * 0.8)

            textob = c.beginText()               
            textob.setTextOrigin(rx, ry)         
            textob.setFont(CHINESE_FONT, font_size) 
            
            # 两端对齐计算
            text_natural_width = stringWidth(text, CHINESE_FONT, font_size)
            if len(text) > 1:
                char_space = (w - text_natural_width) / (len(text) - 1)
                char_space = max(-font_size * 0.3, min(char_space, font_size * 2))
            else:
                char_space = 0
            textob.setCharSpace(char_space)

            # 透明渲染
            c.setFillColor(Color(0, 0, 0, alpha=0)) 
            textob.setTextRenderMode(3)             
            textob.textOut(text)                 
            c.drawText(textob)                   
            count += 1

        c.showPage() 
        c.save()
        packet.seek(0)
        
        text_layer_pdf = PdfReader(packet)
        if len(text_layer_pdf.pages) > 0:
            original_page.merge_page(text_layer_pdf.pages[0])
        
        writer.add_page(original_page)
        print(f"👉 第 {i + 1}/{total_pdf_pages} 页：成功写入 {count} 段文字（含页眉页脚）。")

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✅ 处理完成！全内容可搜索PDF已生成：{output_path}")

if __name__ == "__main__":
    build_searchable_pdf()