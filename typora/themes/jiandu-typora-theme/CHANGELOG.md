# Changelog / 更新记录

## v0.2.0 — Typography Presets and WYSIWYG PDF / 字体套餐与所见即所得 PDF

- Added seven coordinated screen typography presets: Screen Clear, Formal Publishing, Newspaper, Retro Jinghua, GitHub Modern, LaTeX Style, and WenKai Notes.  
  新增七套统一屏幕字体套餐：屏幕清晰、正式出版、报刊风格、复古京华、GitHub 现代、LaTeX 学术风格、霞鹜文楷。
- Each preset now sets headings, body, tables, quotes, captions, UI, and code together.  
  每套套餐都会统一设置标题、正文、表格、引用、图注、界面和代码字体。
- `user-fonts.css` now uses a single active `@import` selector plus a Personal Overrides block.  
  `user-fonts.css` 改为单个启用的 `@import` 选择器，并提供个人覆盖区。
- Ordinary Jiandu themes now export PDF using their active screen preset and theme palette inside the document area; PDF typography is no longer forcibly replaced by one global print font.  
  普通简读主题导出 PDF 时会沿用当前屏幕字体套餐与文档内部主题配色，不再被全局固定打印字体强制替换。
- `Jiandu Print Preview` is intentionally independent: it maps all ordinary roles to a fixed formal publishing typography both on screen and in PDF export.  
  `Jiandu Print Preview` 刻意独立：无论屏幕套餐如何，它在屏幕与 PDF 中都映射为固定的正式出版字体。
- Preserved the white export canvas safeguard through `--jiandu-bg: #ffffff`, preventing Typora’s coloured page-header/footer bands.  
  保留 `--jiandu-bg: #ffffff` 的白色导出画布保护，避免 Typora PDF 出现有色页眉 / 页脚带。
- Added quote and caption role variables, so a preset can change these areas without affecting code or UI.  
  新增引用与图注角色变量，使套餐可以单独协调这些区域而不影响代码或界面。

## v0.1.15 — Compact Code Language Tab / 紧凑代码语言标签

- Reworked the active code-language selector into a compact edge tab: no oversized outer panel, no floating shadow, and a restrained border similar to the built-in GitHub theme.
- 将活动代码语言选择器改为贴边小标签：移除过大的外层面板和浮动阴影，使用接近 Typora 内置 GitHub 主题的克制边框与尺寸。

## v0.1.14 — Code Language Selector / 代码语言选择器

- Added a visible background, border, and focus ring for Typora's fenced-code language selector.
  为 Typora 围栏代码块的“代码语言”选择器增加可见背景、边框与聚焦描边。
- Kept the code card itself unchanged; only the active selector toolbar is clarified.
  保持代码卡片本体不变；仅增强活动状态下的选择器工具栏辨识度。

## v0.1.13

- Changed the screen default from Source Han Serif to Noto Sans Simplified Chinese / NotoSansSC for clearer desktop reading. A4 print/PDF still uses the formal Source Han Serif publishing stack.  
  屏幕默认从思源宋体改为 Noto Sans Simplified Chinese / NotoSansSC，以获得更清晰的电脑阅读效果；A4 打印 / PDF 仍使用正式的思源宋体出版字体链。
- Added font presets and bilingual comments for Maple Mono NL NF CN, 方正书宋_GBK、方正博雅宋、方正清刻本悦宋、方正报宋、方正粗黑、汉仪粗黑、汉仪旗黑与方正悠黑.  
  新增 Maple Mono NL NF CN、方正书宋_GBK、方正博雅宋、方正清刻本悦宋、方正报宋、方正粗黑、汉仪粗黑、汉仪旗黑与方正悠黑的字体预设及中英双语说明。
- Expanded `user-fonts.css` so body, heading, table, code, UI, and print/PDF fonts can be customized independently.  
  扩展 `user-fonts.css`，使正文、标题、表格、代码、界面、打印 / PDF 字体均可独立配置。
- Added `font-preview.md` with title, paragraph, table, quote, and code samples.  
  新增 `font-preview.md`，内含标题、正文、表格、引用与代码样例。
- Made the user-proven white export canvas permanent by setting every theme's `--jiandu-bg` to white. The screen document paper tone remains controlled by `--jiandu-paper`.  
  将用户验证有效的白色导出画布固化：所有主题的 `--jiandu-bg` 统一设置为白色；屏幕文档纸张色仍由 `--jiandu-paper` 控制。
- Set the package default checkbox baseline alignment to `-0.04em`.  
  将主题默认任务方框基线对齐设置为 `-0.04em`。


## v0.1.12

- Fix the A4 export canvas: all page-level Typora containers are now explicitly white, preventing coloured top/bottom bands in PDF pages. / 修复 A4 导出画布：所有 Typora 页面级容器统一显式白色，避免 PDF 顶部和底部出现主题色带。
- Fix task-list layout: the first task paragraph is inline rather than inline-block, so native checkboxes and text stay on the same line in PDF and Word export. / 修复任务列表布局：任务首段改为 inline，不再使用 inline-block，使原生方框与文字在 PDF 和 Word 导出中保持同一行。
- Remove relative `top` positioning from native checkboxes; use only a small baseline-alignment variable. / 移除原生复选框的 relative/top 偏移，仅保留轻微基线对齐变量。
- Replace all linked SVG assets in `print-test.md` with PNG files, so Word export no longer needs `rsvg-convert`. / 将 `print-test.md` 中全部引用的 SVG 图片替换为 PNG，Word 导出不再依赖 `rsvg-convert`。
- Add `word-export.md` with bilingual troubleshooting for user documents that still contain SVG files. / 新增 `word-export.md`，中英双语说明用户文档仍含 SVG 时的处理方式。

# Changelog / 更新记录

## v0.1.11

- Fixed PDF page-break colour bands. Printing now keeps page-level containers transparent instead of layering a white `#write` panel over a coloured screen canvas.
  修复 PDF 分页色带。打印时页面级容器保持透明，不再在有色屏幕背景上叠加白色 `#write` 面板。
- Native task checkbox alignment now uses a user-editable `--jiandu-task-checkbox-y` optical offset.
  原生任务方框对齐改为可编辑的 `--jiandu-task-checkbox-y` 视觉偏移量。

## v0.1.10 — Native checkbox visual alignment / 原生复选框视觉对齐

- **Task-list checkbox position / 任务列表方框位置**
  - Kept the real Typora / Chromium checkbox and the GitHub-theme inline-flow approach.
  - Added only `vertical-align: -0.12em` plus zero vertical margins, which lowers the native square slightly to align with the visual center of Song-serif body text.
  - No pseudo-element checkbox, custom tick, absolute positioning, or replacement icon is used.
  - 保留 Typora / Chromium 的真实复选框与 GitHub 主题的行内布局方式。
  - 仅增加 `vertical-align: -0.12em` 和上下外边距归零，让原生方框轻微下移，与宋体正文的视觉中心对齐。
  - 未使用伪元素方框、手绘对号、绝对定位或替代图标。


## v0.1.9 — GitHub-layout compatibility pass / GitHub 布局兼容修订

### Fixed / 修复

- **Task list baseline / 任务列表基线**
  - Removed the custom task-item layout reset.
  - Restored the simple Typora GitHub-theme behavior: `li p.first { display: inline-block; }` and `.md-task-list-item > input { margin-left: -1.3em; }`.
  - The checkbox and first task line now share one natural line instead of placing the box alone above the text.

- **Mermaid raw-block flow / Mermaid 源码块布局**
  - Advanced Mermaid fences no longer use a fixed-height scrolling shell.
  - The Mermaid source editor and rendered preview remain consecutive blocks in normal document flow.
  - The interactive preview SVG is still left to Typora for runtime sizing; the theme does not override its width or height.

- **A4 pagination spacer / A4 分页辅助空白块**
  - Removed the empty `.md-pair-skip` helper from print output, preventing pale header/footer bands between pages.


## v0.1.9 — Mermaid interactive preview repair / Mermaid 交互预览修复

- **Fixed:** Clicking a Mermaid diagram now retains Typora’s native source editor and rendered-preview sizing. The chart no longer collapses into an empty bordered panel in affected Typora builds.
  **修复：** 点击 Mermaid 图后，保留 Typora 原生的源码编辑区与预览尺寸计算；在受影响的 Typora 版本中，不再出现只有边框、图形空白的预览面板。
- Mermaid styles now change colours only; they no longer override interactive preview SVG `display`, `width`, or `height`.
  Mermaid 样式现在只调整配色，不再覆盖交互预览 SVG 的 `display`、`width` 或 `height`。
- Added Mermaid v10 `foreignObject` label colour support and preserved responsive width limiting for the final rendered diagram.
  新增 Mermaid v10 `foreignObject` 标签配色支持，并保留最终渲染图的响应式宽度限制。

# Changelog / 更新记录

## 0.1.7 — 2026-06-25

- Replaced the hand-positioned pseudo-element task checkbox with the native GitHub-style checkbox rule. The real control now remains in inline flow with `margin-left: -1.3em`, so Chromium aligns the box and tick to the text baseline instead of relying on a manually positioned `✓`.  
  将手工定位的伪元素任务方框改为 GitHub 风格的原生复选框规则。真实控件保留在行内布局中并使用 `margin-left: -1.3em`，由 Chromium 按文本基线对齐方框和对号，不再依赖手工定位的 `✓`。
- Applied the same native-control rule to A4 print/PDF output and forced a light control scheme during printing so dark screen themes export stable, readable checkboxes.  
  同步将原生控件规则应用到 A4 打印 / PDF 输出，并在打印时强制使用浅色控件方案，保证深色屏幕主题导出时复选框稳定、清晰。

## 0.1.6 — 2026-06-25

- Changed all Markdown tables to a stable fixed-layout model so a long identifier cannot consume most of the table width. Added an explicit six-column PCIe allocation: Register 19%, Bits 8%, Access 8%, Reset 12%, Behavior 26%, and Firmware notes 27%.  
  将所有 Markdown 表格改为稳定的固定布局，避免长字段占据大部分宽度；并增加六列 PCIe 表格的明确列宽：寄存器 19%、位域 8%、访问 8%、复位值 12%、行为说明 26%、固件备注 27%。
- Reworked task lists using the positioned pseudo-element strategy used by Drake-style themes. Native inputs remain clickable but are removed from inline layout, preventing checkbox squares from drifting to the end of a line.  
  参考 Drake 类主题的定位伪元素策略重做任务列表：原生 input 仍可点击，但不再参与行内排版，避免任务方框漂移到文本行尾。
- Applied the same table and task-list rules to A4 print/PDF output.  
  同步将表格和任务列表规则应用到 A4 打印 / PDF 输出。

## 0.1.5 — 2026-06-25

- Fixed the screen-table header selector: only `<thead>` uses the header colour. The first data row now uses the normal table background, and zebra striping begins from the second data row.  
  修复了屏幕表格表头选择器：只有 `<thead>` 使用表头颜色。第一条数据行恢复普通表格底色，斑马纹从第二条数据行开始。

## 0.1.4 — 2026-06-25

- Restored optional screen-reading presets for **LXGW WenKai / 霞鹜文楷** and **KingHwa OldSong / 京华老宋体**, including common English and Chinese family-name aliases. The default remains the Source Han Serif–first publication stack.  
  恢复了 **霞鹜文楷** 与 **京华老宋体** 的可选屏幕阅读预设，并包含常见中英文家族名别名；默认仍为以思源宋体为优先的出版字体链。
- Removed CodeMirror current-line background highlighting in both fenced code blocks and source mode. The caret and text-selection feedback remain available.  
  移除了围栏代码块与源码模式中的 CodeMirror 光标行背景高亮；光标与文本选择反馈仍然保留。
- Updated bilingual font-selection and code-block documentation.  
  更新了中英双语字体选择与代码块说明。

## 0.1.3 — 2026-06-25

- Fixed nested code-card rendering by removing the global `#write pre` code-block skin. Fenced blocks now style only Typora’s outer `.md-fences` shell; inner `pre` and CodeMirror layers are flattened.  
  修复了代码块多层卡片问题：移除了全局 `#write pre` 代码块皮肤。围栏代码现在只美化 Typora 外层 `.md-fences`，内部 `pre` 与 CodeMirror 层会被压平。
- Added an explicit single-layer code-fence test to `print-test.md` and `typography-test.md`.  
  在 `print-test.md` 与 `typography-test.md` 中增加了单层代码围栏测试。
- Kept the Source Han Serif / Noto Serif CJK SC publication-oriented type system; the selector and documentation contain no handwriting or legacy display-font presets.  
  保持以思源宋体 / Noto Serif CJK SC 为核心的出版型字体体系；选择器和说明文档不再包含手写或旧式展示字体预设。

## 0.1.2 — 2026-06-25

- Set the default type system to a publication-oriented **Source Han Serif / 思源宋体** first stack.  
  将默认字体体系确定为以 **Source Han Serif / 思源宋体** 为优先的出版级宋体回退链。
- Removed handwritten, decorative, and old-style display Song presets from the one-line font selector and documentation.  
  从一行字体选择器与说明文档中移除了手写体、装饰体与旧式展示宋体预设。
- Added publishing typography refinements: inter-ideograph justification for prose, strict Chinese line breaking, left-aligned headings and tables, and centered chapter titles for A4 output.  
  增加出版排版细节：正文中文两端对齐、严格中文换行、标题与表格左对齐、A4 章标题居中。
- Added `typography-test.md` for checking book, academic-paper, newspaper, and PCIe text rendering.  
  新增 `typography-test.md`，用于检查书籍、论文、报刊与 PCIe 技术文本的呈现效果。

## 0.1.1 — 2026-06-25

- Moved the theme toward a restrained book, thesis, and newspaper layout.  
  将主题整体调整为更克制的书籍、论文、报刊式版面。
- Removed coloured heading-bar and dot-marker decorations.  
  移除了标题彩色竖条和圆点装饰。
- Improved bilingual font documentation.  
  完善中英双语字体说明。

## 0.1.0 — 2026-06-25

- Initial Jiandu Typora theme pack.  
  初版简读 Typora 主题包。
- Seven English-named screen themes.  
  提供七套英文文件名的屏幕主题。
- Shared font presets with a one-line user selector in `jiandu/user-fonts.css`.  
  在 `jiandu/user-fonts.css` 中提供一行式字体选择。
- Shared automatic A4 print/PDF stylesheet.  
  提供统一的自动 A4 打印 / PDF 样式。
- Local print test document with image, table, code, Mermaid, and pagination checks.  
  提供含图片、表格、代码、Mermaid 与分页检查的本地打印测试文档。