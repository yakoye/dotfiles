# Jiandu Table Layout Test / 简读表格布局测试

This file tests automatic sizing, quick hints, and exact widths from two through six columns. Open it in Typora and also export it to PDF.

本文测试自然分列、快速布局提示和两至六列的精确宽度。请在 Typora 中打开，并导出 PDF 验证。

## 1. Automatic Layout / 自然分列

| Code / 代码 | Name / 名称 | Description / 描述 |
| --- | --- | --- |
| 30h | ERR_COR | A recoverable condition was detected. Hardware corrects the condition automatically, while software can preserve evidence for analysis. |
| 31h | ERR_NONFATAL | A non-fatal condition was detected. The device can remain active, but software should retain the event for diagnosis. |
| 33h | ERR_FATAL | A fatal condition was detected. Recovery can require reset, isolation, replacement, or a higher-level action. |

Expected / 预期：短列紧凑，长说明列自然扩展。

## 2. Wide Last / 最后一列较宽

<div class="jiandu-table-layout wide-last"></div>

| Element / 要素 | Provider / 提供方 | Description / 描述 |
| --- | --- | --- |
| User Interface | Operating system vendor | Provides user-facing tools that request an action, such as activation, shutdown, or a policy-controlled power-state change. |
| Service Layer | Platform software | Coordinates requests, state reporting, and transitions between application intent and device-specific control logic. |
| Driver | Device vendor | Implements device-specific behavior and reports observable evidence back to higher-level software. |

Expected / 预期：最后一列明显更宽。

## 3. Four Columns / 四列

| <span class="jiandu-col-w-34">State / 状态</span> | <span class="jiandu-col-w-22">Tier A</span> | <span class="jiandu-col-w-22">Tier B</span> | <span class="jiandu-col-w-22">Tier C</span> |
| --- | --- | --- | --- |
| Active | First comparison condition. | Second comparison condition. | Third comparison condition. |
| Recovery Mode | A long row label can wrap without squeezing all parallel comparison columns. | Parallel condition. | Parallel condition. |
| Restricted Mode | Additional context may be recorded when a feature is unavailable. | N/A | N/A |

Expected / 预期：34% / 22% / 22% / 22%。

## 4. Five Columns / 五列

| <span class="jiandu-col-w-28">Item</span> | <span class="jiandu-col-w-18">Basic</span> | <span class="jiandu-col-w-18">Pro</span> | <span class="jiandu-col-w-18">Team</span> | <span class="jiandu-col-w-18">Enterprise</span> |
| --- | --- | --- | --- | --- |
| Data retention | 7 days | 30 days | 180 days | Custom policy and archival controls |
| Support channel | Community | Standard | Priority | Dedicated service arrangement |
| Automation | Limited | Standard | Advanced | Configurable governance and controls |

Expected / 预期：28% / 18% / 18% / 18% / 18%。

## 5. Six Columns / 六列

| <span class="jiandu-col-w-25">Item</span> | <span class="jiandu-col-w-15">A</span> | <span class="jiandu-col-w-15">B</span> | <span class="jiandu-col-w-15">C</span> | <span class="jiandu-col-w-15">D</span> | <span class="jiandu-col-w-15">Notes</span> |
| --- | --- | --- | --- | --- | --- |
| Coverage | Included | Included | Optional | Optional | Regional availability may vary |
| Response time | 48 hours | 24 hours | 8 hours | 4 hours | Service-level terms apply |
| Reporting | Basic | Standard | Advanced | Custom | Export options can be policy-controlled |

Expected / 预期：25% / 15% / 15% / 15% / 15% / 15%。

## 6. Ratio Shortcut / 快捷比例类

<div class="jiandu-table-layout ratio-3-2-2-2"></div>

| State / 状态 | A | B | C |
| --- | --- | --- | --- |
| Active | Visible | Visible | Visible |
| Recovery Mode | Review | Review | Review |
| Restricted Mode | N/A | N/A | N/A |

Expected / 预期：3 : 2 : 2 : 2，即 33.333% / 22.222% / 22.222% / 22.222%。

## 7. High-Density Table / 高密度表格

<div class="jiandu-table-layout dense"></div>

| ID | Region | Service | Current State | Owner | Notes |
| --- | --- | --- | --- | --- | --- |
| A-001 | North | Gateway | Active | Team One | Normal telemetry flow and daily evidence retention. |
| B-014 | East | Storage | Review | Team Two | Capacity validation is currently in progress. |
| C-229 | West | Analytics | Restricted | Team Three | Access depends on a policy approval workflow. |

Expected / 预期：保持自然分列，但字号和单元格留白更紧凑。
