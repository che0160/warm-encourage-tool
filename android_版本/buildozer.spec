[app]

# 应用名称（显示在手机上的名字）
title = 温暖鼓励小工具

# 包名（Android应用唯一标识）
package.name = warmencourage

# 包的域名（通常使用反向域名）
package.domain = org.example

# 源代码目录
source.dir = .

# 源代码包含的文件
source.include_exts = py,png,jpg,kv,atlas

# 应用版本
version = 1.0

# 应用依赖的Python包
requirements = python3,kivy

# 支持的Android架构（arm64-v8a是现代手机常用架构）
android.archs = arm64-v8a,armeabi-v7a

# Android权限（根据需要添加）
# android.permissions = INTERNET

# 应用图标（如果有的话）
# icon.filename = %(source.dir)s/icon.png

# 启动画面（如果有的话）
# presplash.filename = %(source.dir)s/presplash.png

# Android API版本
android.api = 31
android.minapi = 21

# NDK版本
android.ndk = 25b

# 是否自动接受SDK许可
android.accept_sdk_license = True

# 应用方向（landscape横屏, portrait竖屏, all全部）
orientation = all

# 全屏模式
fullscreen = 0

# Android启动模式
android.entrypoint = org.kivy.android.PythonActivity

# Android应用主题
# android.apptheme = "@android:style/Theme.NoTitleBar"

[buildozer]

# 日志级别（0=错误, 1=信息, 2=调试）
log_level = 2

# 警告级别
warn_on_root = 1

# 构建目录
build_dir = ./.buildozer

# 二进制文件目录
bin_dir = ./bin
