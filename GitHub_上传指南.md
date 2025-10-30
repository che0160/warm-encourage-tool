# GitHub Actions 自动打包APK指南

## 📋 前置准备

### 1. 注册GitHub账号
如果还没有GitHub账号，请访问 https://github.com 注册（免费）

### 2. 安装Git（如果未安装）
下载地址：https://git-scm.com/download/win

安装后重启PowerShell或CMD。

---

## 🚀 上传步骤

### 步骤1：在GitHub创建新仓库

1. 登录GitHub
2. 点击右上角的 **"+"** → **"New repository"**
3. 填写信息：
   - **Repository name**: `温暖鼓励小工具` 或 `warm-encourage-tool`
   - **Description**: 可选，如"一个温暖的鼓励小工具"
   - **Public** 或 **Private**: 选择Public（公开仓库免费使用GitHub Actions）
   - **不要勾选** "Initialize this repository with a README"
4. 点击 **"Create repository"**

### 步骤2：在本地初始化Git仓库

打开PowerShell，执行以下命令：

```powershell
# 进入项目目录
cd "c:\Users\24019\OneDrive\Desktop\有太多话想说"

# 初始化Git仓库
git init

# 配置用户信息（替换成你的信息）
git config user.name "你的GitHub用户名"
git config user.email "你的GitHub邮箱"

# 添加所有文件
git add .

# 提交
git commit -m "初始提交：Windows和Android版本"

# 设置主分支名为main
git branch -M main

# 关联远程仓库（替换成你的仓库地址）
git remote add origin https://github.com/你的用户名/温暖鼓励小工具.git

# 推送到GitHub
git push -u origin main
```

**注意事项：**
- 替换 `你的GitHub用户名` 为实际用户名
- 替换 `你的GitHub邮箱` 为注册GitHub的邮箱
- 替换仓库地址为你刚才创建的仓库地址

### 步骤3：查看自动构建

1. 推送成功后，打开你的GitHub仓库页面
2. 点击顶部的 **"Actions"** 标签
3. 你会看到一个正在运行的工作流 **"Build Android APK"**
4. 点击进入查看详细进度

**构建时间：** 首次构建约30-60分钟（需要下载Android SDK等工具）

### 步骤4：下载生成的APK

构建完成后：

1. 在Actions页面，点击已完成的工作流
2. 向下滚动到 **"Artifacts"** 部分
3. 点击 **"android-apk"** 下载APK文件
4. 解压下载的zip文件，即可得到APK

---

## 🔄 后续更新

如果你修改了代码，想重新打包：

```powershell
# 进入项目目录
cd "c:\Users\24019\OneDrive\Desktop\有太多话想说"

# 查看修改的文件
git status

# 添加修改的文件
git add .

# 提交修改
git commit -m "描述你的修改内容"

# 推送到GitHub
git push
```

推送后，GitHub Actions会自动触发构建，无需手动操作。

---

## 🎯 手动触发构建

如果想在没有代码修改的情况下重新构建：

1. 打开GitHub仓库页面
2. 点击 **"Actions"** 标签
3. 选择左侧的 **"Build Android APK"** 工作流
4. 点击右侧的 **"Run workflow"** 按钮
5. 选择分支（main）
6. 点击绿色的 **"Run workflow"** 按钮

---

## ❓ 常见问题

### Q1: 推送时提示需要认证？
**A:** GitHub已停止使用密码认证，需要使用Personal Access Token：

1. GitHub右上角头像 → **Settings**
2. 左侧最底部 **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token** → **Generate new token (classic)**
5. 勾选 `repo` 权限
6. 生成后复制token（只显示一次，请保存好）
7. 推送时用token代替密码

### Q2: Actions构建失败？
**A:** 检查以下几点：

1. 仓库是否为Public（私有仓库有使用时长限制）
2. 查看失败的步骤日志，了解具体错误
3. 常见问题：网络问题导致下载SDK失败，重新运行即可

### Q3: 如何使APK文件更小？
**A:** 在 `buildozer.spec` 中修改：

```ini
# 只打包arm64架构（大部分新手机）
android.archs = arm64-v8a
```

### Q4: 能否自动发布Release？
**A:** 可以！创建Git tag并推送：

```powershell
git tag v1.0
git push origin v1.0
```

GitHub Actions会自动创建Release并附上APK。

---

## 🔐 安全提示

1. **不要上传敏感信息**：API密钥、密码等
2. **使用.gitignore**：已为你配置好，避免上传临时文件
3. **Token保管**：Personal Access Token要妥善保管，不要泄露

---

## 📱 安装APK到手机

下载APK后：

1. 将APK传输到手机（数据线、云盘、微信等）
2. 在手机上打开APK文件
3. 允许安装未知来源应用
4. 完成安装

---

## 💡 优化建议

### 加速构建

在 `.github/workflows/build-android.yml` 中添加缓存：

```yaml
- name: 缓存Buildozer目录
  uses: actions/cache@v3
  with:
    path: .buildozer
    key: ${{ runner.os }}-buildozer-${{ hashFiles('**/buildozer.spec') }}
```

### 自动发布到Release

已在工作流中配置，只需推送tag即可：

```powershell
git tag v1.0.0 -m "第一个正式版本"
git push origin v1.0.0
```

---

**祝你上传顺利！🎉**

如有问题，欢迎随时询问。
