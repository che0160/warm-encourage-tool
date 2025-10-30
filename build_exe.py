"""
自动打包脚本 - 将好好的_单屏版.py打包成exe文件
使用PyInstaller进行打包
"""
import os
import subprocess
import sys

def build_exe():
    """执行打包命令"""
    
    # 检查PyInstaller是否安装
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
    except ImportError:
        print("✗ PyInstaller 未安装")
        print("正在安装 PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # 设置打包参数
    script_name = "好好的_单屏版.py"
    output_name = "温暖鼓励小工具"
    
    # PyInstaller打包命令
    # --onefile: 打包成单个exe文件
    # --windowed: 不显示控制台窗口（适合GUI程序）
    # --name: 指定生成的exe文件名
    # --clean: 清理临时文件
    # --noconfirm: 覆盖输出目录时不询问
    
    cmd = [
        "pyinstaller",
        "--onefile",           # 单文件模式
        "--windowed",          # 无控制台窗口
        f"--name={output_name}",  # 输出文件名
        "--clean",             # 清理缓存
        "--noconfirm",         # 不询问确认
        script_name
    ]
    
    print(f"\n开始打包 {script_name}...")
    print(f"命令: {' '.join(cmd)}\n")
    
    # 执行打包
    result = subprocess.run(cmd, capture_output=False)
    
    if result.returncode == 0:
        print("\n✓ 打包成功！")
        print(f"生成的exe文件位于: dist\\{output_name}.exe")
        print("\n提示：")
        print("  - spec文件和build文件夹可以删除")
        print("  - dist文件夹中的exe文件即为最终程序")
    else:
        print("\n✗ 打包失败，请检查错误信息")
        return False
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("温暖鼓励小工具 - 打包脚本")
    print("=" * 50)
    
    # 检查源文件是否存在
    if not os.path.exists("好好的_单屏版.py"):
        print("✗ 错误：找不到 好好的_单屏版.py 文件")
        print("请确保在正确的目录下运行此脚本")
        sys.exit(1)
    
    # 执行打包
    success = build_exe()
    
    if success:
        print("\n打包完成！按任意键退出...")
        input()
    else:
        print("\n打包失败！按任意键退出...")
        input()
        sys.exit(1)
