@echo off
chcp 65001 >nul
echo ====================================
echo 温暖鼓励小工具 - Android版本测试
echo ====================================
echo.
echo 提示：此脚本用于在Windows上测试Kivy应用
echo 需要先安装Kivy: pip install kivy
echo.
echo 按任意键开始运行...
pause >nul

python main.py

echo.
echo 程序已关闭
pause
