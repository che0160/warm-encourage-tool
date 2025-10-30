# 获取GitHub Personal Access Token 详细指南

## 🔑 什么是Personal Access Token？

GitHub在2021年8月后停止支持密码认证，必须使用Token代替密码进行Git操作。

---

## 📝 获取Token步骤（5分钟）

### 步骤1：登录GitHub并进入设置

1. 访问 https://github.com
2. 使用你的账号登录
   - 用户名：`che0160`
   - 邮箱：`2183321847@qq.com`
   - 密码：你设置的密码

### 步骤2：进入Token设置页面

**方式A：直接访问（推荐）**
- 直接打开：https://github.com/settings/tokens

**方式B：通过菜单**
1. 点击右上角头像
2. 选择 **Settings**（设置）
3. 左侧菜单最底部，点击 **Developer settings**
4. 左侧选择 **Personal access tokens**
5. 选择 **Tokens (classic)**

### 步骤3：生成新Token

1. 点击右上角 **"Generate new token"** 按钮
2. 选择 **"Generate new token (classic)"**

### 步骤4：配置Token

填写以下信息：

| 字段 | 填写内容 |
|------|---------|
| **Note** | `warm-encourage-tool` |
| **Expiration** | 选择 `No expiration`（永不过期）或 `90 days` |
| **Select scopes** | 勾选 ✅ **repo**（完整的仓库访问权限） |

**重要**：只需要勾选 `repo` 这一项即可，它会自动包含所有子选项。

### 步骤5：生成并保存Token

1. 滚动到页面底部
2. 点击绿色的 **"Generate token"** 按钮
3. **立即复制Token！**（只显示一次，刷新后消失）

Token格式类似：`ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

## 💾 保存Token

将Token保存到安全的地方：
- 记事本
- 密码管理器（如1Password、LastPass）
- **不要保存在公开的地方！**

---

## 🚀 使用Token推送代码

### 方法1：运行脚本

1. 双击 `上传到GitHub.bat`
2. 当提示输入用户名和密码时：
   - **Username**: `che0160`
   - **Password**: 粘贴你的Token（不是密码）

### 方法2：手动命令

```powershell
# 重新打开一个新的PowerShell窗口
cd "c:\Users\24019\OneDrive\Desktop\有太多话想说"

git init
git config user.name "che0160"
git config user.email "2183321847@qq.com"
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/che0160/warm-encourage-tool.git
git push -u origin main

# 提示输入用户名和密码时
# Username: che0160
# Password: [粘贴你的Token]
```

---

## ⚠️ 在推送前：确保已创建GitHub仓库

### 创建仓库步骤

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `warm-encourage-tool`
   - **Description**: `温暖鼓励小工具 - Windows和Android版本`
   - 选择 **Public**（公开）
   - **不要勾选** 任何初始化选项
3. 点击 **"Create repository"**

---

## 🔒 Token安全建议

1. ✅ Token等同于密码，妥善保管
2. ✅ 不要上传到GitHub或公开分享
3. ✅ 如果泄露，立即在GitHub删除并重新生成
4. ✅ 为不同项目使用不同的Token
5. ✅ 定期更新Token

---

## 📱 Token过期怎么办？

如果Token设置了过期时间，过期后需要：

1. 重新访问 https://github.com/settings/tokens
2. 删除旧Token
3. 生成新Token
4. 使用新Token进行推送

---

## ❓ 常见问题

### Q: 忘记保存Token了怎么办？
A: Token只显示一次，如果忘记保存，需要删除旧Token并重新生成。

### Q: 可以使用密码吗？
A: 不可以，GitHub已完全禁用密码认证，必须使用Token。

### Q: Token输入错误会怎样？
A: 会提示认证失败，重新运行脚本并输入正确的Token即可。

### Q: 多人协作时Token共享吗？
A: 不建议！每个人应使用自己的Token。

---

## 📞 需要帮助？

如果遇到问题：

1. 检查Token是否正确复制（没有多余空格）
2. 确认Token的 `repo` 权限已勾选
3. 确认GitHub仓库已创建
4. 查看错误提示信息

---

**准备好后，双击运行 `上传到GitHub.bat` 开始上传！** 🚀
