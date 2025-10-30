@echo off
chcp 65001 >nul
title GitHub上传工具
color 0A

echo ====================================
echo 正在上传到GitHub...
echo ====================================
echo.

cd /d "%~dp0"

REM 检测Git路径
set "GIT_CMD=git"
where git >nul 2>&1
if errorlevel 1 (
    echo Git命令未找到，尝试使用完整路径...
    if exist "C:\Program Files\Git\bin\git.exe" (
        set "GIT_CMD=C:\Program Files\Git\bin\git.exe"
        echo ✓ 找到Git: %GIT_CMD%
    ) else if exist "C:\Program Files (x86)\Git\bin\git.exe" (
        set "GIT_CMD=C:\Program Files (x86)\Git\bin\git.exe"
        echo ✓ 找到Git: %GIT_CMD%
    ) else (
        echo.
        echo ====================================
        echo ✗ 错误：找不到Git！
        echo ====================================
        echo.
        echo 解决方法：
        echo 1. 重启电脑（让Git环境变量生效）
        echo 2. 或者手动添加Git到环境变量
        echo 3. 或者重新安装Git
        echo.
        echo Git下载地址：https://git-scm.com
        echo.
        pause
        exit /b 1
    )
) else (
    echo ✓ Git已准备就绪
)

echo.
echo ====================================
echo 开始Git操作...
echo ====================================
echo.

echo [1/7] 初始化Git仓库...
"%GIT_CMD%" init
if errorlevel 1 (
    echo ✗ 失败：Git初始化失败
    echo.
    pause
    exit /b 1
)
echo ✓ 完成

echo.
echo [2/7] 配置Git用户信息...
"%GIT_CMD%" config user.name "che0160"
"%GIT_CMD%" config user.email "2183321847@qq.com"
echo ✓ 完成

echo.
echo [3/7] 添加文件到Git...
"%GIT_CMD%" add .
if errorlevel 1 (
    echo ✗ 警告：部分文件添加失败（可忽略）
)
echo ✓ 完成

echo.
echo [4/7] 提交文件...
"%GIT_CMD%" commit -m "初始提交：温暖鼓励小工具 Windows和Android版本"
if errorlevel 1 (
    echo ✗ 失败：提交失败
    echo 可能的原因：Git仓库已存在
    echo 继续执行...
)
echo ✓ 完成

echo.
echo [5/7] 设置主分支...
"%GIT_CMD%" branch -M main
echo ✓ 完成

echo.
echo [6/7] 添加远程仓库...
"%GIT_CMD%" remote remove origin >nul 2>&1
"%GIT_CMD%" remote add origin https://github.com/che0160/warm-encourage-tool.git
if errorlevel 1 (
    echo ✗ 警告：可能远程仓库已存在
)
echo ✓ 完成

echo.
echo ====================================
echo [7/7] 准备推送到GitHub...
echo ====================================
echo.
echo ⚠️ 重要提示：
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
echo 1. 推送时需要输入 Personal Access Token
echo    （不是你的GitHub密码！）
echo.
echo 2. 如果还没有Token，请：
echo    a. 打开：https://github.com/settings/tokens
echo    b. 点击 "Generate new token (classic)"
echo    c. Note填写: warm-encourage-tool
echo    d. 勾选 "repo" 权限
echo    e. 点击 "Generate token"
echo    f. 复制生成的token
echo.
echo 3. 推送时输入：
echo    Username: che0160
echo    Password: [粘贴你的token]
echo.
echo 4. 确保已创建GitHub仓库：
echo    https://github.com/new
echo    名称: warm-encourage-tool
echo    类型: Public
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.
pause

echo.
echo 开始推送...
echo.
"%GIT_CMD%" push -u origin main

if errorlevel 1 (
    echo.
    echo ====================================
    echo ✗ 推送失败！
    echo ====================================
    echo.
    echo 可能的原因和解决方法：
    echo.
    echo 1. 仓库未创建
    echo    → 访问 https://github.com/new
    echo    → 创建名为 warm-encourage-tool 的仓库
    echo.
    echo 2. Token错误或未输入
    echo    → 重新获取：https://github.com/settings/tokens
    echo    → 确保勾选了 repo 权限
    echo.
    echo 3. 仓库已有内容
    echo    → 使用强制推送：
    echo    → git push -f origin main
    echo.
    echo 4. 网络连接问题
    echo    → 检查网络
    echo    → 稍后重试
    echo.
    echo ====================================
    echo.
    echo 是否要强制推送？（覆盖远程内容）
    set /p force="输入 yes 强制推送，其他键跳过: "
    if /i "%force%"=="yes" (
        echo.
        echo 执行强制推送...
        "%GIT_CMD%" push -f origin main
        if errorlevel 1 (
            echo ✗ 强制推送也失败了
        ) else (
            echo ✓ 强制推送成功！
            goto success
        )
    )
) else (
    :success
    echo.
    echo ====================================
    echo ✓✓✓ 上传成功！✓✓✓
    echo ====================================
    echo.
    echo 🎉 代码已成功推送到GitHub！
    echo.
    echo 📱 下一步 - 获取Android APK：
    echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    echo.
    echo 1. 访问你的仓库：
    echo    https://github.com/che0160/warm-encourage-tool
    echo.
    echo 2. 点击顶部 "Actions" 标签
    echo.
    echo 3. 查看 "Build Android APK" 工作流
    echo    （正在自动构建中...）
    echo.
    echo 4. 等待构建完成（约30-60分钟）
    echo    ⏰ 可以先做其他事情，稍后回来查看
    echo.
    echo 5. 构建完成后（显示绿色✓）：
    echo    → 点击工作流名称
    echo    → 向下滚动到 "Artifacts"
    echo    → 点击 "android-apk" 下载
    echo    → 解压zip得到APK文件
    echo.
    echo 📖 详细说明：查看 GitHub_上传指南.md
    echo.
    echo ====================================
)

echo.
echo 按任意键关闭窗口...
pause >nul
