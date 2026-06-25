@echo off
chcp 65001 >nul
setlocal

set "TARGET=%~dp0turn_off_screen.bat"

if not exist "%TARGET%" (
    echo 没有找到 turn_off_screen.bat
    echo.
    echo 请把 install_context_menu.bat 和 turn_off_screen.bat 放在同一个目录。
    echo.
    pause
    exit /b 1
)

echo 正在添加右键菜单：关闭屏幕
echo.
echo 目标脚本：
echo %TARGET%
echo.

set "KEY1=HKCU\Software\Classes\Directory\Background\shell\TurnOffScreen"
set "KEY2=HKCU\Software\Classes\DesktopBackground\Shell\TurnOffScreen"

rem 先删除旧配置，避免 Position=Top 残留
reg delete "%KEY1%" /f >nul 2>nul
reg delete "%KEY2%" /f >nul 2>nul

rem 文件夹空白处右键
reg add "%KEY1%" /ve /d "📴关闭屏幕" /f >nul
reg add "%KEY1%" /v "Icon" /d "powercpl.dll,1" /f >nul
reg add "%KEY1%\command" /ve /d "cmd.exe /c ""%TARGET%""" /f >nul

rem 桌面空白处右键
reg add "%KEY2%" /ve /d "📴关闭屏幕" /f >nul
reg add "%KEY2%" /v "Icon" /d "powercpl.dll,1" /f >nul
reg add "%KEY2%\command" /ve /d "cmd.exe /c ""%TARGET%""" /f >nul

echo 添加完成。
echo.
echo 已取消 Position=Top。
echo 现在“关闭屏幕”不会强制显示在最上面。
echo.
echo 如果没有立即生效，可以重启资源管理器，或者注销后重新登录。
echo.
pause