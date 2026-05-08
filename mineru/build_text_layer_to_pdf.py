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

# ================= 2. 深度提取文本逻辑 (升级版：支持无限递归嵌套) =================
def extract_texts_from_block(block):
    """递归深入 MinerU 的 json，提取真正的文字和对应的坐标，完美支持表格和复杂嵌套"""
    extracted = []
    
    # 1. 如果存在子 blocks（如表格、多列排版），先递归深入
    if "blocks" in block and isinstance(block["blocks"], list):
        for sub_block in block["blocks"]:
            extracted.extend(extract_texts_from_block(sub_block))
            
    # 2. 提取当前层级的 lines -> spans
    lines = block.get("lines", [])
    if lines:
        for line in lines:
            spans = line.get("spans", [])
            if spans:
                for span in spans:
                    text = span.get("content", span.get("text", "")).strip()
                    bbox = span.get("bbox", [])
                    if text and len(bbox) == 4:
                        extracted.append((text, bbox))
            else:
                text = line.get("content", line.get("text", "")).strip()
                bbox = line.get("bbox", [])
                if text and len(bbox) == 4:
                    extracted.append((text, bbox))
                    
    # 3. 如果当前 block 既没有嵌套的 blocks，也没有 lines，尝试直接抓取外层
    elif not block.get("blocks"):
        text = block.get("content", block.get("text", "")).strip()
        bbox = block.get("bbox", [])
        if text and len(bbox) == 4:
            extracted.append((text, bbox))
            
    return extracted

# ================= 3. 主程序（全量处理版） =================
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

    # ================= 核心修复 1：构建精准的页码映射字典 =================
    # 防止因 MinerU 跳过空白页导致前后页码错位
    page_data_map = {}
    for idx, p_data in enumerate(pages_data):
        # 尝试获取 MinerU 记录的真实页码 (page_idx通常为0起跳，page_no通常为1起跳)
        p_idx = p_data.get("page_idx", p_data.get("page_no"))
        if p_idx is not None:
            page_data_map[int(p_idx)] = p_data
        else:
            page_data_map[idx] = p_data  # 降级处理

    # 自动识别 JSON 的页码是 0 还是 1 开始。如果是 1 开始，整体减 1 对齐 PDF 数组
    if page_data_map and min(page_data_map.keys()) == 1:
        page_data_map = {k - 1: v for k, v in page_data_map.items()}
    # ======================================================================

    for i in range(total_pdf_pages):
        original_page = reader.pages[i]
        page_data = page_data_map.get(i)

        # 如果这一页在 MinerU 中根本没有数据（比如纯空白页），直接合并原页并跳过
        if not page_data:
            writer.add_page(original_page)
            print(f"👉 第 {i + 1}/{total_pdf_pages} 页：安全跳过（JSON 中无此页数据）。")
            continue

        # 获取当前页的物理尺寸
        pdf_w = float(original_page.mediabox.width)
        pdf_h = float(original_page.mediabox.height)

        # 获取 MinerU 记录的尺寸以计算缩放比
        page_size_data = page_data.get("page_size", [pdf_w, pdf_h])
        layout_w = page_size_data[0] if page_size_data[0] else pdf_w
        layout_h = page_size_data[1] if page_size_data[1] else pdf_h
        
        scale_x = pdf_w / layout_w
        scale_y = pdf_h / layout_h

        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=(pdf_w, pdf_h))

        # ================= 核心修复 2：更健壮的块选择 =================
        blocks = page_data.get("para_blocks", [])
        if not blocks: # 如果没有排版块，降级使用原始块
            blocks = page_data.get("preproc_blocks", [])
            
        count = 0
        for block in blocks:
            text_items = extract_texts_from_block(block)
            for text, bbox in text_items:
                # 缩放坐标：增加提取 x1 用于计算宽度
                x0 = bbox[0] * scale_x
                y0 = bbox[1] * scale_y
                x1 = bbox[2] * scale_x
                y1 = bbox[3] * scale_y
				
                # 文本块实际宽度和高度
                w = x1 - x0
                h = y1 - y0 
				
                # ReportLab 是左下角原点，MinerU 是左上角原点
                rx = x0
				# 【纵向对齐】：基线补偿
                # 加上 h * 0.15 作为向上偏移补偿，把基线稍微抬高。
                # 0.15 是经验值，适用于大多数字体和字号，既能避免文字被切掉，又能保持在框内。
                # 这个可以根据实际情况微调，如果发现某些字体或字号有轻微偏差，可以适当增加或减少这个值。
                ry = pdf_h - y1 + h * 0.15
                font_size = max(4, h * 0.8)

                textob = c.beginText()               
                textob.setTextOrigin(rx, ry)         
                textob.setFont(CHINESE_FONT, font_size) 
                
                # ================= 【横向对齐】：两端对齐 =================
				# 测量这段文字在当前字号下的“自然物理宽度”
                text_natural_width = stringWidth(text, CHINESE_FONT, font_size)
				# 计算两端对齐间距，需要拉伸或压缩的平均字符间距
                if len(text) > 1:
                    char_space = (w - text_natural_width) / (len(text) - 1)
                    # 保护机制：防止极端的 OCR 框导致文字无限拉长或挤成一团黑
                    char_space = max(-font_size * 0.3, min(char_space, font_size * 2))
                else:
                    char_space = 0
                    
                # 设置字符间距（正数拉伸，负数压缩，文字内容本身不受影响）
                textob.setCharSpace(char_space)

                # 双重隐形策略：完全透明 + PDF 隐身渲染模式
                c.setFillColor(Color(0, 0, 0, alpha=0)) 
                textob.setTextRenderMode(3)             
                
                # 写入画布
                textob.textOut(text)                 
                c.drawText(textob)                   
                count += 1

        # 强制生成该页面（防止遇上无文字的图片页、空白页报错）
        c.showPage() 
        c.save()
        packet.seek(0)
        
        # 将刚才画好的这1页透明图层合并到原 PDF 的当前页上
        text_layer_pdf = PdfReader(packet)
        if len(text_layer_pdf.pages) > 0:
            text_page = text_layer_pdf.pages[0]
            original_page.merge_page(text_page)
        
        # 将合并好的页面放入写入器
        writer.add_page(original_page)
        print(f"👉 第 {i + 1}/{total_pdf_pages} 页：成功写入 {count} 段隐形文字。")

    # 循环结束后，一次性写入磁盘
    print("⏳ 正在保存最终的 PDF 文件，请稍候...")
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✅ 全量处理完成！完美的双层可搜索 PDF 已生成：{output_path}")

if __name__ == "__main__":
    build_searchable_pdf()