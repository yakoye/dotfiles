# MinerU 双层可搜索 PDF 构建工具

#  (MinerU PDF Layers Builder)

这是一个专为 **MinerU (Magic-PDF)** 设计的后处理工具。它可以将 MinerU 输出的 `middle.json` 文本信息精准地回填至原始扫描版 PDF 中，生成一个**保持原貌、可检索、可选中复制**的双层 PDF 文件。



## ✨ 技术亮点

- **全内容捕获**：除了正文，还能自动识别并处理 `discarded_blocks` 中的页眉、页脚、页码和脚注。
- **智能跨页路由**：自动纠正 MinerU 偶尔出现的跨页块识别错误，确保文字在物理坐标正确的一页渲染。
- **工业级排版对齐**：
    - 自动计算字符间距（CharSpace），实现文字两端对齐。
    - 自动适配页面缩放比例（Scale X/Y），兼容不同分辨率的扫描件。
    - 纵向基线补偿，确保透明文本层与底层图像完美重叠。
- **深度递归提取**：支持复杂嵌套结构（如表格、多栏布局）的文字提取。
- **健壮性优化**：内置去重逻辑，防止因 JSON 脏数据导致的文字重叠。

## 🚀 快速开始

### 1. 环境准备

在windows上使用。

确保你的 Python 环境中已安装以下依赖：

```bash
pip install pypdf reportlab
```

同时，为了支持中文字体，请在脚本同级目录下放置 `SimHei.ttf`（黑体）文件。

### 2. 使用方法

本工具已封装为命令行模式，无需修改代码即可处理不同文件。

需要用到MinerU识别pdf后，生成的output文件夹，其中有**xxx_middle.json**、**xxx_origin.pdf**文件。

#### 基础用法：

```
python build_text_layer_to_pdf.py -p "原始文件.pdf" -j "MinerU输出_middle.json"
```

执行后会默认生成 `原始文件_ocr.pdf`。

#### 自定义输出路径：

```
python build_text_layer_to_pdf.py -p xxx_origin.pdf -j xxx_middle.json -o xxx_ocr.pdf
```

例子：

```
python build_text_layer_to_pdf.py -p "HassabisAI_6394_origin.pdf" -j "HassabisAI_6394_middle.json" -o "HassabisAI_6394_ocr.pdf"
```



## 🛠️ 参数说明

| **参数**   | **缩写** | **强制** | **说明**                                     |
| ---------- | -------- | -------- | -------------------------------------------- |
| `--pdf`    | `-p`     | 是       | 输入的原始扫描版 PDF 路径                    |
| `--json`   | `-j`     | 是       | MinerU 生成的 `middle.json` 路径             |
| `--output` | `-o`     | 否       | 输出 PDF 的路径（默认为原名 + `_ocr_final`） |

## 📂 项目结构

- `build_text_layer_to_pdf.py`: 主核心逻辑脚本。
- `SimHei.ttf`: (需自行放入) 渲染透明层所需的中文字体。

```
./
├── .gitignore              (建议忽略 .pdf 和 .json 原始文件)
├── README.md               (上面的文件)
├── build_text_layer_to_pdf.py     (我们写的核心代码)
└── requirements.txt        (包含 pypdf 和 reportlab)
```

