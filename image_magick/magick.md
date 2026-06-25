# magick使用说明

## 一、安装imageMagick

### Windows

1. 官网下载：[imagemagick.org](https://link.wtturl.cn/?target=https%3A%2F%2Fimagemagick.org&scene=im&aid=497858&lang=zh) → Download → Windows → 选 **64-bit Q16**
2. 安装时勾选 **Add to PATH**
3. 打开 CMD 输入 `magick -version`，能显示版本就 ok

### macOS（Homebrew）

```
brew install imagemagick
```

### Linux（Ubuntu/Debian）

```
sudo apt install imagemagick
```

------

## 二、核心命令（magick/convert 都可以）

下面示例统一用：**input.png** = 原图，输出自动编号。

### 1）竖向分割（左右切）

#### 对半分（2 列）

```
magick input.png -crop 2x1@ +repage output_%02d.png
```

- 2x1@：2 列、1 行 → 左右两半
- 输出：竖切_00.png（左）、竖切_01.png（右）

#### 竖向切成 N 等份（例：3 列）

```
magick input.png -crop 3x1@ +repage output_%02d.png
```

------

### 2）横向分割（上下切）

#### 对半分（2 行）

```
magick input.png -crop 1x2@ +repage output_%02d.png
```

- 1x2@：1 列、2 行 → 上下两半
- 输出：横切_00.png（上）、横切_01.png（下）

#### 横向切成 N 等份（例：4 行）

```
magick input.png -crop 1x4@ +repage output_%02d.png
```

------

### 3）任意网格（M 列 ×N 行）

```
magick input.png -crop 2x3@ +repage output_%02d.png
```

→ 2 列 3 行，共 6 张

### 4）图像转换，png转webp

直接转

```
magick input.png output.webp
```

调整压缩质量

```
magick input.png -quality 85 output.webp
```

批量转换

```
for file in *.png; do magick "$file" "${file%.png}.webp"; done
```



------

## 三、关键参数说明

- `-crop WxH@`：按**份数**分割（不是像素），`@` 表示等分
- `+repage`：清除多余画布信息，避免打开时偏移
- `%02d`：输出文件名用 **00、01、02…** 排序（`%03d` 是 001、002）

------

## 四、Windows 注意（CMD 里直接用）

把 `magick` 换成 `convert` 也行：

```
convert input.png -crop 2x1@ +repage output_%02d.png
```