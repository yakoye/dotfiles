#!/usr/bin/env bash

INPUT_FILE="$HOME/.vscode/extensions/extensions.json"

# 输出文件
TXT_OUT="extensions.txt"
JSON_OUT=".vscode/extensions.json"

mkdir -p .vscode

echo "==> 提取扩展 ID..."

# 提取 publisher.name（过滤 UUID）
EXT_LIST=$(grep -A 1 '"identifier"' "$INPUT_FILE" \
  | grep '"id"' \
  | sed -E 's/.*"id": *"([^"]+)".*/\1/' \
  | grep -E '^[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$' \
  | sort -u)

# 生成 extensions.txt
echo "$EXT_LIST" > "$TXT_OUT"
echo "✔ 已生成 $TXT_OUT"

# 生成 extensions.json
echo "{" > "$JSON_OUT"
echo '    "recommendations": [' >> "$JSON_OUT"

echo "$EXT_LIST" | awk '{print "        \""$0"\","}' | sed '$ s/,$//' >> "$JSON_OUT"

echo "    ]" >> "$JSON_OUT"
echo "}" >> "$JSON_OUT"

echo "✔ 已生成 $JSON_OUT"

echo "==> 完成"