# 温暖鼓励小工具 - Android版本

## 📱 项目简介

这是"温暖鼓励小工具"的Android移动版本，使用Kivy框架开发，可以在Android手机和平板上运行。

## ✨ 功能特性

- 📝 **60+温暖语句**：包含爱自己、好好生活、鼓励加油等5大类别
- 🎨 **8种柔和配色**：随机背景颜色
- 📍 **随机位置显示**：每次位置不同
- 👆 **触摸关闭**：点击标签即可关闭
- 🔄 **自动生成**：自动逐个显示鼓励语句
- 📱 **适配屏幕**：自动适配不同尺寸设备

## 🆚 与Windows版本的区别

| 特性 | Windows版本 | Android版本 |
|------|------------|-------------|
| GUI框架 | tkinter | Kivy |
| 窗口数量 | 200个 | 30个 |
| 关闭方式 | 点击X按钮 | 触摸标签 |
| 创建速度 | 70ms/个 | 150ms/个 |

## 📦 文件说明

```
android_版本/
├── main.py                    # Kivy主程序
├── buildozer.spec             # Android打包配置
├── requirements.txt           # 依赖列表
├── 打包说明_Android.md        # 打包教程
└── README_Android.md          # 本文档
```

## 🚀 快速开始

### 安装APK
1. 下载APK文件
2. 在Android设备上安装
3. 允许安装来自未知来源的应用

### 自己打包
详见 [`打包说明_Android.md`](./打包说明_Android.md)

```bash
# Linux环境
pip install buildozer
buildozer android debug
```

## 🎨 自定义配置

### 修改标签数量
```python
self.max_labels = 30  # 在main.py中修改
```

### 修改创建速度
```python
Clock.schedule_interval(self.create_floating_label, 0.15)
```

## 📱 系统要求

- **最低版本**：Android 5.0 (API 21)
- **推荐版本**：Android 8.0+
- **内存**：至少1GB RAM
- **存储**：20MB可用空间

## 🔧 技术栈

- Python 3.8+
- Kivy 2.3.0
- Buildozer 1.5.0
- Android (arm64-v8a, armeabi-v7a)

## 🔄 更新日志

### v1.0 (2025-10-30)
- ✨ 初始版本发布
- ✨ 60+温暖鼓励语句
- ✨ 触摸关闭功能
- ✨ 自适应屏幕

## 🐛 常见问题

**Q: 安装提示"未知来源"？**
A: 在设置中允许安装未知来源应用

**Q: 如何在Windows上打包？**
A: 需要使用WSL2或虚拟机，详见打包说明

**Q: 如何修改语句内容？**
A: 编辑main.py中的messages列表
