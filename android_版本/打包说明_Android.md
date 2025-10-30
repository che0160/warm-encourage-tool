# 温暖鼓励小工具 - Android APK打包说明

## ⚠️ 重要前提条件

**Buildozer打包工具只支持Linux和macOS系统！**

Windows用户有以下选择：
1. **使用WSL2（推荐）** - Windows Subsystem for Linux
2. **使用虚拟机** - 安装Ubuntu等Linux系统
3. **使用云服务器** - 租用Linux服务器进行打包
4. **使用在线打包服务** - 如GitHub Actions

本教程以**Ubuntu Linux**为例。

---

## 📋 环境准备

### 1. 系统要求

- **操作系统**：Ubuntu 20.04/22.04 或其他Linux发行版
- **Python版本**：3.8-3.11
- **磁盘空间**：至少10GB可用空间
- **内存**：建议4GB以上

### 2. 安装系统依赖

```bash
# 更新包管理器
sudo apt update
sudo apt upgrade -y

# 安装必要的系统依赖
sudo apt install -y \
    python3-pip \
    build-essential \
    git \
    zip \
    unzip \
    openjdk-11-jdk \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev

# 安装Android构建工具依赖
sudo apt install -y \
    ccache \
    libltdl-dev \
    libffi-dev \
    libssl-dev \
    python3-setuptools
```

### 3. 安装Python依赖

```bash
# 安装Cython和Buildozer
pip3 install --upgrade pip
pip3 install cython==0.29.36
pip3 install buildozer==1.5.0
pip3 install kivy==2.3.0

# 或者使用requirements.txt
pip3 install -r requirements.txt
```

---

## 🔧 配置Android SDK

Buildozer会自动下载Android SDK和NDK，但你也可以手动配置：

### 自动配置（推荐）

Buildozer首次运行时会自动下载所需工具，无需手动配置。

### 手动配置（可选）

如果自动下载失败，可以手动设置环境变量：

```bash
# 编辑 ~/.bashrc 或 ~/.zshrc
export ANDROID_SDK_ROOT=$HOME/.buildozer/android/platform/android-sdk
export ANDROID_NDK_ROOT=$HOME/.buildozer/android/platform/android-ndk-r25b
export PATH=$PATH:$ANDROID_SDK_ROOT/tools:$ANDROID_SDK_ROOT/platform-tools
```

---

## 📦 打包步骤

### 1. 初始化项目（如果是首次打包）

```bash
cd android_版本
buildozer init
```

这会生成`buildozer.spec`配置文件（我们已经提供了）。

### 2. 执行打包

```bash
# 清理之前的构建（可选）
buildozer android clean

# 打包APK（debug版本）
buildozer -v android debug

# 首次打包会下载SDK、NDK等工具，需要较长时间（30分钟-2小时）
# 后续打包会快很多（5-10分钟）
```

### 3. 查找生成的APK

打包成功后，APK文件位于：
```
android_版本/bin/温暖鼓励小工具-1.0-arm64-v8a-debug.apk
```

---

## 📱 安装到手机

### 方法1：USB连接

```bash
# 确保手机开启USB调试模式
# 使用adb安装
adb install bin/温暖鼓励小工具-1.0-arm64-v8a-debug.apk
```

### 方法2：文件传输

1. 将APK文件传输到手机（通过数据线、云盘、微信等）
2. 在手机上打开APK文件
3. 允许安装来自未知来源的应用
4. 完成安装

---

## 🎯 打包发布版本（上架应用商店）

### 生成签名密钥

```bash
# 生成密钥库
keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias \
    -keyalg RSA -keysize 2048 -validity 10000
```

### 配置buildozer.spec

在`buildozer.spec`中添加：

```ini
[app]
# 发布版本配置
android.release_artifact = apk

# 签名配置
[buildozer]
android.sign.enabled = true
android.sign.keystore = /path/to/my-release-key.keystore
android.sign.keystore_password = your_password
android.sign.key_alias = my-key-alias
android.sign.key_password = your_password
```

### 打包发布版

```bash
buildozer android release
```

---

## 🐛 常见问题与解决方案

### 问题1：Buildozer下载SDK失败

**解决方案：使用国内镜像**

编辑`~/.buildozer/android/platform/android-sdk/tools/android`，修改下载源。

或手动下载SDK并放置到指定目录：
```bash
mkdir -p ~/.buildozer/android/platform/
# 手动下载并解压SDK到上述目录
```

### 问题2：编译时出现"No space left on device"

**解决方案：清理磁盘空间**

```bash
# 清理buildozer缓存
buildozer android clean
rm -rf .buildozer

# 清理系统缓存
sudo apt clean
sudo apt autoremove
```

### 问题3：APK安装后闪退

**解决方案：检查日志**

```bash
# 连接手机后查看日志
adb logcat | grep python
```

常见原因：
- Python版本不兼容
- 缺少依赖库
- 权限配置错误

### 问题4：打包时间过长

**原因：首次打包需要下载大量工具**

- Android SDK：约1GB
- Android NDK：约1GB
- Python编译工具链：约500MB

**解决方案：耐心等待，或使用更快的网络**

### 问题5：在Windows上打包

**解决方案：使用WSL2**

```powershell
# 在Windows PowerShell中安装WSL2
wsl --install -d Ubuntu

# 进入WSL2
wsl

# 在WSL2中按照Linux步骤操作
```

---

## 🚀 使用GitHub Actions自动打包（推荐）

对于Windows用户，可以使用GitHub Actions在云端自动打包。

### 创建 .github/workflows/build.yml

```yaml
name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        pip install buildozer cython==0.29.36
        sudo apt update
        sudo apt install -y openjdk-11-jdk
    
    - name: Build APK
      working-directory: ./android_版本
      run: buildozer -v android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: android-apk
        path: android_版本/bin/*.apk
```

### 使用步骤

1. 将代码推送到GitHub
2. GitHub Actions自动触发构建
3. 在Actions页面下载生成的APK

---

## 📊 性能优化建议

### 1. 减少标签数量

在`main.py`中调整：
```python
self.max_labels = 20  # 根据手机性能调整（10-50）
```

### 2. 调整创建速度

```python
Clock.schedule_interval(self.create_floating_label, 0.2)  # 增加间隔时间
```

### 3. 添加清理机制

自动清理超过一定数量的标签，防止内存溢出。

---

## 📝 版本更新流程

1. 修改`main.py`代码
2. 更新`buildozer.spec`中的版本号
3. 重新打包：`buildozer android debug`
4. 测试新版本APK
5. 发布到应用商店或分发给用户

---

## 🔐 上架应用商店

### Google Play商店

1. 注册Google Play开发者账号（$25一次性费用）
2. 创建应用
3. 上传发布版APK
4. 填写应用信息和截图
5. 提交审核

### 国内应用商店

- 华为应用市场
- 小米应用商店
- OPPO软件商店
- vivo应用商店
- 应用宝（腾讯）

每个商店都需要单独注册和提交。

---

## 💡 提示

1. **首次打包耗时长**：首次打包需要下载约3GB的工具和依赖，建议使用良好的网络环境
2. **使用虚拟环境**：建议在Python虚拟环境中进行开发，避免依赖冲突
3. **保存签名密钥**：发布版的签名密钥非常重要，丢失后无法更新应用
4. **测试充分**：在不同Android版本和设备上充分测试
5. **版本管理**：使用Git管理代码，便于版本回退和协作

---

## 📞 技术支持

如遇到问题：
1. 查看Buildozer官方文档：https://buildozer.readthedocs.io/
2. 查看Kivy官方文档：https://kivy.org/doc/stable/
3. 搜索GitHub Issues
4. 在Stack Overflow提问

---

*祝你打包顺利！🎉*
