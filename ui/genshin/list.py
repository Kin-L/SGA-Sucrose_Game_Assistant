# -*- coding:gbk -*-
from ui.element.control import *


class GenshinList:
    def __init__(self, widget, location):
        # �����б���
        scroll = ScrollArea(widget, location)
        scroll.setFrameShape(QtWidgets.QFrame.Shape(0))
        self.widget = Widget(scroll, (0, 0, 215, 515))
        # ���ÿؼ�
        self.label_genshin = Label(self.widget, (95, 10, 92, 20), "ԭ��", 18)
        setpath = "assets/main_window/ui/set.png"
        self.set_genshin = PicButton(self.widget, (180, 10, 22, 22), setpath, (22, 22))

        self.check_team = Check(self.widget, (15, 50, 140, 22), "�л���׼����")
        self.check_disp = Check(self.widget, (15, 95, 140, 22), "̽����ǲ")
        self.check_trans = Check(self.widget, (15, 140, 140, 22), "ʹ�ò����ʱ���")
        self.check_fly = Check(self.widget, (15, 185, 140, 22), "��׽����")
        self.check_comp = Check(self.widget, (15, 230, 140, 22), "�ϳ�Ũ����֬")
        self.check_pot = Check(self.widget, (15, 275, 140, 22), "��ȡ�����")
        self.check_mail = Check(self.widget, (15, 320, 140, 22), "��ȡ�ʼ�")
        self.check_tree = Check(self.widget, (15, 365, 140, 22), "�ɼ�ľ��")

        self.set_team = PicButton(self.widget, (180, 50, 22, 22), setpath, (22, 22))
        self.set_disp = PicButton(self.widget, (180, 95, 22, 22), setpath, (22, 22))
        self.set_trans = PicButton(self.widget, (180, 140, 22, 22), setpath, (22, 22))
        self.set_fly = PicButton(self.widget, (180, 185, 22, 22), setpath, (22, 22))
        self.set_comp = PicButton(self.widget, (180, 230, 22, 22), setpath, (22, 22))
        self.set_pot = PicButton(self.widget, (180, 275, 22, 22), setpath, (22, 22))
        self.set_mail = PicButton(self.widget, (180, 320, 22, 22), setpath, (22, 22))
        self.set_tree = PicButton(self.widget, (180, 365, 22, 22), setpath, (22, 22))
