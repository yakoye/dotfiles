# Git 一键提交推送
gitp() {
    set -e
    # 自动获取当前所在分支，不用手动改 main/master
    local BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

    # 判断当前是不是 git 仓库
    if [ -z "$BRANCH" ]; then
        echo "❌ 当前目录不是 Git 仓库！"
        return 1
    fi

    echo "===== Git 自定义提交推送 ====="
    # 读取提交信息，空着就用时间默认信息
    local COMMIT_MSG
    read -p "请输入提交信息(直接回车用默认): " COMMIT_MSG
    if [ -z "$COMMIT_MSG" ]; then
        COMMIT_MSG="自动提交: $(date +'%Y-%m-%d %H:%M:%S')"
    fi

    echo "🔄 拉取远程最新代码..."
    git pull origin "$BRANCH"

    echo "📦 添加所有变更文件..."
    git add .

    echo "✍️  提交: $COMMIT_MSG"
    git commit -m "$COMMIT_MSG"

    echo "🚀 推送到远程 $BRANCH 分支..."
    git push origin "$BRANCH"

    echo -e "\n🎉 推送成功！"
}