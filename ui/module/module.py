# -*- coding:gbk -*-
from qfluentwidgets import EditableComboBox
from ui.element.control import *


# ģ�����ô���
class ModuleWindow:
    def __init__(self, main):
        # ģ�����ô���
        self.widget_module = Widget(None, (5, 0, 670, 570))
        main.stack_setting.addWidget(self.widget_module)
        # ģ�鰴ť
        self.scroll_list = ScrollArea(self.widget_module, (0, 0, 215, 65))
        self.widget_icon = Widget(self.scroll_list, (0, 0, 270, 50))
        self.widget_icon.setMinimumSize(270, 50)
        self.scroll_list.setWidget(self.widget_icon)
        self.scroll_list.setFrameShape(QtWidgets.QFrame.Shape(0))
        # �����л��б�
        self.box_config_change = EditableComboBox(self.widget_module)
        self.box_config_change.setGeometry(QtCore.QRect(265, 9, 210, 30))
        # ��ʼ��ͣ��ť
        self.button_config_delete = PicButton(self.widget_module, (225, 8, 35, 35),
                                              r"assets\main_window\ui\delete.png", (25, 25))
        self.button_config_unlock = TransPicButton(self.widget_module, (480, 8, 35, 35),
                                                   r"assets\main_window\ui\unlock.png", (25, 25))
        self.button_config_unlock.hide()
        self.button_config_lock = TransPicButton(self.widget_module, (480, 8, 35, 35),
                                                 r"assets\main_window\ui\lock.png", (25, 25))
        self.button_config_save = PicButton(self.widget_module, (520, 8, 35, 35),
                                            r"assets\main_window\ui\save.png", (25, 25))
        self.button_pause = Button(self.widget_module, (560, 8, 60, 35), "ֹͣ")
        self.button_pause.hide()
        self.button_start = Button(self.widget_module, (560, 8, 60, 35), "��ʼ")
        # �ѵ�����
        self.stack_module = Stack(self.widget_module, (0, 65, 670, 515))


