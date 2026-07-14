# Jiandu Punctuation Test / 简读中英文标点测试

This file verifies that Chinese full-width punctuation and English ASCII punctuation remain visually distinct in headings, body text, lists, quotes, tables, and PDF output.

本文用于检查中文全角标点与英文 ASCII 半角标点在标题、正文、列表、引用、表格和 PDF 导出中是否保持清晰区分。

> Important / 重要：  
> A theme can preserve the glyphs you typed, but it cannot convert an ASCII comma `,` into a Chinese comma `，`.  
> 主题可以正确保留你输入的字符，但不能把英文逗号 `,` 自动转换成中文逗号 `，`。

## 1. Chinese Punctuation / 中文标点

中文逗号，中文句号。中文分号；中文冒号：中文问号？中文感叹号！

顿号、连接号—破折号——省略号……间隔号·波浪号～。

双引号“中文双引号”，单引号‘中文单引号’。

书名号《简读主题》，单书名号〈章节标题〉。

圆括号（中文括号），方头括号【重点】，六角括号〔补充〕。

全角方括号［内容］，全角花括号｛内容｝。

## 2. English Punctuation / 英文标点

English comma, English period. English semicolon; English colon: question mark? exclamation mark!

Hyphen-minus -, en dash – and em dash —. Ellipsis ...

Double quotes "English quotes" and single quotes 'English quotes'.

Parentheses (content), brackets [content], braces {content}, angle brackets <content>.

## 3. Side-by-side Comparison / 并排对比

| Type / 类型 | Characters / 字符 | Sentence / 句子 |
| --- | --- | --- |
| Chinese / 中文 | `，。；：？！` | 知道名称或定义，只是认识了标签，不等于真正理解这个东西。 |
| English / 英文 | `, . ; : ? !` | Knowing a name or definition is not the same as understanding the subject. |
| Chinese quotes / 中文引号 | `“”‘’` | 解释不仅要说“是什么”，还要说“为什么”和“怎么发生”。 |
| English quotes / 英文引号 | `" "' '` | Explain not only "what", but also "why" and "how". |
| Chinese brackets / 中文括号 | `（）【】《》` | 这是（补充说明）与【重点内容】以及《文章标题》。 |
| English brackets / 英文括号 | `() [] <>` | This is (additional text), [important text], and <a label>. |

## 4. Mixed Chinese and English / 中英文混排

PCIe 6.0：链路速率为 64 GT/s；状态为 L0，设备工作正常。

The PCIe 6.0 link is active: speed is 64 GT/s; state is L0, and the device is operating normally.

中文说明中包含 `Link Control 2`、`AER` 和 `LTSSM`，中文逗号仍应显示为全角字符。

In English prose, commas, periods, colons: and semicolons; should remain ASCII punctuation.

## 5. List / 列表

- 中文逗号，后面应保留中文全角标点的视觉空间。
- 中文句号。句号应保持圆点位于中文标点字面框内。
- 中文分号；中文冒号：中文问号？中文感叹号！
- English comma, period. semicolon; colon: question? exclamation!
- 中英文混排：English phrase, 中文说明；下一项继续。

## 6. Quote / 引用

> “知道名称”不等于“真正理解”；复述、解释、举例和迁移属于不同层次。

> "Knowing the name" is not the same as "understanding the subject"; explanation and transfer are different abilities.

## 7. Heading Punctuation / 标题标点

### 中文标题：理解、复述与表达

### English Heading: Understanding, Retelling, and Expression

## Expected Result / 预期结果

- Chinese `，。；：？！` must remain full-width CJK punctuation.  
  中文 `，。；：？！` 应保持全角中日韩标点字形。
- English `, . ; : ? !` must remain ASCII punctuation.  
  英文 `, . ; : ? !` 应保持半角 ASCII 标点。
- The theme must not enable proportional CJK punctuation alternates.  
  主题不得启用中日韩标点的比例宽度替代字形。
- Screen and PDF output should use the same punctuation behavior.  
  屏幕显示和 PDF 导出应保持同一套标点行为。
