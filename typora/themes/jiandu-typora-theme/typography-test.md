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

