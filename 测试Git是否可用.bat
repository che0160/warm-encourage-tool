@echo off
chcp 65001 >nul
title Git测试工具
color 0B

echo ====================================
echo Git 环境测试
echo ====================================
echo.

echo 测试1: 检查Git命令是否可用...
git --version 2>nul
if errorlevel 1 (
    echo ✗ Git命令不可用（环境变量未生效）
    echo.
    
    echo 测试2: 检查Git安装路径...
    if exist "C:\Program Files\Git\bin\git.exe" (
        echo ✓ 找到Git: C:\Program Files\Git\bin\git.exe
        echo.
        echo 测试3: 使用完整路径执行Git...
        "C:\Program Files\Git\bin\git.exe" --version
        if errorlevel 1 (
            echo ✗ Git执行失败
        ) else (
            echo ✓ Git可以使用（需要完整路径）
            echo.
            echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            echo 结论：Git已安装但环境变量未生效
            echo.
            echo 解决方法：
            echo 1. 重启电脑（推荐）
            echo 2. 或使用 上传到GitHub_v2.bat（自动处理路径）
            echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        )
    ) else if exist "C:\Program Files (x86)\Git\bin\git.exe" (
        echo ✓ 找到Git: C:\Program Files (x86)\Git\bin\git.exe
        echo.
        echo 测试3: 使用完整路径执行Git...
        "C:\Program Files (x86)\Git\bin\git.exe" --version
        if errorlevel 1 (
            echo ✗ Git执行失败
        ) else (
            echo ✓ Git可以使用（需要完整路径）
            echo.
            echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            echo 结论：Git已安装但环境变量未生效
            echo.
            echo 解决方法：
            echo 1. 重启电脑（推荐）
            echo 2. 或使用 上传到GitHub_v2.bat（自动处理路径）
            echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        )
    ) else (
        echo ✗ 未找到Git安装
        echo.
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        echo 结论：Git未正确安装
        echo.
        echo 解决方法：
        echo 1. 访问 https://git-scm.com
        echo 2. 下载并安装Git
        echo 3. 重启电脑
        echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    )
) else (
    echo ✓ Git命令可用
    echo.
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo 结论：Git已正确配置，可以直接使用
    echo.
    echo 你可以运行任何上传脚本了！
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
)

echo.
pause
