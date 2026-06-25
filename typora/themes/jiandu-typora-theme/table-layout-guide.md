# Jiandu Table Layout Guide / 简读表格布局指南

Jiandu v0.2.3 uses **automatic browser column sizing** for ordinary Markdown tables. This is the default because it adapts to different languages, writing systems, and content types without forcing every table into equal columns.

简读 v0.2.3 对普通 Markdown 表格默认使用**浏览器自然分列**。这是默认推荐方式，因为它可以适应不同语言、不同文字系统和不同内容，不会把所有表格强行分成等宽列。

## Important: Markdown dash counts do not control width / 重要：Markdown 横杠数量不控制列宽

This Markdown delimiter row:

```markdown
| Code | Name | Description |
| --- | ----- | ----------- |
```

uses the dashes only to identify a Markdown table. Typora parses the row and does not retain the dash count in the rendered HTML. A CSS theme therefore cannot read or calculate widths from those dash lengths.

下面这个 Markdown 分隔行：

```markdown
| 代码 | 名称 | 描述 |
| --- | ----- | ----------- |
```

横杠只用于识别 Markdown 表格。Typora 解析后不会把横杠数量保留在最终 HTML 中，因此纯 CSS 主题无法读取或根据横杠长度计算列宽。

Use one of the optional layout hints below when a particular table needs manual control.

当某一张表需要手动控制时，请使用下面的可选布局提示。

---

## 1. Automatic layout / 自然布局（默认）

No marker is needed. Short columns tend to remain compact; narrative columns naturally receive more room.

无需标记。短列通常会保持紧凑，说明性长列会自然获得更多空间。

| Message Code / 消息代码 | Name / 名称 | Description / 描述 |
| --- | --- | --- |
| 30h | ERR_COR | A recoverable error was detected. The hardware corrects the condition automatically, while software can still record the trend. |
| 31h | ERR_NONFATAL | A non-fatal error was detected. The device may remain operational, but software should record the evidence and recover when required. |
| 33h | ERR_FATAL | A fatal error was detected. The affected function may need a reset or higher-level recovery action. |

---

## 2. Directional layouts / 方向型布局

Put an empty HTML marker immediately before the table. The marker is hidden in Typora, exported HTML, and PDF.

在表格正前方放一个空 HTML 标记。该标记在 Typora、导出 HTML 和 PDF 中均不显示。

### `narrow-first` / 第一列较窄

Best for ID + description, number + details, date + event, or term + definition.

适合“编号 + 说明”“日期 + 事件”“术语 + 定义”等。

```html
<div class="jiandu-table-layout narrow-first"></div>
```

<div class="jiandu-table-layout narrow-first"></div>

| ID / 编号 | Details / 详情 |
| --- | --- |
| 0 | Attention Button Present: indicates that the enclosure provides an attention button near this location. |
| 14:7 | Slot Power Limit Value: specifies the maximum power that can be delivered at this location. |
| 31:19 | Physical Slot Number: records the associated physical slot number. |

### `wide-first` / 第一列较宽

Best for long item names followed by short data columns.

适合“长项目名称 + 多个短数据列”。

```html
<div class="jiandu-table-layout wide-first"></div>
```

<div class="jiandu-table-layout wide-first"></div>

| Project or Item / 项目或条目 | Status / 状态 | Owner / 负责人 |
| --- | --- | --- |
| Standardized Hot-Plug System Driver | Active | Platform Team |
| Device Driver | Planned | Adapter Vendor |

### `wide-last` / 最后一列较宽

Best for name + provider + explanation, property + source + notes, or any table whose final column is long narrative text.

适合“名称 + 提供方 + 说明”“属性 + 来源 + 备注”等最后一列为长说明的表格。

```html
<div class="jiandu-table-layout wide-last"></div>
```

<div class="jiandu-table-layout wide-last"></div>

| Software Element / 软件要素 | Provider / 提供方 | Description / 描述 |
| --- | --- | --- |
| User Interface | Operating System Vendor | Provides user-facing tools that request a device action, such as power removal or activation. |
| Hot-Plug Service | Operating System Vendor | Processes service requests, coordinates policy, and reports events to higher-level software. |
| Device Driver | Adapter Vendor | Implements device-specific support and reacts to operating-system initiated actions. |

### `balanced` / 均衡列宽

Best for comparison tables in which every column should have equal visual weight.

适合每一列都应该具有相近视觉权重的对比表。

```html
<div class="jiandu-table-layout balanced"></div>
```

---

## 3. Explicit manual ratios / 明确手动比例

For a precise common ratio, use a `ratio-*` class. The class numbers are the column weights in order.

当需要明确比例时，使用 `ratio-*` 类。类名数字就是从左到右各列的权重。

```html
<div class="jiandu-table-layout ratio-2-3-5"></div>
```

This means:

```text
20% / 30% / 50%
```

Example / 示例：

<div class="jiandu-table-layout ratio-2-3-5"></div>

| Code / 代码 | Name / 名称 | Description / 描述 |
| --- | --- | --- |
| 30h | ERR_COR | A recoverable error detected by the device. The condition is corrected automatically, while software can log the event and track recurrence. |
| 31h | ERR_NONFATAL | A non-fatal error that may allow continued operation, but needs software attention and potential recovery. |
| 33h | ERR_FATAL | A fatal condition that can require reset, isolation, replacement, or another recovery action. |

Available ratio classes / 已提供比例类：

| Columns / 列数 | Available classes / 可用类 |
| --- | --- |
| 2 | `ratio-1-1`, `ratio-1-2`, `ratio-1-3`, `ratio-2-3`, `ratio-3-2` |
| 3 | `ratio-1-1-2`, `ratio-1-2-2`, `ratio-1-2-3`, `ratio-2-2-3`, `ratio-2-3-5`, `ratio-3-2-5` |
| 4 | `ratio-1-1-2-2`, `ratio-2-2-3-3` |

Use a ratio whose number of parts matches the number of table columns.

请选择与表格列数相同的比例类。

---

## 4. Density helpers / 紧凑布局

These do not force column widths. They preserve automatic layout while reducing type size and cell padding.

这两种不强制列宽，而是在保留自然分列的同时减小字号和单元格留白。

```html
<div class="jiandu-table-layout compact"></div>
```

- `compact`: moderately smaller text and padding.  
  `compact`：适度缩小字号和留白。

```html
<div class="jiandu-table-layout dense"></div>
```

- `dense`: tighter text and padding for high-density tables.  
  `dense`：更紧凑，适用于高密度表格。

---

## Practical recommendation / 实际建议

1. Start with no marker. / 先不加任何标记。  
2. Use `narrow-first`, `wide-first`, or `wide-last` when one side is clearly special. / 某一侧明显需要更窄或更宽时，使用方向型布局。  
3. Use a `ratio-*` class only when the visual ratio must be exact. / 必须精确控制比例时，再使用 `ratio-*`。  
4. Use `compact` or `dense` for crowded tables before reducing the entire document font size. / 表格过密时优先使用 `compact` 或 `dense`，不要先缩小整篇文档字号。  
