# Jiandu Typora Theme

> A reading-first Typora theme pack with an A4-oriented print / PDF engine.  
> 一套以阅读体验为先、并重点面向 A4 打印 / 导出 PDF 的 Typora 主题包。

**Version / 版本：** `0.1.5`  
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
- Task lists use the real GitHub-style native checkbox in normal inline flow. The browser controls the tick baseline, preventing a hand-drawn checkmark from sitting too high.  
  任务列表采用 GitHub 风格的真实原生复选框并保留正常行内布局；对号基线由浏览器处理，避免手工绘制的对号偏上。
- Formal book / thesis / newspaper typography is the default; screen font remains a one-line setting and print fonts stay independent and stable.  
  默认采用正式书籍 / 论文 / 报刊式字体；屏幕字体仍只需改一行，打印字体独立固定，保证分页和技术排版稳定。

---

## Default Typography / 默认排版方向

Jiandu now defaults to `--jiandu-font-publishing`, a publication-oriented Song-serif stack that prefers **Source Han Serif SC / 思源宋体** and then uses Noto Serif CJK SC and system Song fallbacks. This is intentionally a clean, modern Chinese publishing face: suitable for books, academic papers, newspapers, and PCIe technical reference material, rather than handwritten or decorative reading styles.  
简读现在默认使用 `--jiandu-font-publishing`，这是一套面向出版排版的宋体回退链，优先调用 **Source Han Serif SC / 思源宋体**，再使用 Noto Serif CJK SC 与系统宋体回退。它刻意采用干净、现代、适合出版物的中文宋体风格，用于书籍、论文、报刊和 PCIe 技术参考资料，而不是手写体或装饰性阅读字体。

Screen headings use the same formal family and rely on size, weight, spacing, and thin rules for hierarchy. Coloured bars and dot markers are intentionally removed.  
屏幕标题默认与正文使用同一正式字体，通过字号、字重、留白和细分隔线建立层级；已刻意去除彩色竖条和圆点装饰。

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

> `assets/` and `print-test.md` are optional test files. They do not need to be copied into the Typora theme folder.  
> `assets/` 和 `print-test.md` 是可选测试文件，不需要复制到 Typora 主题文件夹。

---

## Font Selection — Change One Line / 字体选择：只改一行

Open `jiandu/user-fonts.css`, then change **only** this line:

打开 `jiandu/user-fonts.css`，只修改下面这一行：

```css
--jiandu-reading-font: var(--jiandu-font-publishing);
```

Available choices / 可选字体预设：

```css
/* Source Han Serif / 思源宋体 — default / 默认：正式书籍、论文、报刊与技术资料 */
--jiandu-reading-font: var(--jiandu-font-publishing);

/* System Song fallback / 系统宋体回退 — compact system-native book layout / 紧凑的系统原生书面布局 */
--jiandu-reading-font: var(--jiandu-font-system-song);

/* LXGW WenKai / 霞鹜文楷 — optional screen reading / 可选：屏幕长文、笔记与日记 */
--jiandu-reading-font: var(--jiandu-font-wenkai);

/* KingHwa OldSong / 京华老宋体 — optional traditional book feeling / 可选：传统旧书阅读气质 */
--jiandu-reading-font: var(--jiandu-font-kinghwa-old-song);

/* Technical sans / 技术无衬线 — dense engineering editing only / 仅适合密集工程编辑 */
--jiandu-reading-font: var(--jiandu-font-technical-sans);
```

> Common aliases are also available: `--jiandu-font-lxgw-wenkai`, `--jiandu-font-kinghwa`, and `--jiandu-font-old-song`.  
> 同时提供常用别名：`--jiandu-font-lxgw-wenkai`、`--jiandu-font-kinghwa` 与 `--jiandu-font-old-song`。

### Important font behavior / 字体逻辑说明

- Your one-line choice affects screen body text, headings, quotes, and tables.  
  这一行会影响屏幕正文、标题、引用和表格。
- Code, register fields, commands, and ASCII diagrams remain in a monospace font.  
  代码、寄存器字段、命令行和 ASCII 图始终使用等宽字体。
- Print / PDF uses a dedicated, stable Source Han Serif–first publishing stack for body and headings, plus a separate code font. It deliberately does **not** follow the screen-font switch.  
  打印 / PDF 使用独立、稳定、以思源宋体为优先的出版级正文与标题字体，并使用独立代码字体；不会跟随屏幕字体开关，从而减少分页和表格宽度变化。
- A font must already be installed on your system. If Source Han Serif is missing, the next family in the fallback chain is used.  
  对应字体需要已安装在系统中；若未安装思源宋体，会自动使用回退链中的下一种字体。

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

- Wide, tall, and square local SVG images / 宽图、长图、方图；
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

## Update Notes / 更新建议

When you update this theme later, preserve your `jiandu/user-fonts.css` file if you have customized it. That is the only file intended for your personal font selection.  
以后升级主题时，若你改过字体，请保留自己的 `jiandu/user-fonts.css`。它是唯一专门留给个人字体选择的文件。

---

## Third-Party Notice / 第三方说明

The uploaded Drake theme was used as a compatibility reference for Typora element coverage, such as code blocks, Mermaid diagrams, sidebars, and print behavior. This package is newly organized and restyled for Jiandu. See `THIRD-PARTY-NOTICES.md` for the MIT attribution retained for that reference.  
你提供的 Drake 主题被用作 Typora 元素覆盖范围的兼容性参考，例如代码块、Mermaid 图、侧栏和打印行为。本包按“简读”重新组织与设计；相关 MIT 署名见 `THIRD-PARTY-NOTICES.md`。
