# HELP



### extension安装方法

#### Linux / macOS

```bash
cat extensions.txt | xargs -n 1 code --install-extension
```

#### Windows PowerShell

```bat
Get-Content extensions.txt | ForEach-Object { code --install-extension $_ }
```

#### 生成extensions方法

```
gen_vscode_ext.sh
```



### VS Code漂亮 MonoKai Pro 主题许可证

1、打开VS Code的命令面板，Windows快捷键 ctrl+shift+p；MAC快捷键Command⌘+shift+p

2、输入`Monokai Pro: enter license`，enter！

3、输入email 地址为`id@chinapyg.com`，enter！

4、输入lincese key `d055c-36b72-151ce-350f4-a8f69`，enter！

5、大功告成
