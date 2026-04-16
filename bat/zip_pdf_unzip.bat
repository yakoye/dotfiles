@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:menu
cls
echo.
echo ===================== 功能菜单 =====================
echo 1 - [精准版] 手动输入前缀，将分卷压缩包改为 .pdf 后缀
echo 2 - [精准版] 手动输入前缀，还原分卷压缩包 (去除 .pdf)
echo 3 - 退出脚本
echo ====================================================
echo.
set /p choice=请输入功能序号（1/2/3）：

if "%choice%"=="1" goto to_pdf
if "%choice%"=="2" goto to_zip
if "%choice%"=="3" exit
goto menu

:to_pdf
echo.
echo ==============================================
echo 你的文件类似：CHROME.z01、CHROME.zip
echo 那么前缀就是：CHROME
echo ==============================================
set /p "prefix=请输入你要转换的文件名前缀: "

if "!prefix!"=="" (
    echo 错误：前缀不能为空！
    pause
    goto menu
)

set "file_count=0"
echo.

REM 精准查找以该前缀开头的 .z** 和 .zip 文件
for /f "delims=" %%f in ('dir /b "!prefix!*.z??" "!prefix!*.zip" 2^>nul') do (
    set "filename=%%~nf"
    set "ext=%%~xf"
    
    REM 剥离原扩展名的点，直接和文件名拼接并加上 .pdf
    REM 例如 CHROME.z01 -> CHROMEz01.pdf
    set "clean_ext=!ext:.=!"
    ren "%%f" "!filename!!clean_ext!.pdf"
    
    echo 已转换：%%f -^> !filename!!clean_ext!.pdf
    set /a file_count+=1
)

echo.
if !file_count! equ 0 (
    echo 未找到以 [!prefix!] 开头的分卷压缩包文件，请检查拼写！
) else (
    echo 转换完成，共处理 !file_count! 个文件。
)
pause
goto menu

:to_zip
echo.
echo ==============================================
echo 你的文件类似：CHROMEz01.pdf
echo 那么前缀就是：CHROME
echo ==============================================
set /p "prefix=请输入你要还原的文件名前缀: "

if "!prefix!"=="" (
    echo 错误：前缀不能为空！
    pause
    goto menu
)

set "file_count=0"
set "main_zip="

echo.
REM 查找所有包含该前缀的 pdf 文件
for /f "delims=" %%f in ('dir /b "!prefix!*.pdf" 2^>nul') do (
    set "fullname=%%~nf"
    
    REM 核心逻辑：直接把前缀抠掉，剩下的字就是原后缀
    set "real_ext=!fullname:%prefix%=!"
    
    if not "!real_ext!"=="" (
        set "origin_name=!prefix!.!real_ext!"
        ren "%%f" "!origin_name!"
        echo 成功还原：%%f -^> !origin_name!
        set /a file_count+=1
        
        REM 记录主程序 zip，方便自动打开
        if /i "!real_ext!"=="zip" set "main_zip=!origin_name!"
    )
)

echo.
if !file_count! equ 0 (
    echo 未找到以 [!prefix!] 开头的 .pdf 文件，请检查大小写或拼写是否完全一致！
) else (
    echo 还原完成，共恢复 !file_count! 个文件！
    if defined main_zip (
        echo 正在打开主压缩包...
        start "" "!main_zip!"
    )
)
pause
goto menu