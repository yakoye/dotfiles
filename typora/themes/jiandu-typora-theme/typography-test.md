---
title: Jiandu Typography Test / 简读字体排版测试
---

# 中文出版排版测试

本文件用于检查“简读”默认的出版级宋体排版效果。正文应当呈现出接近正式书籍、论文与报刊的稳定阅读节奏：中文笔画清晰，英文和数字不过分跳脱，段落在屏幕与 A4 页面中都保持均衡。

PCIe 设备完成复位后，会先进行链路训练，再执行枚举与资源分配。正常流程通常为 **Detect → Polling → Configuration → L0**；若双方支持更高速率，则会继续进行 Gen2、Gen3、Gen4 或更高代际的速率训练。最后进入 L0 状态，软件才能枚举 BAR、配置 MSI/MSI-X，并开始正常访问设备。

## Technical Terms / 技术术语

- `LTSSM`：Link Training and Status State Machine，链路训练与状态状态机。
- `Completion Timeout`：完成超时，必须在设备与软件可接受的范围内配置。
- `0x0000_0000_8000_0000`：64 位 BAR 的示例起始地址。
- The quick brown fox jumps over the lazy dog. 1234567890

## Formal Reading Sample / 正式阅读样张

知识并不只来自快速获取的信息，也来自持续、安静地理解。对于技术资料而言，清晰的层级、稳定的字形、合适的行距和可靠的打印分页，能够让读者更容易识别重点、复查细节，并在纸面上保留可追溯的阅读痕迹。

> 排版的目的不是制造装饰，而是降低阅读阻力。  
> Typography should reduce reading friction instead of becoming decoration.

## Table Sample / 表格样张

| Field / 字段 | Description / 说明 | Example / 示例 |
|---|---|---|
| Link Speed | 当前协商后的链路速率，软件可由 Link Status 寄存器读取。 | Gen4 / 16.0 GT/s |
| Link Width | 当前激活的 Lane 数。 | x16 |
| Completion Timeout | 请求发出后等待 Completion 的上限时间。 | 10 ms |

---



## Chinese and English Punctuation / 中英文标点

中文全角：逗号，句号。分号；冒号：问号？感叹号！顿号、破折号——省略号……引号“”‘’括号（）【】书名号《》。

English ASCII: comma, period. semicolon; colon: question? exclamation! quotes " " ' ' brackets () [] {}.

中英文混排：PCIe 6.0 的状态为 L0，速率为 64 GT/s；the link is active, and no error is reported.

Expected / 预期：中文标点保持全角字形，英文标点保持半角字形；中文逗号不得再显示成类似英文逗号的比例字形。

完整检查见 `punctuation-test.md`。

## Table Layout System / 表格布局系统

普通表格默认按实际内容自然分列；短代码列不会因为主题的全局固定规则被放大，长说明列会获得更多阅读空间。

| Message Code / 消息代码 | Name / 名称 | Description / 描述 |
| --- | --- | --- |
| 30h | ERR_COR | 设备检测到可纠正错误。硬件自动修正条件，软件可以记录事件并观察趋势。 |
| 31h | ERR_NONFATAL | 设备检测到不可纠正但非致命的错误。功能可能继续工作，但软件应保留证据并按策略恢复。 |
| 33h | ERR_FATAL | 设备检测到致命条件，可能需要复位、隔离、替换或其他恢复操作。 |

当一张表需要精确列宽时，使用隐藏标记。下面示例为 `20% / 30% / 50%`：

<div class="jiandu-table-layout ratio-2-3-5"></div>

| Code / 代码 | Name / 名称 | Description / 描述 |
| --- | --- | --- |
| A1 | Short Name | The final explanatory column deliberately receives half of the available width. |
| B2 | Another Name | This remains readable in screen view and A4/PDF output without changing all other tables. |

更多布局提示和比例示例请查看 `table-layout-guide.md`。


## Exact Table Widths / 精确表格列宽

This four-column example uses whole-number width markers directly inside header cells. It is intentionally language-neutral and works for any subject area.

下面四列示例在表头单元格内直接使用整数宽度标记。它不绑定任何主题领域，适用于任意内容。

| <span class="jiandu-col-w-34">State / 状态</span> | <span class="jiandu-col-w-22">A</span> | <span class="jiandu-col-w-22">B</span> | <span class="jiandu-col-w-22">C</span> |
| --- | --- | --- | --- |
| Active | First comparison value. | Second comparison value. | Third comparison value. |
| Recovery Mode | A long label should wrap naturally. | Parallel value. | Parallel value. |

For a full 2–6 column test matrix, open `table-layout-test.md`.

二至六列完整测试矩阵请打开 `table-layout-test.md`。


## Exact Table Widths / 精确表格列宽

This four-column example uses integer width markers inside each header cell. It works for any subject area; the labels are only an example.

下面四列示例在每个表头单元格中使用整数宽度标记。它适用于任意主题领域，表头名称仅为示例。

| <span class="jiandu-col-w-34">State / 状态</span> | <span class="jiandu-col-w-22">A</span> | <span class="jiandu-col-w-22">B</span> | <span class="jiandu-col-w-22">C</span> |
| --- | --- | --- | --- |
| Active | First comparison value. | Second comparison value. | Third comparison value. |
| Recovery Mode | A long label should wrap naturally. | Parallel value. | Parallel value. |

For complete two- to six-column examples, open `table-layout-test.md`.

完整的二至六列示例见 `table-layout-test.md`。

## Single-layer Code Fence Test / 单层代码围栏测试

The following fence should render as one card only: one background, one border, and one padding layer.
Move the caret inside the fence: no full-line current-caret tint should appear.

下面这段围栏代码应只呈现为一张卡片：一层背景、一层边框、一层内边距。
将光标移入代码块：不应出现整行的光标行背景色。

```css
/* Outer fence only / 只美化外层围栏 */
.md-fences {
    padding: 0.92rem 1.08rem;
    border: 1px solid var(--jiandu-code-border);
}

/* Internal layers stay flat / 内部层保持扁平 */
.md-fences pre,
.md-fences .CodeMirror {
    margin: 0;
    padding: 0;
    background: transparent;
    border: 0;
}
```

