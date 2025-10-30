@echo off
chcp 65001 >nul
echo ====================================
echo GitHub 快速上传脚本
echo ====================================
echo.
echo 使用前请确保：
echo 1. 已安装Git（https://git-scm.com）
echo 2. 已创建GitHub仓库
echo 3. 已配置Git用户信息
echo.
echo ====================================
echo.

set /p username="请输入GitHub用户名: "
set /p reponame="请输入仓库名（如: warm-encourage-tool）: "
set /p email="请输入GitHub邮箱: "

echo.
echo 开始执行Git操作...
echo.

REM 初始化Git
git init
if errorlevel 1 (
    echo 错误: Git未安装或初始化失败
    pause
    exit /b 1
)

REM 配置用户信息
git config user.name "%username%"
git config user.email "%email%"

REM 添加文件
echo 添加文件到Git...
git add .

REM 提交
echo 提交文件...
git commit -m "初始提交：Windows和Android版本"

REM 设置主分支
git branch -M main

REM 添加远程仓库
echo 关联远程仓库...
git remote add origin https://github.com/%username%/%reponame%.git

REM 推送
echo 推送到GitHub...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ====================================
    echo 推送失败！可能的原因：
    echo 1. 需要输入Personal Access Token（不是密码）
    echo 2. 仓库地址不正确
    echo 3. 网络连接问题
    echo.
    echo 如何获取Token：
    echo GitHub → Settings → Developer settings
    echo → Personal access tokens → Generate new token
    echo ====================================
) else (
    echo.
    echo ====================================
    echo ✓ 上传成功！
    echo.
    echo 下一步：
    echo 1. 访问 https://github.com/%username%/%reponame%
    echo 2. 点击 Actions 标签
    echo 3. 等待APK构建完成（约30-60分钟）
    echo 4. 在 Artifacts 中下载APK
    echo ====================================
)

echo.
pause
