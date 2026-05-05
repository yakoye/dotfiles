#!/bin/bash
set -e

BRANCH="main"

clear
echo "===== Git 自定义提交推送 ====="
read -p "请输入提交信息: " COMMIT_MSG

git pull origin $BRANCH
git add .
git commit -m "$COMMIT_MSG"
git push origin $BRANCH

echo "🎉 推送成功！"