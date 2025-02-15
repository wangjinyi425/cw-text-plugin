"""
    这是一个示例插件
"""
from PyQt5 import uic
from loguru import logger
from datetime import datetime
from .ClassWidgets.base import PluginBase, SettingsBase, PluginConfig  # 导入CW的基类

from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import ImageLabel, LineEdit

# 自定义小组件
WIDGET_CODE = 'widget_text.ui'
WIDGET_NAME = '自定义组件'
WIDGET_WIDTH = 245

file_w = open(f'{self.PATH}/text.txt','w+')

class Plugin(PluginBase):  # 插件类
    def __init__(self, cw_contexts, method):  # 初始化
        super().__init__(cw_contexts, method)  # 调用父类初始化方法

        self.method.register_widget(WIDGET_CODE, WIDGET_NAME, WIDGET_WIDTH)  # 注册小组件到CW
        self.cfg = PluginConfig(self.PATH, 'config.json')  # 实例化配置类

    def execute(self):  # 自启动执行部分
        # 小组件自定义（照PyQt的方法正常写）
        logger.success('PluginText executed!')
        logger.info(f'Config path: {self.PATH}')

    def update(self, cw_contexts):  # 自动更新部分
        super().update(cw_contexts)  # 调用父类更新方法
        self.cfg.update_config()  # 更新配置

        self.method.change_widget_content(WIDGET_CODE, '文本', file_w.read())


# 设置页
class Settings(SettingsBase):
    def __init__(self, plugin_path, parent=None):
        super().__init__(plugin_path, parent)
        uic.loadUi(f'{self.PATH}/settings.ui', self)  # 加载设置界面

        self.PrimaryPushButton.clicked.connect(self.save)
    def save(self)
        file_w.write(self.TextEdit.text())