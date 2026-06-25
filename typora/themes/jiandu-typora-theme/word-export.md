# Word Export / Word 导出

## Package test document / 本主题测试文档

`print-test.md` uses PNG image assets. It should not invoke `rsvg-convert` when exported to DOCX.

`print-test.md` 使用 PNG 图片资源，导出 DOCX 时不应调用 `rsvg-convert`。

## Why the warning appeared / 为什么会出现警告

The previous test document used three SVG files. Word/DOCX export often rasterizes SVG images first. Your message shows that the conversion program `rsvg-convert` is not installed or not available in `PATH`.

此前测试文档引用了三张 SVG。Word/DOCX 导出通常需要先将 SVG 栅格化；你看到的提示说明 `rsvg-convert` 未安装或不在 `PATH` 中。

## For your own SVG files / 对你自己的 SVG 文件

Option A — install the converter on Windows:

```powershell
choco install rsvg-convert
```

Option B — convert SVG to PNG before Word export. PNG avoids this external dependency and is the safer default for Word compatibility.

方案 A：在 Windows 安装转换器。

方案 B：导出 Word 前将 SVG 转为 PNG。PNG 不依赖外部转换程序，对 Word 兼容性更稳。
