# Font Preset Preview / 字体套餐预览

> Select a preset in `jiandu/user-fonts.css`, then switch Typora to another theme and back to reload it.  
> 在 `jiandu/user-fonts.css` 选择字体套餐后，先切换到其他主题再切回简读，以便 Typora 重新加载。

> Ordinary Jiandu themes export with the active screen preset. `Jiandu Print Preview` is deliberately independent and stays on its fixed formal-print typography.  
> 普通简读主题导出 PDF 时沿用当前屏幕套餐；`Jiandu Print Preview` 则刻意独立，固定使用正式印刷字体。

---

# Chapter Title / 一级标题：PCIe 文档字体预览

## Section Title / 二级标题：标题、正文、表格、引用与代码协同

### Subsection / 三级标题：Windows 屏幕清晰度与 A4 输出风格

中文正文示例：PCIe 技术资料通常需要同时兼顾寄存器字段、协议术语、英文缩写与连续中文叙述。屏幕阅读更强调字形清晰、笔画稳定和中英文混排节奏；导出 PDF 时，普通主题会继续使用当前套餐，因此可以保留你正在阅读的风格。

English sample: When the Endpoint receives a Configuration Write Request, firmware records the programmed value, checks the LTSSM transition, and preserves AER evidence for later diagnosis.

> Quote sample / 引用示例：同一套餐会同步作用于标题、正文、表格、引用、图注、界面和代码。你可以在 `user-fonts.css` 的“个人覆盖区”只替换其中一个角色，例如只换代码字体。

## Preset Summary / 套餐速览

| Preset / 套餐 | Intended use / 适用场景 | Default core combination / 默认核心组合 |
| --- | --- | --- |
| Screen Clear / 屏幕清晰 | Windows/macOS 技术资料、日常笔记 | Noto Sans SC + Maple Mono |
| Formal Publishing / 正式出版 | 书籍、论文、长报告 | 思源宋体 + 方正博雅宋（已安装时） |
| Newspaper / 报刊风格 | 评论、史料、报刊式长文 | 方正报宋 + 方正粗黑（已安装时） |
| Retro Jinghua / 复古京华 | 日记、随笔、旧书感阅读 | 京华老宋体 + Maple Mono |
| GitHub Modern / GitHub 现代 | README、项目说明、开发笔记 | 系统现代无衬线 + GitHub Mono |
| LaTeX Style / LaTeX 学术风格 | 论文、规范、公式文档 | Latin Modern / CMU + CJK 宋体回退 |
| WenKai Notes / 霞鹜文楷 | 日记、读书笔记、随笔 | 霞鹜文楷 + Maple Mono |

## Body and Table / 正文与表格

| Register / 寄存器 | Access / 访问 | Description / 说明 |
| --- | --- | --- |
| `PCI_EXP_LNKCTL2_TARGET_LINK_SPEED` | RW | Software-requested target link speed. Compare letter spacing, Chinese readability, and long field wrapping. |
| `AER_UNCORRECTABLE_ERROR_STATUS` | RW1C | Preserve error evidence before clearing bits. Compare body, table, and inline-code consistency. |

## Code / 代码

```c
/* Code font preview / 代码字体预览 */
static void pcie_dump_link_state(struct pcie_port *port)
{
    log_info("speed=Gen%u width=x%u ltssm=%s aer=0x%08x",
             port->current_gen, port->current_width,
             port->ltssm_name, port->aer_uncorrectable_status);
}
```

Inline code / 行内代码：`LinkCtl2[3:0]`、`0x0000000000000042`、`Completion Timeout`。

## Personal Override Examples / 个人覆盖示例

Keep the chosen preset, but replace only the code font / 保持当前套餐，只替换代码字体：

```css
--jiandu-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
/* or / 或 */
--jiandu-code-font: var(--jiandu-font-github-mono);
/* or / 或 */
--jiandu-code-font: var(--jiandu-font-latex-mono);
```

Keep the chosen preset, but use a stronger technical heading / 保持当前套餐，只替换更有力度的技术标题：

```css
--jiandu-heading-font: var(--jiandu-font-fz-youhei);
/* or / 或 */
--jiandu-heading-font: var(--jiandu-font-hy-qihei);
```

Use a formal Song body while retaining a clear Noto Sans SC table / 正文使用正式宋体，表格保留清晰的 Noto Sans SC：

```css
--jiandu-reading-font: var(--jiandu-font-publishing);
--jiandu-table-font: var(--jiandu-font-noto-sans-sc);
```

## Print Preview Check / 印刷预览检查

Switch to **Jiandu Print Preview** and compare this same file. It should use its fixed formal publishing fonts whether your active screen preset is Screen Clear, WenKai Notes, or GitHub Modern.  
切换到 **Jiandu Print Preview** 后再查看本文：无论你当前屏幕套餐是 Screen Clear、霞鹜文楷还是 GitHub Modern，它都应稳定使用固定的正式出版字体。
