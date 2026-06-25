# Changelog / 更新记录

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
