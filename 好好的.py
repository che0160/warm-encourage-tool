import tkinter as tk
import random
import time
import ctypes
import ctypes.wintypes

# 多样化文本内容 - 温暖鼓励主题
messages = [
    # 爱自己系列
    '好好爱自己', '你值得被温柔对待', '要对自己好一点',
    '给自己一个拥抱', '你已经很棒了', '相信自己',
    '你很重要', '做最好的自己', '你是独特的',
    '接纳自己的不完美', '温柔地对待自己', '你值得拥有美好',
    
    # 好好生活系列
    '好好吃饭', '好好睡觉', '好好生活',
    '享受当下', '慢慢来，不着急', '一切都会好起来的',
    '珍惜每一天', '生活会越来越好', '明天会更好',
    '活在当下', '认真生活', '热爱生活',
    
    # 鼓励加油系列
    '你超棒的！', '加油！', '你可以的',
    '继续努力', '坚持下去', '不要放弃',
    '你很优秀', '你已经做得很好了', '为自己骄傲',
    '每一步都算数', '你在进步', '你很勇敢',
    
    # 温馨关怀系列
    '早点休息', '别熬夜', '多喝水哦~',
    '记得吃水果', '天冷多穿衣服', '注意身体',
    '累了就休息', '不要太累', '保重身体',
    '记得按时吃饭', '照顾好自己', '健康最重要',
    
    # 心情治愈系列
    '保持好心情', '保持微笑', '开心一点',
    '放轻松', '不要焦虑', '深呼吸',
    '给自己一些时间', '允许自己不开心', '情绪会过去的',
    '今天也辛苦了', '你做得够好了', '不必苛责自己',
]

# 随机颜色生成
def get_random_color():
    colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow',
              'lavender', 'mistyrose', 'paleturquoise', 'peachpuff']
    return random.choice(colors)

# 获取所有显示器信息的函数
def get_monitors_info():
    monitors = []
    
    def callback(hMonitor, hdcMonitor, lprcMonitor, dwData):
        # lprcMonitor 是一个 RECT 结构，包含显示器的边界
        rect = lprcMonitor.contents
        monitors.append({
            'x': rect.left,
            'y': rect.top,
            'width': rect.right - rect.left,
            'height': rect.bottom - rect.top
        })
        return 1  # 继续枚举
    
    # 定义回调函数类型
    MonitorEnumProc = ctypes.WINFUNCTYPE(
        ctypes.c_int,
        ctypes.c_ulong,
        ctypes.c_ulong,
        ctypes.POINTER(ctypes.wintypes.RECT),
        ctypes.c_double
    )
    
    # 调用 Windows API 枚举所有显示器
    ctypes.windll.user32.EnumDisplayMonitors(None, None, MonitorEnumProc(callback), 0)
    
    return monitors

def create_float_window(root):
    # 创建顶级窗口，指定主窗口为父级
    window = tk.Toplevel(root)

    # 获取所有显示器信息
    monitors = get_monitors_info()
    
    # 找到x坐标最大的显示器（最右边的屏幕）
    if len(monitors) >= 2:
        # 按x坐标排序，取最右边的
        right_monitor = max(monitors, key=lambda m: m['x'])
        screen_x = right_monitor['x']  # 右边屏幕的起始x坐标
        screen_y = right_monitor['y']  # 右边屏幕的起始y坐标
        screen_width = right_monitor['width']
        screen_height = right_monitor['height']
    else:
        # 如果只有一块屏幕，使用主屏幕
        screen_x = 0
        screen_y = 0
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
    
    # 在第二块屏幕范围内随机位置
    window_width = 200
    window_height = 100
    x = random.randrange(screen_x, screen_x + screen_width - window_width)
    y = random.randrange(screen_y, screen_y + screen_height - window_height)
    window.geometry(f"+{x}+{y}")

    message = random.choice(messages)
    color = get_random_color()

    tk.Label(window,
             text=message,
             bg=color,
             font=('楷体', 18),
             width=15,
             height=2).pack()

def create_windows_periodically(root, count=100, delay=50):
    if count > 0:
        create_float_window(root)
        # 递归调用，每隔delay毫秒创建一个新窗口
        root.after(delay, create_windows_periodically, root, count - 1, delay)

if __name__ == "__main__":
    # 创建主窗口（隐藏）
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 开始创建浮动窗口
    create_windows_periodically(root, 200, 70)

    # 启动主事件循环（必须在主线程）
    root.mainloop()