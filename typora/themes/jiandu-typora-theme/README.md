# Jiandu Typora Theme

> **v0.2.4 / v0.2.4**  
> Reading-first Typora themes with coordinated screen font presets, WYSIWYG PDF export for ordinary themes, and one independent formal-print theme.  
> 一套以阅读为先的 Typora 主题：提供统一的屏幕字体套餐、普通主题所见即所得 PDF 导出，以及一套独立固定的正式印刷主题。

## Highlights / 核心特点

- Seven colour themes: Natural Paper, Bright White, Warm Beige, Mist Blue, Night Green, Deep Navy, and Print Preview.  
  七套配色主题：自然纸张、明亮白、暖米色、雾蓝、夜间绿、深墨蓝、印刷预览。
- Eight coordinated screen font presets: Screen Clear, Formal Publishing, Source Han Serif, Newspaper, Retro Jinghua, GitHub Modern, LaTeX Style, and WenKai Notes.  
  八套统一字体套餐：屏幕清晰、正式出版、思源宋体、报刊风格、复古京华、GitHub 现代、LaTeX 学术风格、霞鹜文楷。
- A preset applies to headings, body, tables, quotes, captions, UI, and code together.  
  一套套餐会同时应用到标题、正文、表格、引用、图注、界面和代码。
- Ordinary Jiandu themes export PDF using the current screen font preset and the document’s own theme style.  
  普通简读主题导出 PDF 时保留当前屏幕字体套餐与文档风格，尽量所见即所得。
- `Jiandu Print Preview` deliberately ignores screen font presets and uses a fixed formal publishing typography on screen and in PDF.  
  `Jiandu Print Preview` 刻意不跟随屏幕字体套餐，在屏幕与 PDF 中都使用固定正式出版字体。
- The outer export canvas remains white to prevent Typora PDF header/footer colour bands.  
  导出页面最外层画布保持白色，避免 Typora PDF 出现有色页眉 / 页脚带。

## Install / 安装

1. In Typora, open **File → Preferences → Appearance → Open Theme Folder**.  
   在 Typora 中打开：**文件 → 偏好设置 → 外观 → 打开主题文件夹**。
2. Copy the seven top-level `jiandu-*.css` files and the complete `jiandu` folder into that theme folder.  
   将根目录下七个 `jiandu-*.css` 文件以及完整的 `jiandu` 文件夹，一起复制到主题文件夹中。
3. Keep this structure unchanged / 请保持目录结构：

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
   ├─ font-presets/
   │  ├─ screen-clear.css
   │  ├─ formal-publishing.css
   │  ├─ source-han-serif.css
   │  ├─ newspaper.css
   │  ├─ retro-jinghua.css
   │  ├─ github-modern.css
   │  ├─ latex-style.css
   │  └─ wenkai-notes.css
   ├─ core.css
   ├─ code.css
   ├─ mermaid.css
   ├─ ui.css
   └─ print.css
```

4. Restart Typora, or switch away and back to reload the theme.  
   重启 Typora，或者先切换到其他主题再切回来。

> `assets/`, `font-preview.md`, `table-layout-guide.md`, `table-layout-test.md`, `print-test.md`, `typography-test.md`, and `word-export.md` are tests and documentation. They do not need to be copied into Typora’s theme folder.  
> `assets/`、`font-preview.md`、`table-layout-guide.md`、`table-layout-test.md`、`print-test.md`、`typography-test.md`、`word-export.md` 是测试与说明文件，不需要复制到 Typora 主题文件夹。

## Choose a Screen Font Preset / 选择屏幕字体套餐

Open `jiandu/user-fonts.css`. At the top, keep **one** import line active:

打开 `jiandu/user-fonts.css`，在顶部只保留**一行**启用的导入：

```css
@import url("./font-presets/screen-clear.css");

/* @import url("./font-presets/formal-publishing.css"); */
/* @import url("./font-presets/source-han-serif.css"); */
/* @import url("./font-presets/newspaper.css"); */
/* @import url("./font-presets/retro-jinghua.css"); */
/* @import url("./font-presets/github-modern.css"); */
/* @import url("./font-presets/latex-style.css"); */
/* @import url("./font-presets/wenkai-notes.css"); */
```

| Preset / 套餐 | Best for / 适合 |
| --- | --- |
| Screen Clear / 屏幕清晰 | Noto Sans SC + Maple Mono；Windows/macOS 技术资料、PCIe、日常笔记 |
| Formal Publishing / 正式出版 | 思源宋体正文 + 方正博雅宋标题优先；书籍、论文、长报告 |
| Source Han Serif / 思源宋体 | 标题与正文统一思源宋体；正式书刊、论文、长篇技术文档 |
| Newspaper / 报刊风格 | 方正报宋 / 方正粗黑优先；评论、报刊、史料 |
| Retro Jinghua / 复古京华 | 京华老宋体；日记、随笔、旧书感阅读 |
| GitHub Modern / GitHub 现代 | README、项目说明、开发笔记 |
| LaTeX Style / LaTeX 学术风格 | 论文、规范、公式与架构文档 |
| WenKai Notes / 霞鹜文楷 | 日记、读书笔记、随笔 |

All requested local fonts are referenced through safe font stacks: Noto Sans SC, Maple Mono NL NF CN, 方正书宋_GBK、方正博雅宋、方正清刻本悦宋、方正报宋、方正粗黑、汉仪粗黑、汉仪旗黑、方正悠黑、霞鹜文楷与京华老宋体。When a preferred font is not installed, the stack falls back to Windows/macOS/system fonts automatically.  
所有字体只按本机字体栈引用：Noto Sans SC、Maple Mono NL NF CN、方正书宋_GBK、方正博雅宋、方正清刻本悦宋、方正报宋、方正粗黑、汉仪粗黑、汉仪旗黑、方正悠黑、霞鹜文楷与京华老宋体。若优选字体没有安装，会自动回退到 Windows、macOS 或通用字体。

## Personal Font Overrides / 个人字体覆盖

After choosing a preset, you can replace only the role you dislike in the `Personal Overrides` block of `jiandu/user-fonts.css`.

选好套餐后，可以在 `jiandu/user-fonts.css` 的 `Personal Overrides / 个人覆盖区` 中，只替换你不喜欢的那个角色：

```css
/* Order / 顺序：标题 → 正文 → 表格 → 引用 → 图注 → 界面 → 代码 */
--jiandu-heading-font: var(--jiandu-font-fz-youhei);
--jiandu-reading-font: var(--jiandu-font-noto-sans-sc);
--jiandu-table-font: var(--jiandu-font-noto-sans-sc);
--jiandu-quote-font: var(--jiandu-font-noto-sans-sc);
--jiandu-caption-font: var(--jiandu-font-noto-sans-sc);
--jiandu-ui-font: var(--jiandu-font-noto-sans-sc);
--jiandu-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
```

For example, retain the whole selected preset but use a different code font:

例如，保留整个套餐，只换代码字体：

```css
--jiandu-code-font: var(--jiandu-font-github-mono);
/* or / 或 */
--jiandu-code-font: var(--jiandu-font-latex-mono);
```

Task-checkbox baseline alignment is now fixed in `jiandu/core.css` and is no longer a user setting:

已确认有效的任务方框基线对齐已固定在 `jiandu/core.css`，不再作为用户字体设置暴露：

```css
--jiandu-task-checkbox-align: -0.04em;
```

Do not copy this rule into `user-fonts.css`; it intentionally stays unchanged across all font presets.  
不要把这条规则复制到 `user-fonts.css`；它会在所有字体套餐中保持不变。


## Tables / 表格

### Default behavior / 默认行为

Ordinary Markdown tables use browser-driven automatic column sizing. This lets short columns remain compact and gives descriptive columns more room, instead of forcing every two-column or three-column table into equal widths.

普通 Markdown 表格使用浏览器自然分列。短列会保持紧凑，长说明列会得到更多空间；不再把所有两列、三列表格强制分成等宽。

Long words, URLs, identifiers, and inline code can wrap inside cells, so a single unbroken string does not push the table beyond the document width.

长英文、URL、标识符和行内代码可以在单元格内换行，避免一条长字符串把表格撑出文档宽度。

### Optional per-table hints / 可选的单表布局提示

When one particular table needs manual control, put an empty marker directly above it:

当某一张表需要手动控制时，在它正上方加入一个空标记：

```html
<div class="jiandu-table-layout wide-last"></div>
```

The marker is hidden in Typora and in exports. It only controls the next table.

该标记在 Typora 和导出结果中不显示，只影响紧随其后的下一张表。

Available general-purpose layouts / 可用的通用布局：

| Hint / 提示 | Purpose / 用途 |
| --- | --- |
| none or `auto` | Natural browser sizing / 浏览器自然分列 |
| `balanced` | Equal visual columns / 均衡列宽 |
| `narrow-first` | ID, date, number, term + details / 编号、日期、术语 + 详情 |
| `wide-first` | Long item name + short data / 长名称 + 短数据 |
| `wide-last` | Name + source + long description / 名称 + 来源 + 长说明 |
| `compact` | Automatic columns with smaller spacing / 自然分列 + 较紧凑留白 |
| `dense` | High-density automatic table / 高密度自然表格 |
| `ratio-2-3-5` | Explicit 20% / 30% / 50% example / 明确 20% / 30% / 50% 示例 |

For a full list of ratio classes, exact `jiandu-col-w-N` header markers, and live Markdown examples, open `table-layout-guide.md` and `table-layout-test.md`.

完整比例类、精确 `jiandu-col-w-N` 表头标记与可直接预览的 Markdown 示例见 `table-layout-guide.md` 和 `table-layout-test.md`。

> Markdown delimiter dash lengths such as `| --- | ----- | ----------- |` do not control rendered column width. Typora discards those counts when it converts Markdown to HTML, so a CSS theme cannot calculate them.  
> Markdown 分隔行中的横杠长度，例如 `| --- | ----- | ----------- |`，不会控制渲染后的列宽。Typora 转换为 HTML 时会丢弃横杠数量，因此 CSS 主题无法据此计算列宽。



### Exact widths for any column count / 任意列数的精确宽度

For any four-, five-, six-, or higher-column variation, place `jiandu-col-w-N` inside each header cell. `N` is a whole-number percentage from `1` to `100`.

对于任意四列、五列、六列或更多列的变化，可在每个表头单元格中使用 `jiandu-col-w-N`。`N` 是 `1` 到 `100` 的整数百分比。

```markdown
| <span class="jiandu-col-w-34">State</span> | <span class="jiandu-col-w-22">A</span> | <span class="jiandu-col-w-22">B</span> | <span class="jiandu-col-w-22">C</span> |
| --- | --- | --- | --- |
```

Keep the header widths close to a total of 100. This is progressive enhancement: modern Typora renders the exact plan; old Chromium builds safely fall back to automatic sizing.

请让表头宽度总和接近 100。这是渐进增强：新版 Typora 会按精确方案渲染；较旧 Chromium 会安全回退到自然分列。


### Exact widths for any column count / 任意列数的精确宽度

For a unique four-, five-, six-, or higher-column arrangement, place `jiandu-col-w-N` around the text in each header cell. `N` is an integer percentage from `1` to `100`.

对于独特的四列、五列、六列或更多列布局，可在每个表头单元格文字外使用 `jiandu-col-w-N`。`N` 是 `1` 至 `100` 的整数百分比。

```markdown
| <span class="jiandu-col-w-34">State</span> | <span class="jiandu-col-w-22">A</span> | <span class="jiandu-col-w-22">B</span> | <span class="jiandu-col-w-22">C</span> |
| --- | --- | --- | --- |
```

Keep all values close to 100. Modern Typora applies the exact plan on screen and in A4/PDF; older Chromium safely falls back to automatic sizing.

请让所有数值总和接近 100。新版 Typora 会在屏幕和 A4/PDF 中应用精确方案；旧 Chromium 会安全回退到自然分列。

## PDF and Print / PDF 与打印

### Ordinary themes / 普通主题

When using Natural Paper, Bright White, Warm Beige, Mist Blue, Night Green, or Deep Navy, PDF export keeps the active screen typography preset and document-area theme style. This is intended for PDFs that are read on screens as well as sent to others.  
使用自然纸张、明亮白、暖米色、雾蓝、夜间绿或深墨蓝时，PDF 导出会保留当前屏幕字体套餐和正文区域的主题风格，适合在屏幕上阅读或发送给他人的 PDF。

### Jiandu Print Preview / 简读·印刷预览

`Jiandu Print Preview` is a dedicated formal-print mode. Its stylesheet explicitly sets these roles and maps them into the normal theme roles; it does **not** follow `user-fonts.css` screen presets:

`Jiandu Print Preview` 是专门的正式印刷模式。它会显式设置下列角色并映射为普通主题角色；它**不会**跟随 `user-fonts.css` 的屏幕套餐：

```css
--jiandu-print-heading-font: var(--jiandu-font-publishing);
--jiandu-print-body-font: var(--jiandu-font-publishing);
--jiandu-print-table-font: var(--jiandu-print-body-font);
--jiandu-print-quote-font: var(--jiandu-print-body-font);
--jiandu-print-caption-font: var(--jiandu-font-noto-sans-sc);
--jiandu-print-ui-font: var(--jiandu-font-noto-sans-sc);
--jiandu-print-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
```

Choose this theme when you need A4 printing, a formal book/paper PDF, or a stable archival appearance.  
当需要 A4 打印、正式书刊式 PDF、稳定的归档外观时，选择该主题。

All themes keep `--jiandu-bg: #ffffff` as the export-safe outer canvas; this fixes Typora’s blank top/bottom page bands.  
所有主题都保持 `--jiandu-bg: #ffffff` 作为导出安全的外层画布，用于解决 Typora 分页顶部 / 底部出现有色空白带的问题。

### A4 safeguards / A4 保护逻辑

- A4 pages use 18 mm top/bottom and 16 mm left/right margins.  
  A4 页面使用上下 18 mm、左右 16 mm 页边距。
- Images remain centered, proportional, and inside printable width.  
  图片保持居中、等比缩放，不超出可打印宽度。
- Long PCIe fields and code lines wrap instead of clipping at the right edge.  
  长 PCIe 字段和长代码行会换行，而不是从右侧裁切。
- Tables repeat headers where the print engine supports it.  
  表格会在打印引擎支持时重复表头。

## Validation Files / 验证文件

- `font-preview.md` — compare screen presets and personal overrides. / 对比字体套餐与个人覆盖效果。
- `print-test.md` — test A4 images, tables, code, Mermaid, task lists, and page breaks. / 测试 A4 图片、表格、代码、Mermaid、任务列表与分页。
- `typography-test.md` — general rendering tests. / 通用排版测试。
- `table-layout-guide.md` — automatic sizing, manual hints, exact header widths, and ratio examples. / 自然分列、手动提示、精确表头宽度与比例示例。
- `table-layout-test.md` — live 2–6 column screen and PDF verification. / 二至六列表格的屏幕与 PDF 实测文档。
- `word-export.md` — notes on SVG and Word export. / SVG 与 Word 导出说明。

## Updating / 更新

Before replacing an older version, back up your local `jiandu/user-fonts.css` if you customized it. After copying this version, reapply your selected `@import` line and personal overrides.  
替换旧版本前，若你修改过本地 `jiandu/user-fonts.css`，请先备份。复制新版本后，再恢复你选定的 `@import` 行与个人覆盖设置。

## License and Attribution / 许可证与致谢

The theme is an original Jiandu reorganization and design. Drake and GitHub theme files supplied during development were used only as compatibility references for Typora structures such as fences, Mermaid, sidebars, and task lists. See `THIRD-PARTY-NOTICES.md` for applicable attribution.  
本主题为简读的重新组织与设计。开发过程中，用户提供的 Drake 和 GitHub 主题仅作为 Typora 结构兼容性参考，例如围栏代码、Mermaid、侧栏与任务列表。相关署名见 `THIRD-PARTY-NOTICES.md`。
