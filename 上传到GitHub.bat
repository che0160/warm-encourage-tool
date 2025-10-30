@echo off
chcp 65001 >nul
echo ====================================
echo 正在上传到GitHub...
echo ====================================
echo.

cd /d "%~dp0"

echo [1/6] 初始化Git仓库...
git init
if errorlevel 1 (
    echo 错误：Git初始化失败
    echo 请重启电脑后再试，或手动打开新的PowerShell窗口
    pause
    exit /b 1
)

echo.
echo [2/6] 配置Git用户信息...
git config user.name "che0160"
git config user.email "2183321847@qq.com"

echo.
echo [3/6] 添加文件到Git...
git add .

echo.
echo [4/6] 提交文件...
git commit -m "初始提交：温暖鼓励小工具 Windows和Android版本"

echo.
echo [5/6] 设置主分支...
git branch -M main

echo.
echo [6/6] 添加远程仓库...
git remote add origin https://github.com/che0160/warm-encourage-tool.git

echo.
echo ====================================
echo 准备推送到GitHub...
echo ====================================
echo.
echo 重要提示：
echo 1. 推送时需要输入 Personal Access Token（不是密码）
echo 2. 如果还没有Token，请按照以下步骤获取：
echo.
echo    a. 访问 https://github.com/settings/tokens
echo    b. 点击 "Generate new token (classic)"
echo    c. Note 填写: warm-encourage-tool
echo    d. 勾选 "repo" 权限
echo    e. 点击底部 "Generate token"
echo    f. 复制生成的token（只显示一次！）
echo.
echo 3. 用户名输入: che0160
echo 4. 密码输入: 刚才复制的token
echo.
pause

echo.
echo 开始推送...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ====================================
    echo 推送失败！可能的原因：
    echo ====================================
    echo 1. 还没有创建GitHub仓库
    echo    请访问: https://github.com/new
    echo    仓库名: warm-encourage-tool
    echo    选择: Public
    echo.
    echo 2. Token输入错误或没有权限
    echo    重新获取Token: https://github.com/settings/tokens
    echo.
    echo 3. 仓库已存在内容
    echo    使用: git push -f origin main （强制推送）
    echo ====================================
) else (
    echo.
    echo ====================================
    echo ✓✓✓ 上传成功！✓✓✓
    echo ====================================
    echo.
    echo 下一步：
    echo 1. 访问 https://github.com/che0160/warm-encourage-tool
    echo 2. 点击 "Actions" 标签
    echo 3. 查看 "Build Android APK" 工作流
    echo 4. 等待构建完成（30-60分钟）
    echo 5. 在 "Artifacts" 中下载APK
    echo.
    echo ====================================
)

echo.
pause
