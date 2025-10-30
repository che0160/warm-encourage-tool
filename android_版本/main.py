"""
温暖鼓励小工具 - Android版本
使用Kivy框架开发，支持Android平台
"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import random

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

# 随机颜色生成（使用RGB格式，Kivy使用0-1范围）
def get_random_color():
    colors = [
        (1, 0.75, 0.8),      # pink
        (0.68, 0.85, 0.9),   # lightblue
        (0.56, 0.93, 0.56),  # lightgreen
        (1, 1, 0.88),        # lightyellow
        (0.9, 0.9, 0.98),    # lavender
        (1, 0.89, 0.88),     # mistyrose
        (0.69, 0.88, 0.9),   # paleturquoise
        (1, 0.85, 0.73),     # peachpuff
    ]
    color = random.choice(colors)
    return color + (1,)  # 添加alpha通道

class FloatingLabel(Label):
    """可点击关闭的浮动标签"""
    
    def __init__(self, **kwargs):
        super(FloatingLabel, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 100)
        
    def on_touch_down(self, touch):
        """点击标签时移除自己"""
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
            return True
        return super(FloatingLabel, self).on_touch_down(touch)

class WarmEncourageApp(App):
    """主应用程序类"""
    
    def __init__(self, **kwargs):
        super(WarmEncourageApp, self).__init__(**kwargs)
        self.float_layout = None
        self.label_count = 0
        self.max_labels = 30  # Android设备建议30个标签（避免卡顿）
        
    def build(self):
        """构建应用界面"""
        self.title = '温暖鼓励小工具'
        self.float_layout = FloatLayout()
        
        # 设置背景颜色（白色）
        with self.float_layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=Window.size, pos=self.float_layout.pos)
        
        # 绑定窗口大小变化事件
        Window.bind(size=self._update_rect)
        
        # 开始创建浮动标签（延迟0.1秒后开始）
        Clock.schedule_once(self.start_creating_labels, 0.1)
        
        return self.float_layout
    
    def _update_rect(self, instance, value):
        """更新背景矩形大小"""
        self.rect.size = instance.size
    
    def start_creating_labels(self, dt):
        """开始定时创建标签"""
        Clock.schedule_interval(self.create_floating_label, 0.15)  # 每0.15秒创建一个
    
    def create_floating_label(self, dt):
        """创建一个浮动标签"""
        if self.label_count >= self.max_labels:
            # 达到最大数量，停止创建
            return False  # 返回False停止定时器
        
        # 获取屏幕尺寸
        screen_width, screen_height = Window.size
        
        # 标签尺寸
        label_width = 200
        label_height = 100
        
        # 随机位置（确保标签完全在屏幕内）
        x = random.uniform(0, max(0, screen_width - label_width))
        y = random.uniform(0, max(0, screen_height - label_height))
        
        # 随机消息和颜色
        message = random.choice(messages)
        color = get_random_color()
        
        # 创建浮动标签
        label = FloatingLabel(
            text=message,
            pos=(x, y),
            font_size='20sp',
            halign='center',
            valign='middle',
        )
        
        # 设置背景颜色
        with label.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*color)
            label.bg_rect = Rectangle(pos=label.pos, size=label.size)
        
        # 绑定位置和大小变化
        label.bind(pos=self._update_label_bg, size=self._update_label_bg)
        
        # 添加到布局
        self.float_layout.add_widget(label)
        self.label_count += 1
    
    def _update_label_bg(self, instance, value):
        """更新标签背景"""
        if hasattr(instance, 'bg_rect'):
            instance.bg_rect.pos = instance.pos
            instance.bg_rect.size = instance.size

if __name__ == '__main__':
    WarmEncourageApp().run()
