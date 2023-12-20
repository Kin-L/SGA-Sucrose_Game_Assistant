# -*- coding:gbk -*-
from qfluentwidgets import CompactSpinBox
from ui.element.ui_part import Independent
from ui.element.control import *


class Local:
    def __init__(self, stack):
        # ��ʼ������
        self.page_local = Widget(stack)
        stack.addWidget(self.page_local)
        # ��ӿؼ�
        self.label_local = Label(self.page_local, (0, 12, 180, 18), "����ҳ�棺ԭ�� ���з�ʽ")
        self.line_local0 = Line(self.page_local, (0, 42, 395, 3))

        self.label_overall = Label(self.page_local, (0, 50, 180, 27), "ȫ�����ã�")
        self.label_start = Label(self.page_local, (0, 90, 80, 27), "������")
        self.combo_server = Combobox(self.page_local, (80, 90, 100, 32))
        self.combo_server.addItems(["�ٷ�", "B��"])
        self.label_start = Label(self.page_local, (0, 130, 80, 27), "����·��")
        self.line_start = Lineedit(self.page_local, (0, 160, 385, 33))
        self.line_local1 = Line(self.page_local, (0, 202, 395, 3))

        self.label_single = Label(self.page_local, (0, 210, 220, 27), "�����������ã�")
        self.independent = Independent(self.page_local, (0, 250, 350, 70))


class Team:
    def __init__(self, stack):
        # ��ʼ������
        self.page_team = Widget(stack)
        stack.addWidget(self.page_team)
        # ��ӿؼ�
        self.label_team = Label(self.page_team, (0, 12, 180, 18), "����ҳ�棺�л���׼����")
        self.label_team_tip = Label(self.page_team, (90, 80, 220, 27), "�л���׼���� ����������Ŀ��")


dispatch_dir = {
    "�ɵ�": ["ˮ����,������(1)", "ˮ����,������(2)", "Ħ��", "����,����", "�ݵ�,����", "���ܲ�,���ܲ�"],
    "����": ["ˮ����,������", "Ħ��1", "Ħ��2", "��β,�����", "���ܲ�,���ܲ�", "����,����"],
    "����": ["Ħ��1", "Ħ��2", "����,�ݵ�", "����,����", "���ܲ�,����", "����,�����"],
    "����": ["Ħ��", "Ǿޱ,ƻ��", "����,Ģ��", "�ݵ�,�����", "������,���ܲ�", "�ն���,�ɹ�"],
    "�㵤": ["Ħ��", "ϫ��,Ģ��", "�Խ��,�ݵ�", "������,����", "���ݽ�,����", "����,����"]}


class Disp:
    def __init__(self, stack):
        # ��ʼ������
        self.page_dispatch = Widget(stack)
        stack.addWidget(self.page_dispatch)
        # ��ӿؼ�
        self.label_dispatch = Label(self.page_dispatch, (0, 12, 180, 18), "����ҳ�棺̽����ǲ")

        self.label_area = Label(self.page_dispatch, (20, 45, 180, 27), "����ѡ��")
        self.label_mat = Label(self.page_dispatch, (180, 45, 180, 27), "����ѡ��")

        self.area0 = Combobox(self.page_dispatch, (0, 80, 100, 32))
        self.area1 = Combobox(self.page_dispatch, (0, 120, 100, 32))
        self.area2 = Combobox(self.page_dispatch, (0, 160, 100, 32))
        self.area3 = Combobox(self.page_dispatch, (0, 200, 100, 32))
        self.area4 = Combobox(self.page_dispatch, (0, 240, 100, 32))

        self.mat0 = Combobox(self.page_dispatch, (140, 80, 180, 32))
        self.mat1 = Combobox(self.page_dispatch, (140, 120, 180, 32))
        self.mat2 = Combobox(self.page_dispatch, (140, 160, 180, 32))
        self.mat3 = Combobox(self.page_dispatch, (140, 200, 180, 32))
        self.mat4 = Combobox(self.page_dispatch, (140, 240, 180, 32))

        self.area0.addItems(["�ɵ�", "����", "����", "����", "�㵤"])
        self.area1.addItems(["�ɵ�", "����", "����", "����", "�㵤"])
        self.area2.addItems(["�ɵ�", "����", "����", "����", "�㵤"])
        self.area3.addItems(["�ɵ�", "����", "����", "����", "�㵤"])
        self.area4.addItems(["�ɵ�", "����", "����", "����", "�㵤"])

        self.mat0.addItems(dispatch_dir["�ɵ�"])
        self.mat1.addItems(dispatch_dir["�ɵ�"])
        self.mat2.addItems(dispatch_dir["�ɵ�"])
        self.mat3.addItems(dispatch_dir["�ɵ�"])
        self.mat4.addItems(dispatch_dir["�ɵ�"])

        self.area0.currentIndexChanged.connect(lambda: self.list_change(self.area0, self.mat0))
        self.area1.currentIndexChanged.connect(lambda: self.list_change(self.area1, self.mat1))
        self.area2.currentIndexChanged.connect(lambda: self.list_change(self.area2, self.mat2))
        self.area3.currentIndexChanged.connect(lambda: self.list_change(self.area3, self.mat3))
        self.area4.currentIndexChanged.connect(lambda: self.list_change(self.area4, self.mat4))
        self.area0.setCurrentIndex(0)
        self.area1.setCurrentIndex(0)
        self.area2.setCurrentIndex(0)
        self.area3.setCurrentIndex(0)
        self.area4.setCurrentIndex(0)
        self.mat0.setCurrentIndex(0)
        self.mat1.setCurrentIndex(0)
        self.mat2.setCurrentIndex(0)
        self.mat3.setCurrentIndex(0)
        self.mat4.setCurrentIndex(0)

        self.redisp = Check(self.page_dispatch, (0, 285, 100, 25), "�ٴ���ǲ")

    @staticmethod
    def list_change(fa, fm):
        fm.clear()
        fm.addItems(dispatch_dir[fa.currentText()])


class Trans:
    def __init__(self, stack):
        # ��ʼ������
        self.page_trans = Widget(stack)
        stack.addWidget(self.page_trans)
        # ��ӿؼ�
        self.label_trans = Label(self.page_trans, (0, 12, 200, 18), "����ҳ�棺ʹ�ò����ʱ���")
        self.LineEdit0 = Lineedit(self.page_trans, (0, 50, 385, 33))
        self.LineEdit1 = Lineedit(self.page_trans, (0, 100, 385, 33))
        self.LineEdit2 = Lineedit(self.page_trans, (0, 150, 385, 33))
        self.LineEdit3 = Lineedit(self.page_trans, (0, 200, 385, 33))
        self.LineEdit4 = Lineedit(self.page_trans, (0, 250, 385, 33))


class Fly:
    def __init__(self, stack):
        # ��ʼ������
        self.page_fly = Widget(stack)
        stack.addWidget(self.page_fly)
        # ��ӿؼ�
        self.label_fly = Label(self.page_fly, (0, 12, 180, 18), "����ҳ�棺��׽����")
        self.fly0 = Check(self.page_fly, (0, 45, 140, 50), "���ֻ��ǹ���\nɳĮ����֮���·�")
        self.fly1 = Check(self.page_fly, (0, 110, 140, 22), "ɳĮ������Ϸ�")
        self.fly2 = Check(self.page_fly, (0, 165, 140, 22), "ɳĮ�����ݿ��·�")
        self.fly3 = Check(self.page_fly, (0, 220, 140, 22), "���Ҿ�Ԩ������������")
        self.fly4 = Check(self.page_fly, (0, 275, 140, 22), "����ƽ����")


class Concentrate:
    def __init__(self, stack):
        # ��ʼ������
        self.page_concentrate = Widget(stack)
        stack.addWidget(self.page_concentrate)
        # ��ӿؼ�
        self.label_concentrate = Label(self.page_concentrate, (0, 12, 180, 18), "����ҳ�棺�ϳ�Ũ����֬")
        self.label_concentrate_tip = Label(self.page_concentrate, (90, 80, 220, 27), "�ϳ�Ũ����֬ ����������Ŀ��")


class Pot:
    def __init__(self, stack):
        # ��ʼ������
        self.page_pot = Widget(stack)
        stack.addWidget(self.page_pot)
        # ��ӿؼ�
        self.label_pot = Label(self.page_pot, (0, 12, 180, 18), "����ҳ�棺��ȡ�����")
        self.label_pot_tip = Label(self.page_pot, (90, 80, 220, 27), "��ȡ����� ����������Ŀ��")


class Mail:
    def __init__(self, stack):
        # ��ʼ������
        self.page_mail = Widget(stack)
        stack.addWidget(self.page_mail)
        # ��ӿؼ�
        self.label_mail = Label(self.page_mail, (0, 12, 180, 18), "����ҳ�棺��ȡ�ʼ�")
        self.label_mail_tip = Label(self.page_mail, (90, 80, 220, 27), "��ȡ�ʼ� ����������Ŀ��")


class Tree:
    def __init__(self, stack):
        # ��ʼ������
        self.page_tree = Widget(stack)
        stack.addWidget(self.page_tree)
        # ��ӿؼ�
        self.label_tree = Label(self.page_tree, (0, 12, 180, 18), "����ҳ�棺�ɼ�ľ��")
        self.CompactSpinBox = CompactSpinBox(self.page_tree)
        self.CompactSpinBox.setGeometry(QtCore.QRect(0, 40, 120, 30))

        self.tree0 = Check(self.page_tree, (0, 90, 120, 22), "��ľ")
        self.tree1 = Check(self.page_tree, (130, 90, 120, 22), "�ͻ�ľ")
        self.tree2 = Check(self.page_tree, (260, 90, 120, 22), "��ľ")
        self.tree3 = Check(self.page_tree, (0, 135, 120, 22), "ȴɰľ")
        self.tree4 = Check(self.page_tree, (130, 135, 120, 22), "���")
        self.tree5 = Check(self.page_tree, (260, 135, 120, 22), "����ľ")
        self.tree6 = Check(self.page_tree, (0, 180, 120, 22), "ɼľ")
        self.tree7 = Check(self.page_tree, (130, 180, 120, 22), "�μ�ľ")
        self.tree8 = Check(self.page_tree, (260, 180, 120, 22), "��ľ")
        self.tree9 = Check(self.page_tree, (0, 216, 120, 40), "��ȸľ\n��٤ľ")
        self.tree10 = Check(self.page_tree, (130, 225, 120, 22), "��٤ľ")
        self.tree11 = Check(self.page_tree, (260, 216, 120, 40), "ҵ��ľ\n��ľ")
        self.tree12 = Check(self.page_tree, (0, 270, 120, 22), "֤��ľ")
        self.tree13 = Check(self.page_tree, (130, 270, 120, 22), "�̿�ľ")
        self.tree14 = Check(self.page_tree, (260, 270, 120, 22), "����ľ")
        self.tree15 = Check(self.page_tree, (0, 315, 120, 22), "�ľ")
        self.tree16 = Check(self.page_tree, (130, 315, 120, 22), "���ľ")
        self.tree17 = Check(self.page_tree, (260, 315, 120, 22), "���ľ")
        self.tree18 = Check(self.page_tree, (0, 360, 120, 22), "��ľ")


class GenshinStack(Local, Team, Disp, Trans, Fly, Concentrate, Pot, Mail, Tree):
    def __init__(self, widget, location):
        # ���ܶѵ�����
        self.stack = Stack(widget, location)
        Local.__init__(self, self.stack)
        Team.__init__(self, self.stack)
        Disp.__init__(self, self.stack)
        Trans.__init__(self, self.stack)
        Fly.__init__(self, self.stack)
        Concentrate.__init__(self, self.stack)
        Pot.__init__(self, self.stack)
        Mail.__init__(self, self.stack)
        Tree.__init__(self, self.stack)
        