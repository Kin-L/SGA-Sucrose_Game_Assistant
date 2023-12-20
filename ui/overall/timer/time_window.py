# -*- coding:gbk -*-
from qfluentwidgets import TimePicker
from ui.element.control import *


class TimerWindow:
    def __init__(self, widget, location):
        super().__init__()
        widget = Widget(widget, location)
        # pic1 = Picture(widget, (0, 0, 1800, 1500), r"D:\Download\test0.png")
        self.time_item = 3
        # ʱ����Ŀ����
        self.label_item = Label(widget, (0, 0, 100, 30), "ʱ����Ŀ����")

        self.add = PicButton(widget, (110, 0, 30, 30),
                             r"assets/main_window/ui/add.png",
                             (20, 20))
        self.deduce = PicButton(widget, (150, 0, 30, 30),
                                r"assets/main_window/ui/reduce.png",
                                (20, 20))
        self.apply = PicButton(widget, (190, 0, 30, 30),
                               r"assets/main_window/ui/save.png",
                               (20, 20))
        # ʱ����Ŀ��ǩ
        self.label_execute = Label(widget, (35, 30, 50, 30), "ִ��")
        self.label_timer = Label(widget, (205, 30, 50, 30), "��ʱ")
        self.label_text = Label(widget, (415, 30, 80, 30), "����ѡ��")
        self.label_awake = Label(widget, (565, 30, 60, 30), "����")
        # ʱ����Ŀ�б�
        self.scroll = ScrollArea(widget, (0, 65, 620, 162))
        self.widget = Widget(None, (0, 0, 620, 120))
        self.scroll.setWidget(self.widget)
        self.widget.setFixedHeight(120)
        # self.scroll_time_item.setFrameShape(QtWidgets.QFrame.Shape(0))
        # ʱ����Ŀ��ť
        self.execute0 = Combobox(self.widget, (5, 5, 90, 30))
        self.execute1 = Combobox(self.widget, (5, 45, 90, 30))
        self.execute2 = Combobox(self.widget, (5, 85, 90, 30))
        self.execute3 = Combobox(self.widget, (5, 125, 90, 30))
        self.execute4 = Combobox(self.widget, (5, 165, 90, 30))
        self.execute5 = Combobox(self.widget, (5, 205, 90, 30))
        self.execute6 = Combobox(self.widget, (5, 245, 90, 30))
        self.execute7 = Combobox(self.widget, (5, 285, 90, 30))
        self.execute8 = Combobox(self.widget, (5, 325, 90, 30))
        self.execute9 = Combobox(self.widget, (5, 365, 90, 30))
        _list = ["����", "ÿ��", "��һ", "�ܶ�", "����", "����", "����", "����", "����"]
        self.execute0.addItems(_list)
        self.execute1.addItems(_list)
        self.execute2.addItems(_list)
        self.execute3.addItems(_list)
        self.execute4.addItems(_list)
        self.execute5.addItems(_list)
        self.execute6.addItems(_list)
        self.execute7.addItems(_list)
        self.execute8.addItems(_list)
        self.execute9.addItems(_list)

        self.timer0 = TimePicker(self.widget)
        self.timer1 = TimePicker(self.widget)
        self.timer2 = TimePicker(self.widget)
        self.timer3 = TimePicker(self.widget)
        self.timer4 = TimePicker(self.widget)
        self.timer5 = TimePicker(self.widget)
        self.timer6 = TimePicker(self.widget)
        self.timer7 = TimePicker(self.widget)
        self.timer8 = TimePicker(self.widget)
        self.timer9 = TimePicker(self.widget)
        self.timer0.setGeometry(QtCore.QRect(100, 5, 50, 30))
        self.timer1.setGeometry(QtCore.QRect(100, 45, 50, 30))
        self.timer2.setGeometry(QtCore.QRect(100, 85, 50, 30))
        self.timer3.setGeometry(QtCore.QRect(100, 125, 50, 30))
        self.timer4.setGeometry(QtCore.QRect(100, 165, 50, 30))
        self.timer5.setGeometry(QtCore.QRect(100, 205, 50, 30))
        self.timer6.setGeometry(QtCore.QRect(100, 245, 50, 30))
        self.timer7.setGeometry(QtCore.QRect(100, 285, 50, 30))
        self.timer8.setGeometry(QtCore.QRect(100, 320, 50, 30))
        self.timer9.setGeometry(QtCore.QRect(100, 360, 50, 30))

        self.text0 = Combobox(self.widget, (345, 5, 210, 30))
        self.text1 = Combobox(self.widget, (345, 45, 210, 30))
        self.text2 = Combobox(self.widget, (345, 85, 210, 30))
        self.text3 = Combobox(self.widget, (345, 125, 210, 30))
        self.text4 = Combobox(self.widget, (345, 165, 210, 30))
        self.text5 = Combobox(self.widget, (345, 205, 210, 30))
        self.text6 = Combobox(self.widget, (345, 245, 210, 30))
        self.text7 = Combobox(self.widget, (345, 285, 210, 30))
        self.text8 = Combobox(self.widget, (345, 325, 210, 30))
        self.text9 = Combobox(self.widget, (345, 365, 210, 30))

        self.awake0 = Check(self.widget, (570, 5, 30, 30), " ")
        self.awake1 = Check(self.widget, (570, 45, 30, 30), " ")
        self.awake2 = Check(self.widget, (570, 85, 30, 30), " ")
        self.awake3 = Check(self.widget, (570, 125, 30, 30), " ")
        self.awake4 = Check(self.widget, (570, 165, 30, 30), " ")
        self.awake5 = Check(self.widget, (570, 205, 30, 30), " ")
        self.awake6 = Check(self.widget, (570, 245, 30, 30), " ")
        self.awake7 = Check(self.widget, (570, 285, 30, 30), " ")
        self.awake8 = Check(self.widget, (570, 325, 30, 30), " ")
        self.awake9 = Check(self.widget, (570, 365, 30, 30), " ")

        self.text0.addItem("<δѡ��>")
        self.text1.addItem("<δѡ��>")
        self.text2.addItem("<δѡ��>")
        self.text3.addItem("<δѡ��>")
        self.text4.addItem("<δѡ��>")
        self.text5.addItem("<δѡ��>")
        self.text6.addItem("<δѡ��>")
        self.text7.addItem("<δѡ��>")
        self.text8.addItem("<δѡ��>")
        self.text9.addItem("<δѡ��>")
