# ========================= Alias 别名定义 =========================
# 说明：
# 所有自定义命令别名（alias）建议统一放在此文件中，便于管理。
#
# 重要：
# 此文件要生效，必须确保 ~/.bashrc 中已经启用以下配置（取消注释）：
#
# if [ -f ~/.bash_aliases ]; then
#     . ~/.bash_aliases
# fi
# ==================================================================
# 如果不是交互式 shell，直接退出，不执行后续内容
case $- in
    *i*) ;;
      *) return;;
esac

# 历史记录中不保存重复行，也不保存以空格开头的命令
# 更多选项参见 bash(1)
HISTCONTROL=ignoreboth

# 追加方式写入历史文件，而非覆盖
shopt -s histappend

# 历史记录条数设置：HISTSIZE 内存条数，HISTFILESIZE 文件最大条数
HISTSIZE=1000
HISTFILESIZE=2000

# 每条命令执行后检查窗口大小，必要时更新 LINES 和 COLUMNS
shopt -s checkwinsize

# 若启用，** 可匹配任意文件、0 个或多层目录
#shopt -s globstar

# 让 less 支持非文本文件（如二进制、压缩包），参见 lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# 设置 chroot 环境标识（用于提示符）
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# 判断终端是否支持彩色提示符
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# 如果终端是 xterm，强制设为 xterm-256color 支持完整色彩
if [ "$TERM" == "xterm" ]; then
    export TERM=xterm-256color
fi

# 取消注释可强制开启彩色提示符
#force_color_prompt=yes

# 如果开启强制彩色，检测终端是否支持 ANSI 颜色
if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# 支持颜色（遵循 ANSI/ECMA-48 标准）
	color_prompt=yes
    else
	color_prompt=
    fi
fi

# 根据是否支持颜色设置不同提示符
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# xterm / rxvt 终端：设置标题栏 + 自定义带日期、时间、历史编号、彩色提示符
case "$TERM" in
xterm*|rxvt*)
    #PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    PS1="\[\033[01;33m\][\D{%y-%m-%d} \t]\[\033[00m\]\[\033[01;32m\][\!]\[\033[00m\]${debian_chroot:+($debian_chroot)}\[\033[01;37m\]\u@\h\[\033[00m\]: \[\033[01;34m\]\w \[\033[00m\]\n \[\033[05;35m\]\$ \[\033[00m\]"
    ;;
*)
    ;;
esac

# 启用 ls 彩色显示，设置常用别名
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# GCC 错误/警告彩色输出（可取消注释启用）
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# --- 基础导航与查看 ---
alias ll='ls -lh'
alias la='ls -alt'
alias l='ls -CF'
alias lt='ls -latF'
alias lh='ls -lhF'
alias duall='du -h --max-depth=1'

# --- 灵活路径处理 (使用 $HOME 代替 /home/test) ---
# 这样无论在哪个用户下，只要脚本路径一致就能跑通
alias bc="$HOME/vimrc_x/scripts/bcompare_run.sh &"
alias backupfile="$HOME/code/backupfile.sh"

# --- 常用工具 ---
alias vscode='/snap/bin/code'
alias s='screen'
# alias mp="screen $HOME/tools/os/p95v298b6/mprime &"
alias eclipse="$HOME/tools/os/eclipse/eclipse &"
alias bcompare='/bin/rm -rf $HOME/.config/bcompare/registry.dat; /usr/bin/bcompare'

alias pwgen='pwgen -s'
alias fd='fdfind' # Debian/树莓派系统下 fd 的包名通常是 fdfind

# --- 开发与 Tags (针对芯片/嵌入式源码) ---
alias astyle='astyle -A1 -s4 -S -N -j -m0 -M40 -c -U -H -p -n -q'
alias tgc='echo "tag cleaned"; rm -f cscope.* tags'

# 重新定义 tgg，增加灵活性
alias tgg='echo "tag generate ..."; ctags -R *; find /usr/include $(pwd) -name "*.[ch]" -o -name "*.cpp" > cscope.files; cscope -bkq -i cscope.files; echo "Finish."'

# --- 编译与配置 ---
alias mk='make clean; make'
alias vb="vim $HOME/.bashrc"
alias sb="source $HOME/.bashrc && echo 'Bash config reloaded'"
alias python='python3'

# --- 系统维护 (修正了原有的 update 错误) ---
alias install='sudo apt-get install'
alias update='sudo apt-get update && sudo apt-get upgrade' # 原来你写的是 install update，那是错的

# --- 帮助与记录 ---
alias hh='cat -n $HOME/help; cp $HOME/help $HOME/help.bk'

# --- 函数类 Alias (修复参数传递问题) ---
# 注意：Alias 不支持 $1 参数传递，必须使用函数 (function)

# 依然保留一个“真删除”命令rmrm替代rm，以防万一需要彻底清理磁盘
alias rmrm='/bin/rm -iv'

# 安全删除函数：替代原始 rm
rm() {
    local trash_base="/tmp/trash"
    local date_str=$(date +%y%m%d_%H%M%S)
    local trash_dir="$trash_base/$date_str"

    # 1. 如果没有参数，模拟原始 rm 的提示
    if [ $# -eq 0 ]; then
        command rm
        return
    fi

    # 2. 检查是否有忽略回收站的参数 (比如使用 -f 强删，或者你想保留原始 rm 功能)
    # 如果你输入 rmrm，可以直接用你之前定义的那个别名
    
    # 3. 创建回收站根目录（如果不存在）
    if [ ! -d "$trash_base" ]; then
        mkdir -p "$trash_base"
        chmod 1777 "$trash_base"
    fi

    # 4. 执行移动操作
    # 使用 -- 确保处理以 - 开头的文件名
    # 将所有参数移动到带时间戳的目录中
    mkdir -p "$trash_dir"
    
    # 打印操作信息
    echo -e "\e[33m[Trash]\e[0m Moving $* to $trash_dir"
    
    # 执行移动
    mv -- "$@" "$trash_dir"
    
    if [ $? -eq 0 ]; then
        echo -e "\e[32m[Success]\e[0m Delete Finish."
    else
        echo -e "\e[31m[Error]\e[0m Move failed!"
    fi
}


# --- 灵活的 Vim 启动函数 (处理 file:line 格式) ---
v() {
    local args=()
    # 循环处理所有输入参数
    for arg in "$@"; do
        # 检查参数中是否包含冒号且冒号后是数字 (如 path/to/file:123)
        if [[ "$arg" =~ ^(.+):([0-9]+)$ ]]; then
            # 提取文件名和行号，转化为 Vim 识别的格式
            args+=("${BASH_REMATCH[1]}" "+${BASH_REMATCH[2]}")
        else
            args+=("$arg")
        fi
    done

    # 启动 vim。如果没有任何参数，则直接打开 vim
    if [ ${#args[@]} -eq 0 ]; then
        command vim
    else
        command vim "${args[@]}"
    fi
}

# --- 灵活的 Gvim 启动函数 ---
g() {
    local args=()
    for arg in "$@"; do
        if [[ "$arg" =~ ^(.+):([0-9]+)$ ]]; then
            args+=("${BASH_REMATCH[1]}" "+${BASH_REMATCH[2]}")
        else
            args+=("$arg")
        fi
    done

    # 启动 gvim，末尾加 & 进入后台运行
    if [ ${#args[@]} -eq 0 ]; then
        gvim &
    else
        gvim "${args[@]}" &
    fi
}

grep-c() {
    grep -rn --include="*.[ch]" --include="*.hpp" --include="*.cpp" --include="*.cxx" --include="*.cc" --include="Makefile*" "$1" .
}

grep-p() {
    grep -rn --include="*.py" "$1" .
}

grep-g() {
    grep -rn --include="*.peg" "$1" .
}

find-c() {
    find . -name "*.h" -o -name "*.c"
}
