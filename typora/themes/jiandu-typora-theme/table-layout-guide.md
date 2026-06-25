# Jiandu Table Layout Guide / 简读表格布局指南

Jiandu v0.2.4 provides a general table layout system for Markdown writers. It is not tied to a technical field, language, or a fixed number of columns.

简读 v0.2.4 提供通用 Markdown 表格布局系统，不绑定特定技术领域、语言或固定列数。

## 1. Default: automatic sizing / 默认：自然分列

Ordinary Markdown tables use the browser's automatic table layout. This is the recommended starting point for two, three, four, five, six, or more columns.

普通 Markdown 表格默认使用浏览器自然分列。两列、三列、四列、五列、六列或更多列，都建议先从此模式开始。

Short columns tend to remain compact. Descriptive columns naturally receive more room. Long identifiers, URLs, and inline code can wrap inside a cell instead of pushing the whole table wider.

短列通常保持紧凑；说明列会自然获得更多空间。长标识符、URL 和行内代码可以在单元格内换行，不会撑宽整张表。

| Message Code / 消息代码 | Name / 名称 | Description / 描述 |
| --- | --- | --- |
| 30h | ERR_COR | A recoverable condition was detected. Hardware corrects the condition automatically, while software can record and track the event. |
| 31h | ERR_NONFATAL | A non-fatal condition was detected. The device may remain active, but the event should be retained for diagnosis and recovery policy. |
| 33h | ERR_FATAL | A fatal condition was detected. Recovery can require reset, isolation, replacement, or another higher-level action. |

## 2. Why delimiter dashes cannot control width / 为什么横杠数量不能控制列宽

This Markdown delimiter row:

```markdown
| Code | Name | Description |
| --- | ----- | ----------- |
```

uses dashes only to declare a Markdown table. After Typora converts Markdown to HTML, dash counts no longer exist. A CSS theme cannot inspect or calculate widths from them.

下面的 Markdown 分隔行：

```markdown
| 代码 | 名称 | 描述 |
| --- | ----- | ----------- |
```

横杠仅用于声明 Markdown 表格。Typora 转换为 HTML 后，横杠数量已不存在；纯 CSS 主题无法读取或据此计算列宽。

Use one of the optional controls below only when a specific table needs a stable visual plan.

仅当某一张表需要稳定的视觉比例时，再使用以下可选控制方式。

## 3. Quick layout hints / 快速布局提示

Put an empty HTML marker immediately above the target table. It is hidden in Typora, exported HTML, and PDF. It controls only the next table.

在目标表格正上方放一个空 HTML 标记。它在 Typora、导出 HTML 和 PDF 中均不显示，只影响紧随其后的下一张表。

| Hint / 提示 | Use case / 适用场景 |
| --- | --- |
| `narrow-first` | ID / date / term + long details / 编号、日期、术语 + 长说明 |
| `wide-first` | Long row label + several short data columns / 长行标签 + 多个短数据列 |
| `wide-last` | Name + source + narrative description / 名称 + 来源 + 长说明 |
| `narrow-last` | Narrative columns + short final status/unit / 长说明列 + 短状态或单位 |
| `balanced` | Equal visual columns / 均衡列宽 |
| `compact` | Automatic sizing with reduced spacing / 自然分列 + 较紧凑留白 |
| `dense` | High-density automatic tables / 高密度自然表格 |

Example / 示例：

```html
<div class="jiandu-table-layout wide-last"></div>
```

<div class="jiandu-table-layout wide-last"></div>

| Software Element / 软件要素 | Provider / 提供方 | Description / 描述 |
| --- | --- | --- |
| User Interface | Operating system vendor | Provides user-facing tools that request a device action, such as activation, shutdown, or a policy-controlled power-state change. |
| Service Layer | Platform software | Coordinates requests, state reporting, and the transition between application intent and device-specific control logic. |
| Driver | Device vendor | Implements device-specific behavior and reports observable evidence back to the operating system. |

## 4. Common ratio shortcuts / 常用比例快捷方式

For a common stable ratio, use a ratio class above the table.

对于常用且稳定的比例，在表格前使用比例类。

```html
<div class="jiandu-table-layout ratio-2-3-5"></div>
```

This means `20% / 30% / 50%`.

这表示 `20% / 30% / 50%`。

| Columns / 列数 | Available ratio classes / 可用比例类 |
| --- | --- |
| 2 | `ratio-1-1`, `ratio-1-2`, `ratio-1-3`, `ratio-2-3`, `ratio-3-2` |
| 3 | `ratio-1-1-2`, `ratio-1-2-2`, `ratio-1-2-3`, `ratio-2-2-3`, `ratio-2-3-5`, `ratio-3-2-5` |
| 4 | `ratio-1-1-2-2`, `ratio-2-2-3-3`, `ratio-3-2-2-2` |
| 5 | `ratio-3-2-2-2-2` |
| 6 | `ratio-3-2-2-2-2-2` |

## 5. Exact mode: any column count / 精确模式：任意列数

For exact control over any four-, five-, six-, or higher-column table, place a `jiandu-col-w-N` marker around the text in **every header cell**. `N` can be any whole number from `1` to `100`.

对于任意四列、五列、六列或更多列的精确控制，请在**每个表头单元格**的文字外包一层 `jiandu-col-w-N` 标记。`N` 可以是 `1` 到 `100` 的任意整数。

### Rules / 规则

1. Use markers in the header row only. / 仅在表头行使用标记。  
2. Keep all values close to a total of `100`. / 数字总和请尽量接近 `100`。  
3. Use exact mode only when natural sizing or a quick hint is insufficient. / 仅当自然分列或快速提示不够时使用精确模式。  
4. Modern Typora supports this through CSS `:has()`. Older Chromium engines safely fall back to automatic sizing. / 新版 Typora 通过 CSS `:has()` 支持此功能；旧 Chromium 会安全回退到自然分列。  

### Four columns / 四列

```markdown
| <span class="jiandu-col-w-34">State / 状态</span> | <span class="jiandu-col-w-22">Tier A</span> | <span class="jiandu-col-w-22">Tier B</span> | <span class="jiandu-col-w-22">Tier C</span> |
| --- | --- | --- | --- |
| Active | ... | ... | ... |
```

This produces `34% / 22% / 22% / 22%`.

对应 `34% / 22% / 22% / 22%`。

| <span class="jiandu-col-w-34">State / 状态</span> | <span class="jiandu-col-w-22">Tier A</span> | <span class="jiandu-col-w-22">Tier B</span> | <span class="jiandu-col-w-22">Tier C</span> |
| --- | --- | --- | --- |
| Active | The first parallel condition is described here. | The second parallel condition is described here. | The third parallel condition is described here. |
| Recovery Mode | A longer row label stays readable without squeezing every comparison column. | Parallel condition. | Parallel condition. |

### Five columns / 五列

```markdown
| <span class="jiandu-col-w-28">Item</span> | <span class="jiandu-col-w-18">Basic</span> | <span class="jiandu-col-w-18">Pro</span> | <span class="jiandu-col-w-18">Team</span> | <span class="jiandu-col-w-18">Enterprise</span> |
| --- | --- | --- | --- | --- |
```

This produces `28% / 18% / 18% / 18% / 18%`.

对应 `28% / 18% / 18% / 18% / 18%`。

| <span class="jiandu-col-w-28">Item</span> | <span class="jiandu-col-w-18">Basic</span> | <span class="jiandu-col-w-18">Pro</span> | <span class="jiandu-col-w-18">Team</span> | <span class="jiandu-col-w-18">Enterprise</span> |
| --- | --- | --- | --- | --- |
| Data retention | 7 days | 30 days | 180 days | Custom policy and archival controls |
| Support channel | Community | Standard | Priority | Dedicated service arrangement |

### Six columns / 六列

```markdown
| <span class="jiandu-col-w-25">Item</span> | <span class="jiandu-col-w-15">A</span> | <span class="jiandu-col-w-15">B</span> | <span class="jiandu-col-w-15">C</span> | <span class="jiandu-col-w-15">D</span> | <span class="jiandu-col-w-15">Notes</span> |
| --- | --- | --- | --- | --- | --- |
```

This produces `25% / 15% / 15% / 15% / 15% / 15%`.

对应 `25% / 15% / 15% / 15% / 15% / 15%`。

| <span class="jiandu-col-w-25">Item</span> | <span class="jiandu-col-w-15">A</span> | <span class="jiandu-col-w-15">B</span> | <span class="jiandu-col-w-15">C</span> | <span class="jiandu-col-w-15">D</span> | <span class="jiandu-col-w-15">Notes</span> |
| --- | --- | --- | --- | --- | --- |
| Coverage | Included | Included | Optional | Optional | Regional availability may vary |
| Response time | 48 hours | 24 hours | 8 hours | 4 hours | Service-level terms apply |

## Practical recommendation / 实际建议

1. Start with no marker. / 先不加标记。  
2. Use a directional hint when only one edge needs special treatment. / 只有一侧需要变宽或变窄时，使用方向型提示。  
3. Use a ratio shortcut for a common visual plan. / 常见视觉比例使用快捷比例类。  
4. Use `jiandu-col-w-N` for any unique four-, five-, six-, or higher-column variation. / 任意独特的四列、五列、六列或更多列变化，使用 `jiandu-col-w-N`。  
5. Try `compact` or `dense` before shrinking the entire document font. / 表格过密时先使用 `compact` 或 `dense`，不要先缩小整篇文档字号。  
