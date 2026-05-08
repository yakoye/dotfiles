#!/bin/bash
set -e  # 遇到错误自动停止

# ===================== 配置区 ======================
COMMIT_MSG="自动提交: $(date +'%Y-%m-%d %H:%M:%S')"
BRANCH="main"  # 你的分支：main / master
# ===================================================

clear
echo "=========================================="
echo "          Git 自动推送脚本 (增强版)"
echo "=========================================="

# 检查是否为Git仓库
if [ ! -d .git ]; then
    echo "❌ 错误：当前目录不是Git仓库！"
    exit 1
fi

echo "1/4 拉取远程最新代码..."
git pull origin $BRANCH --no-rebase

echo -e "\n2/4 添加所有修改文件..."
git add .

echo -e "\n3/4 提交代码..."
git commit -m "$COMMIT_MSG"

echo -e "\n4/4 推送到远程仓库..."
git push origin $BRANCH

echo -e "\n🎉 全部完成！"