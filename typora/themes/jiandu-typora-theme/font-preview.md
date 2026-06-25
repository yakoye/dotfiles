# Font Preview / 字体预览

> Change `jiandu/user-fonts.css`, switch back to the Jiandu theme in Typora, then use this file to compare screen typography.  
> 修改 `jiandu/user-fonts.css` 后，在 Typora 中切换到其他主题再切回简读，然后用本文对比屏幕字体效果。

---

# Chapter Title / 一级标题：PCIe 文档字体预览

## Section Title / 二级标题：正文、表格与代码的协同

### Subsection / 三级标题：屏幕清晰度与出版排版

一段中文正文示例：PCIe 技术资料通常需要同时兼顾寄存器字段、协议术语、英文缩写与连续中文叙述。屏幕阅读更强调字形清晰、笔画稳定和中英文混排节奏；打印 / PDF 则更强调纸面密度、分页稳定性以及表格的可读性。

English sample: When the Endpoint receives a Configuration Write Request, firmware records the programmed value, checks the LTSSM transition, and preserves AER evidence for later diagnosis.

> Quote sample / 引用示例：正文、标题和引用不必使用同一字体；关键是正文清楚、标题有层次、代码等宽且稳定。

## Body / 正文预设试读

- `--jiandu-font-noto-sans-sc`：Noto Sans Simplified Chinese，推荐电脑屏幕技术阅读。
- `--jiandu-font-publishing`：思源宋体 / Source Han Serif，推荐正式书刊与 PDF。
- `--jiandu-font-fz-shusong-gbk`：方正书宋_GBK，正式书籍正文。
- `--jiandu-font-fz-boyasong`：方正博雅宋，适合有书卷气的长文。
- `--jiandu-font-fz-qingkeben-yuesong`：方正清刻本悦宋，古典感较强。
- `--jiandu-font-fz-baosong`：方正报宋，适合报刊或评论文体。

## Heading / 标题预设试读

- `--jiandu-font-fz-youhei`：方正悠黑，稳重的技术标题。
- `--jiandu-font-hy-qihei`：汉仪旗黑，清爽的现代标题。
- `--jiandu-font-heavy-black`：方正粗黑 / 汉仪粗黑，适合少量强强调标题。
- `--jiandu-font-fz-baosong`：方正报宋，适合书刊或报纸式标题。

## Table / 表格示例

| Register / 寄存器 | Access / 访问 | Description / 说明 |
| --- | --- | --- |
| `PCI_EXP_LNKCTL2_TARGET_LINK_SPEED` | RW | Software-requested target link speed. Noto Sans SC is often clearer on a display for dense technical fields. |
| `AER_UNCORRECTABLE_ERROR_STATUS` | RW1C | Preserve error evidence before clearing bits. |

## Code / 代码示例

```c
/* Maple Mono NL NF CN preview / Maple Mono NL NF CN 预览 */
static void pcie_dump_link_state(struct pcie_port *port)
{
    log_info("speed=Gen%u width=x%u ltssm=%s aer=0x%08x",
             port->current_gen, port->current_width,
             port->ltssm_name, port->aer_uncorrectable_status);
}
```

Inline code / 行内代码：`LinkCtl2[3:0]`、`0x0000000000000042`、`Completion Timeout`。

## Suggested combinations / 推荐组合

### Clear technical screen / 清晰技术屏幕

```css
--jiandu-reading-font: var(--jiandu-font-noto-sans-sc);
--jiandu-heading-font: var(--jiandu-font-fz-youhei);
--jiandu-table-font: var(--jiandu-font-noto-sans-sc);
--jiandu-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
```

### Formal publication / 正式出版

```css
--jiandu-reading-font: var(--jiandu-font-publishing);
--jiandu-heading-font: var(--jiandu-font-fz-baosong);
--jiandu-table-font: var(--jiandu-font-publishing);
--jiandu-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
```

### FZ ShuSong book style / 方正书宋书籍风格

```css
--jiandu-reading-font: var(--jiandu-font-fz-shusong-gbk);
--jiandu-heading-font: var(--jiandu-font-fz-boyasong);
--jiandu-table-font: var(--jiandu-font-noto-sans-sc);
--jiandu-code-font: var(--jiandu-font-maple-mono-nl-nf-cn);
```
