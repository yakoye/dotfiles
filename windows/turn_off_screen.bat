@echo off
chcp 65001 >nul
setlocal

title 关闭屏幕
color 0F
mode con: cols=72 lines=20

set "PS1_FILE=%TEMP%\turn_off_screen_%RANDOM%%RANDOM%.ps1"

for /L %%S in (3,-1,1) do (
    call :show_countdown %%S
    timeout /t 1 /nobreak >nul
)

> "%PS1_FILE%" echo Add-Type -TypeDefinition @'
>> "%PS1_FILE%" echo using System;
>> "%PS1_FILE%" echo using System.Runtime.InteropServices;
>> "%PS1_FILE%" echo.
>> "%PS1_FILE%" echo public class Monitor {
>> "%PS1_FILE%" echo     [DllImport("user32.dll", SetLastError=true)]
>> "%PS1_FILE%" echo     public static extern IntPtr SendMessageTimeout(
>> "%PS1_FILE%" echo         IntPtr hWnd,
>> "%PS1_FILE%" echo         uint Msg,
>> "%PS1_FILE%" echo         IntPtr wParam,
>> "%PS1_FILE%" echo         IntPtr lParam,
>> "%PS1_FILE%" echo         uint fuFlags,
>> "%PS1_FILE%" echo         uint uTimeout,
>> "%PS1_FILE%" echo         out IntPtr lpdwResult
>> "%PS1_FILE%" echo     );
>> "%PS1_FILE%" echo }
>> "%PS1_FILE%" echo '@
>> "%PS1_FILE%" echo.
>> "%PS1_FILE%" echo Start-Sleep -Milliseconds 300
>> "%PS1_FILE%" echo $result = [IntPtr]::Zero
>> "%PS1_FILE%" echo [Monitor]::SendMessageTimeout([intptr]0xffff, 0x0112, [intptr]0xF170, [intptr]2, 0x0002, 1000, [ref]$result) ^| Out-Null
>> "%PS1_FILE%" echo exit 0

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%PS1_FILE%"

set "ERR=%ERRORLEVEL%"
del "%PS1_FILE%" >nul 2>nul

exit /b %ERR%


:show_countdown
cls
echo.
echo.
echo.
echo.
echo.
echo.
echo                          +------------------------------------------------------------+
echo                                                %1 秒后关闭屏幕
echo.
echo                                                 电脑不会关机
echo.
echo                                            下载、编译、脚本会继续运行
echo.
echo                                             请不要移动鼠标或按键盘
echo.
echo                                                 倒计时：%1 秒
echo                          +------------------------------------------------------------+
exit /b