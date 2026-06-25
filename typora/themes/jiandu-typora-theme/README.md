# Jiandu Typora Theme

> A reading-first Typora theme pack with an A4-oriented print / PDF engine.  
> 一套以阅读体验为先、并重点面向 A4 打印 / 导出 PDF 的 Typora 主题包。

**Version / 版本：** `0.1.13`  
**Default screen theme / 默认屏幕主题：** `Jiandu Natural Paper`

---

## Highlights / 核心特点

- Seven screen themes: Natural Paper, Bright White, Warm Beige, Mist Blue, Night Green, Deep Navy, and Print Preview.  
  七套屏幕主题：自然纸张、明亮白、暖米色、雾蓝、夜间绿、深墨蓝、印刷预览。
- Every theme automatically switches to one stable **A4 white-paper layout** when printing or exporting PDF.  
  任意主题在打印或导出 PDF 时，都会自动切换为统一、稳定的 **A4 白纸排版**。
- Images are centered, constrained to the printable width, and protected against horizontal clipping.  
  图片自动居中、限制在可打印宽度内，并优先避免横向裁切。
- PCIe-oriented table and code-block rules: long identifiers wrap instead of overflowing.  
  针对 PCIe 技术资料优化表格和代码块：长字段优先换行，而不是撑破页面。
- Tables use a stable fixed layout. For six-column PCIe tables, the register column is intentionally limited so behavior and firmware-note columns retain reading space.  
  表格采用稳定的固定列宽布局。六列 PCIe 表格会刻意限制寄存器名列，给行为说明和固件备注保留阅读空间。
- Task lists use the real GitHub-style native checkbox in normal inline flow. A small `vertical-align` correction lowers the native square slightly so it visually aligns with Song-serif text; no replacement icon is drawn.  
  任务列表采用 GitHub 风格的真实原生复选框并保留正常行内布局。仅通过很小的 `vertical-align` 将原生方框下调，使其视觉上与宋体正文对齐；不绘制替代图标。
- Formal book / thesis / newspaper typography is the default; screen font remains a one-line setting and print fonts stay independent and stable.  
  默认采用正式书籍 / 论文 / 报刊式字体；屏幕字体仍只需改一行，打印字体独立固定，保证分页和技术排版稳定。

---

## Default Typography / 默认排版方向

**Screen default / 屏幕默认：** `Noto Sans Simplified Chinese / NotoSansSC` (via `--jiandu-font-noto-sans-sc`). It is selected for its clear desktop rendering, particularly for technical documents and mixed Chinese-English reading.  
**屏幕默认：** `Noto Sans Simplified Chinese / NotoSansSC`（通过 `--jiandu-font-noto-sans-sc`）。它优先服务于电脑屏幕上的清晰显示，尤其适合技术资料与中英文混排。

**Print/PDF default / 打印与 PDF 默认：** `Source Han Serif / 思源宋体` publishing stack. It remains separate from the screen font to keep A4 layout, line wrapping, and PCIe tables stable.  
**打印与 PDF 默认：** `Source Han Serif / 思源宋体` 出版字体链。它与屏幕字体分开，以保持 A4 分页、换行和 PCIe 表格稳定。

`Maple Mono NL NF CN` is now the default code-stack preference, followed by Iosevka, JetBrains Mono, Cascadia Code, and other monospace fallbacks.  
`Maple Mono NL NF CN` 现为默认代码字体优先项，后续依次回退到 Iosevka、JetBrains Mono、Cascadia Code 等等宽字体。

Open `font-preview.md` after installation to compare title, body, table, and code combinations.  
安装后可打开 `font-preview.md`，对比标题、正文、表格与代码的组合效果。

## Theme Names / 主题名称

| CSS file | Typora menu name | Description / 说明 |
|---|---|---|
| `jiandu-natural-paper.css` | Jiandu Natural Paper | Default. Gentle off-white paper and muted green accents. / 默认，柔和纸白与低饱和绿色。 |
| `jiandu-bright-white.css` | Jiandu Bright White | Clean high-clarity writing and office documents. / 清晰明亮，适合办公与技术编辑。 |
| `jiandu-warm-beige.css` | Jiandu Warm Beige | Warm book-page feeling for journals and prose. / 温暖书页感，适合日记与文章。 |
| `jiandu-mist-blue.css` | Jiandu Mist Blue | Calm, cool technical reading. / 安静冷色，适合技术资料阅读。 |
| `jiandu-night-green.css` | Jiandu Night Green | Low-brightness night reading. / 夜间低亮度阅读。 |
| `jiandu-deep-navy.css` | Jiandu Deep Navy | Focused dark theme for code and engineering material. / 深色专业风格，适合代码与工程资料。 |
| `jiandu-print-preview.css` | Jiandu Print Preview | A screen preview close to the A4 export appearance. / 接近 A4 导出效果的屏幕预览。 |

---

## Install / 安装

1. In Typora, open **File → Preferences → Appearance → Open Theme Folder**.  
   在 Typora 中打开：**文件 → 偏好设置 → 外观 → 打开主题文件夹**。
2. Copy the seven top-level `jiandu-*.css` files and the complete `jiandu` folder into that theme folder.  
   将根目录下的七个 `jiandu-*.css` 文件，以及完整的 `jiandu` 文件夹，一起复制到主题文件夹中。
3. Keep the structure unchanged.  
   请保持目录结构不变：

```text
Typora themes/
├─ jiandu-natural-paper.css
├─ jiandu-bright-white.css
├─ jiandu-warm-beige.css
├─ jiandu-mist-blue.css
├─ jiandu-night-green.css
├─ jiandu-deep-navy.css
├─ jiandu-print-preview.css
└─ jiandu/
   ├─ base.css
   ├─ fonts.css
   ├─ user-fonts.css
   ├─ core.css
   ├─ code.css
   ├─ mermaid.css
   ├─ ui.css
   └─ print.css
```

4. Restart Typora, or switch to another theme and switch back.  
   重启 Typora，或者先切换到其他主题再切回来。
5. Select a theme from **Themes / 主题** in Typora's menu.  
   在 Typora 菜单的 **主题** 中选择相应主题。

> `assets/`, `print-test.md`, and `font-preview.md` are optional test files. They do not need to be copied into the Typora theme folder.  
> `assets/`、`print-test.md` 与 `font-preview.md` 是可选测试文件，不需要复制到 Typora 主题文件夹。

---

## Typography Settings / 字体设置

Open `jiandu/user-fonts.css`. The first `:root` block contains the editable font slots for **body**, **headings**, **tables**, **code**, **UI**, and **print/PDF**.  
打开 `jiandu/user-fonts.css`。第一个 `:root` 块提供 **正文**、**标题**、**表格**、**代码**、**界面** 与 **打印 / PDF** 的可编辑字体槽位。

Default screen combination / 默认屏幕组合：

```css
--jiandu-reading-font: var(--jiandu-font-noto-sans-sc);
--jiandu-heading-font: var(--jiandu-font-noto-sans-sc);
--jiandu-table-font: var(--jiandu-reading-font);
--jiandu-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
--jiandu-ui-font: var(--jiandu-font-noto-sans-sc);
```

Default print combination / 默认打印组合：

```css
--jiandu-print-body-font: var(--jiandu-font-publishing);
--jiandu-print-heading-font: var(--jiandu-font-publishing);
--jiandu-print-table-font: var(--jiandu-print-body-font);
--jiandu-print-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
```

### Available local presets / 可用本机字体预设

| Variable / 变量 | Typical role / 典型用途 |
| --- | --- |
| `--jiandu-font-noto-sans-sc` | Noto Sans Simplified Chinese / NotoSansSC; clear desktop body, table, and UI text / 清晰的电脑正文、表格、界面文字 |
| `--jiandu-font-maple-mono-nl-nf-cn` | Maple Mono NL NF CN; code, registers, terminal commands / 代码、寄存器、终端命令 |
| `--jiandu-font-publishing` | Source Han Serif / 思源宋体; formal books, papers, and PDF output / 正式书刊、论文与 PDF |
| `--jiandu-font-fz-shusong-gbk` | 方正书宋_GBK; formal book body / 正式书籍正文 |
| `--jiandu-font-fz-boyasong` | 方正博雅宋; refined essay/book body / 雅致文章、书籍正文 |
| `--jiandu-font-fz-qingkeben-yuesong` | 方正清刻本悦宋; classic literary reading / 古典感阅读正文 |
| `--jiandu-font-fz-baosong` | 方正报宋; newspaper-like body or heading / 报刊式正文或标题 |
| `--jiandu-font-fz-youhei` | 方正悠黑; calm technical headings / 沉静技术标题 |
| `--jiandu-font-hy-qihei` | 汉仪旗黑; modern clean headings / 清爽现代标题 |
| `--jiandu-font-fz-cuhe` | 方正粗黑; strong display headings / 强强调展示标题 |
| `--jiandu-font-hy-cuhe` | 汉仪粗黑; strong display headings / 强强调展示标题 |
| `--jiandu-font-heavy-black` | Generic strong-heading fallback / 通用强强调标题回退 |
| `--jiandu-font-wenkai` | 霞鹜文楷; optional personal screen reading / 可选个人屏幕阅读 |
| `--jiandu-font-kinghwa-old-song` | 京华老宋体; optional traditional reading style / 可选传统阅读风格 |

The complete copy-paste combinations are commented in `user-fonts.css`, and `font-preview.md` contains actual Markdown samples for comparison.  
完整的可复制组合已写入 `user-fonts.css` 注释中；`font-preview.md` 提供真实 Markdown 样例用于比较。

### Task checkbox alignment / 任务方框对齐

Your confirmed working setting is now the package default:

```css
--jiandu-task-checkbox-align: -0.04em;
```

Negative values move the native checkbox slightly down; positive values move it up.  
负值会让原生方框略向下；正值会让它略向上。

## Code Blocks / 代码块

Jiandu styles only Typora’s outer fenced-code shell, `.md-fences`. Internal `pre` and CodeMirror layers are explicitly flattened, so one Markdown fence receives **one** background, **one** border, and **one** padding layer.

简读只美化 Typora 围栏代码的外层 `.md-fences`。内部的 `pre` 与 CodeMirror 层会被显式压平，因此一个 Markdown 代码块只会有**一层**背景、**一层**边框和**一层**内边距。

This follows the safer compatibility pattern used by Drake: style `.md-fences` instead of applying a global `#write pre` card style.

这一处理参考了 Drake 更稳妥的兼容逻辑：美化 `.md-fences`，而不是给全局 `#write pre` 套卡片样式。

Jiandu also removes CodeMirror’s full-line current-caret highlight. The caret remains visible, and text selection still has a selection highlight; only the distracting background tint of the current line is disabled.

简读同时移除了 CodeMirror 的“光标所在行整行高亮”。光标仍会正常显示，选中文本仍保留选中高亮；仅关闭容易分散注意力的当前行背景色。

## Print and PDF / 打印与导出 PDF

All Jiandu themes include the same automatic A4 print stylesheet. When you choose **Print** or **Export → PDF**, Typora enters a white-paper layout automatically.  
所有简读主题都包含同一套自动 A4 打印规则。当你选择 **打印** 或 **导出 → PDF** 时，Typora 会自动进入白纸排版。

### What the A4 engine handles / A4 打印引擎处理内容

- `@page` target: A4, 18 mm top/bottom and 16 mm left/right margins.  
  `@page` 目标：A4，上下 18 mm、左右 16 mm 页边距。
- White background and dark text, regardless of the selected screen theme.  
  无论屏幕选了什么主题，打印都是白底深色文字。
- Screen decorations, shadows, and dark-mode colours are removed.  
  会移除屏幕装饰、阴影和深色模式配色。
- Images: centered, `max-width: 100%`, proportional scaling, no horizontal clipping, and a maximum printable height.  
  图片：居中、`max-width: 100%`、等比缩放、避免横向裁切，并设置单页可打印最大高度。
- Tables: repeated headers across pages where the print engine supports it; long English names and PCIe fields wrap instead of extending past the page edge.  
  表格：在打印引擎支持时重复表头；长英文名称和 PCIe 字段会换行，避免超出右侧页面边界。
- Code: wrapped instead of being clipped on the right.  
  代码：优先换行，而不是在右侧被裁切。
- Headings, images, quotes, code blocks, Mermaid diagrams, and rows are protected from unnecessary page splitting as far as browser print rules allow.  
  标题、图片、引用、代码块、Mermaid 图和表格行会尽可能避免被不必要地拆页。

### Recommended dialog settings / 建议的打印设置

- Paper size / 纸张：**A4**
- Scale / 缩放：**100%** or **Default / 默认**
- Avoid manually setting a larger scale such as 110%–125%; it can reintroduce image clipping.  
  不要手动放大到 110%–125%；这可能重新导致图片或宽表格被裁切。
- Background graphics / 背景图形：optional. The design remains readable with it disabled.  
  背景图形：可选。即使关闭，主题也应保持可读。

### Practical limitation / 实际限制

A Markdown table with very many columns cannot simultaneously be full-size, never wrap, and never overflow on A4. The theme prioritizes **no clipping**, then readability; very wide technical tables may become compact and wrap inside cells.  
列数特别多的 Markdown 表格无法在 A4 上同时做到“完全不缩小、不换行、永不溢出”。本主题优先级为：**不裁切**，其次是可读性；特别宽的技术表格可能变为更紧凑的字号并在单元格内换行。

---

## Print Test / 打印测试

Open `print-test.md` from this package. It contains:

打开本包中的 `print-test.md`。它包含：

- Wide, tall, and square local PNG images / 宽图、长图、方图；
- A PCIe-style long-field table / PCIe 风格长字段表格；
- Long code lines / 超长代码行；
- Mermaid flow diagram / Mermaid 流程图；
- Mixed Chinese-English paragraphs, task lists, quotes, YAML, and footnotes.  
  中英文混排段落、任务列表、引用、YAML 和脚注。

Print it once to PDF before using the theme for a major document.  
在正式打印重要资料前，建议先导出一次该测试文档为 PDF。

---

## File Map / 文件说明

```text
jiandu/
├─ base.css        Shared import entry / 共用导入入口
├─ fonts.css       Font presets and print fallback chains / 字体预设与打印回退链
├─ user-fonts.css  One-line font selector / 一行字体选择器
├─ core.css        Reading layout, headings, images, tables / 阅读布局、标题、图片、表格
├─ code.css        Inline code, fences, CodeMirror / 行内代码、代码块、源码模式
├─ mermaid.css     Mermaid and diagrams / Mermaid 与图表
├─ ui.css          Sidebar, search, dialogs, buttons / 侧栏、搜索、对话框、按钮
└─ print.css       Automatic A4 print/PDF engine / 自动 A4 打印 / PDF 引擎
```

---

## v0.1.13

- The default screen body, heading, table, and UI stack now prefers **Noto Sans Simplified Chinese / NotoSansSC** for sharper desktop rendering; A4 print/PDF remains Source Han Serif–first.  
  屏幕正文、标题、表格与界面默认改为优先使用 **Noto Sans Simplified Chinese / NotoSansSC**，以获得更清晰的电脑显示；A4 打印 / PDF 仍优先使用思源宋体。
- Added configurable presets for Maple Mono NL NF CN, 方正书宋_GBK、方正博雅宋、方正清刻本悦宋、方正报宋、方正粗黑 / 汉仪粗黑、汉仪旗黑与方正悠黑.  
  新增 Maple Mono NL NF CN、方正书宋_GBK、方正博雅宋、方正清刻本悦宋、方正报宋、方正粗黑 / 汉仪粗黑、汉仪旗黑与方正悠黑的可配置预设。
- Expanded `user-fonts.css` with separate body, heading, table, code, UI, and print/PDF controls, plus ready-made copy-paste combinations.  
  扩展 `user-fonts.css`：正文、标题、表格、代码、界面、打印 / PDF 均可独立配置，并附带可直接复制的组合。
- Added `font-preview.md` for visual comparison of titles, paragraphs, tables, and code.  
  新增 `font-preview.md`，用于直观对比标题、正文、表格和代码字体。
- Applied the user-verified export-canvas safeguard: every theme now exposes a white `--jiandu-bg` page canvas, while its reading-paper tone continues to come from `--jiandu-paper`. This prevents Typora PDF export from showing coloured header/footer bands.  
  应用用户验证有效的导出画布修复：所有主题的 `--jiandu-bg` 统一为白色页面画布，阅读纸张色仍由 `--jiandu-paper` 决定，从而避免 Typora 导出 PDF 出现有色页眉 / 页脚带。
- Set the confirmed native-checkbox alignment to `--jiandu-task-checkbox-align: -0.04em`.  
  将已确认有效的原生任务方框对齐值设为 `--jiandu-task-checkbox-align: -0.04em`。

## Update Notes / 更新建议

When you update this theme later, preserve your `jiandu/user-fonts.css` file if you have customized it. That is the only file intended for your personal font selection.  
以后升级主题时，若你改过字体，请保留自己的 `jiandu/user-fonts.css`。它是唯一专门留给个人字体选择的文件。

---

## Third-Party Notice / 第三方说明

The uploaded Drake theme was used as a compatibility reference for Typora element coverage, such as code blocks, Mermaid diagrams, sidebars, and print behavior. This package is newly organized and restyled for Jiandu. See `THIRD-PARTY-NOTICES.md` for the MIT attribution retained for that reference.  
你提供的 Drake 主题被用作 Typora 元素覆盖范围的兼容性参考，例如代码块、Mermaid 图、侧栏和打印行为。本包按“简读”重新组织与设计；相关 MIT 署名见 `THIRD-PARTY-NOTICES.md`。

## v0.1.9

- Task-list and Mermaid layout compatibility refinements.

## Task checkbox alignment / 任务方框对齐

The theme keeps Typora/Chromium's native checkbox and follows the GitHub theme's list-layout pattern. It only adds a minimal optical adjustment for Song-serif text.

主题保留 Typora/Chromium 原生 checkbox，并遵循 GitHub 主题的列表布局逻辑；仅针对宋体正文做极小的视觉微调。

Edit the following line at the end of `jiandu/user-fonts.css` to tune it locally:

需要自行微调时，修改 `jiandu/user-fonts.css` 文件末尾这一行：

```css
--jiandu-task-checkbox-y: 0.13em;
```

- Larger value = lower square / 数值更大 = 方框更靠下
- Smaller value = higher square / 数值更小 = 方框更靠上
- Recommended range: `0.08em`–`0.20em` / 建议范围：`0.08em`–`0.20em`

## A4 page background / A4 页面背景

When exporting PDF, page-level layers are transparent and the PDF engine's white paper canvas becomes the actual page background. This avoids screen-theme colours leaking into the blank area at page breaks.

导出 PDF 时，页面级容器均为透明，由 PDF 引擎的白色纸张画布作为实际页面背景，从而避免屏幕主题颜色渗入分页空白区域。



---

## Word export / Word 导出

`print-test.md` now references PNG test images only. It can be exported to Word without requiring an SVG renderer.

`print-test.md` 现只引用 PNG 测试图片，导出 Word 时不再依赖 SVG 渲染器。

For your own Markdown files, SVG images may still require `rsvg-convert` when Pandoc/Typora creates a DOCX file. On Windows, install the renderer or convert those SVG files to PNG before export.

对于你自己的 Markdown 文件，如仍包含 SVG，Pandoc/Typora 在导出 DOCX 时仍可能需要 `rsvg-convert`。Windows 下可安装该渲染器，或在导出前将 SVG 转为 PNG。

```powershell
choco install rsvg-convert
```

