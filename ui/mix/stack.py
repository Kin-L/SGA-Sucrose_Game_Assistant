# -*- coding:gbk -*-
from ui.element.ui_part import Independent
from ui.element.control import *


class MixStack:
    def __init__(self, widget, location):
        # ���ܶѵ�����
        self.stack = Stack(widget, location)
        # ���ܶѵ�����
        self.widget_set = Widget(self.stack, (0, 0, 395, 515))
        self.label_local = Label(self.widget_set, (0, 12, 220, 18), "����ҳ�棺�������� ���з�ʽ")
        self.line0 = Line(self.widget_set, (0, 41, 395, 3))
        self.independent = Independent(self.widget_set, (0, 50, 350, 70), False)
