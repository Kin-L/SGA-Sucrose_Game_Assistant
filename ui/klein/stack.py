# -*- coding:gbk -*-
from qfluentwidgets import DoubleSpinBox
from ui.element.ui_part import Independent
from ui.element.control import *


class Local:
    def __init__(self, stack):
        # ��ʼ������
        self.page_local = Widget(stack)
        stack.addWidget(self.page_local)
        # ��ӿؼ�
        self.label_local = Label(self.page_local, (0, 12, 180, 18), "����ҳ�棺�������� ���з�ʽ")
        Line(self.page_local, (0, 42, 395, 3))

        self.label_klein_overall = Label(self.page_local, (0, 50, 180, 27), "ȫ�����ã�")
        self.label_start = Label(self.page_local, (0, 90, 80, 27), "������")  # ����·�� /
        self.combo_server = Combobox(self.page_local, (80, 90, 100, 32))
        self.combo_server.addItems(["�ٷ�", "B��"])
        self.label_start = Label(self.page_local, (0, 130, 80, 27), "����·��")
        self.line_start = Lineedit(self.page_local, (0, 160, 385, 33))
        Line(self.page_local, (0, 202, 395, 3))

        self.label_team_tip = Label(self.page_local, (0, 210, 220, 27), "�����������ã�")
        self.independent = Independent(self.page_local, (0, 250, 350, 70))
        Line(self.page_local, (0, 330, 395, 3))
        self.label_tools = Label(self.page_local, (0, 335, 220, 27), "ʵ�ù��ߣ�")
        self.button_gift = Button(self.page_local, (0, 370, 100, 30), "�Ͽɶ�����")
        self.button_wiki = Button(self.page_local, (110, 370, 85, 30), "����ͼ��")


class Fight:
    def __init__(self, stack):
        # ��ʼ������
        self.page_fight = Widget(stack)
        stack.addWidget(self.page_fight)
        # ��ӿؼ�
        self.label_fight = Label(self.page_fight, (0, 12, 220, 18), "����ҳ�棺��ս/����")
        self.label_mat = Label(self.page_fight, (120, 50, 80, 18), "����ѡ��")
        self.re_fight = Check(self.page_fight, (0, 90, 180, 18), "�ٴ�����")
        self.mat = Combobox(self.page_fight, (110, 80, 100, 40))
        self.mat.addItems(["��", "����־", "��"])


class Disp:
    def __init__(self, stack):
        # ��ʼ������
        self.page_dispatch = Widget(stack)
        stack.addWidget(self.page_dispatch)
        # ��ӿؼ�
        self.label_dispatch = Label(self.page_dispatch, (0, 12, 180, 18), "����ҳ�棺̽����ǲ")

        self.check_redisp = Check(self.page_dispatch, (0, 50, 180, 18), "�ٴβɹ�")

        self.label_disp_mat = Label(self.page_dispatch, (25, 80, 80, 27), "����ѡ��")
        self.label_fund = Label(self.page_dispatch, (130, 80, 80, 27), "�ʽ�ѡ��")
        self.label_plan = Label(self.page_dispatch, (260, 80, 80, 27), "����ѡ��")

        self.mat0 = Combobox(self.page_dispatch, (0, 110, 100, 32))
        self.mat1 = Combobox(self.page_dispatch, (0, 150, 100, 32))
        self.mat2 = Combobox(self.page_dispatch, (0, 190, 100, 32))
        self.mat3 = Combobox(self.page_dispatch, (0, 230, 100, 32))
        self.mat4 = Combobox(self.page_dispatch, (0, 270, 100, 32))
        self.mat5 = Combobox(self.page_dispatch, (0, 310, 100, 32))

        self.fund0 = Combobox(self.page_dispatch, (115, 110, 100, 32))
        self.fund1 = Combobox(self.page_dispatch, (115, 150, 100, 32))
        self.fund2 = Combobox(self.page_dispatch, (115, 190, 100, 32))
        self.fund3 = Combobox(self.page_dispatch, (115, 230, 100, 32))
        self.fund4 = Combobox(self.page_dispatch, (115, 270, 100, 32))
        self.fund5 = Combobox(self.page_dispatch, (115, 310, 100, 32))

        self.plan0 = Combobox(self.page_dispatch, (225, 110, 140, 32))
        self.plan1 = Combobox(self.page_dispatch, (225, 150, 140, 32))
        self.plan2 = Combobox(self.page_dispatch, (225, 190, 140, 32))
        self.plan3 = Combobox(self.page_dispatch, (225, 230, 140, 32))
        self.plan4 = Combobox(self.page_dispatch, (225, 270, 140, 32))
        self.plan5 = Combobox(self.page_dispatch, (225, 310, 140, 32))

        mat_list = ["ʳ��", "����", "����", "ʳ��", "����", "����", "����", "��ĩ", "���Ϸ�", "��������"]
        self.mat0.addItems(mat_list)
        self.mat1.addItems(mat_list)
        self.mat2.addItems(mat_list)
        self.mat3.addItems(mat_list)
        self.mat4.addItems(mat_list)
        self.mat5.addItems(mat_list)

        fund_list = ["��Ԫ��", "1000��", "2000��", "3000��"]
        self.fund0.addItems(fund_list)
        self.fund1.addItems(fund_list)
        self.fund2.addItems(fund_list)
        self.fund3.addItems(fund_list)
        self.fund4.addItems(fund_list)
        self.fund5.addItems(fund_list)

        plan_list = ["����̶���Ʒ", "���������Ʒ", "���ٲɹ�ʱ��"]
        self.plan0.addItems(plan_list)
        self.plan1.addItems(plan_list)
        self.plan2.addItems(plan_list)
        self.plan3.addItems(plan_list)
        self.plan4.addItems(plan_list)
        self.plan5.addItems(plan_list)


class Review:
    def __init__(self, stack):
        # ��ʼ������
        self.page_review = Widget(stack)
        stack.addWidget(self.page_review)
        # ��ӿؼ�
        self.label_review = Label(self.page_review, (0, 12, 200, 18), "����ҳ�棺ս���ع�")

        self.label_review_choose = Label(self.page_review, (0, 50, 100, 18), "ս���ع�ѡ��")
        self.num_box_review = DoubleSpinBox(self.page_review)
        self.num_box_review.setGeometry(QtCore.QRect(0, 80, 160, 30))


class Market:
    def __init__(self, stack):
        # ��ʼ������
        self.page_market = Widget(stack)
        stack.addWidget(self.page_market)
        # ��ӿؼ�
        self.label_market = Label(self.page_market, (0, 12, 180, 18), "����ҳ�棺��ȡ����")
        self.label_market_tip = Label(self.page_market, (90, 80, 220, 27), "��ȡ���� ����������Ŀ��")


class Recruit:
    def __init__(self, stack):
        # ��ʼ������
        self.page_recruit = Widget(stack)
        stack.addWidget(self.page_recruit)
        # ��ӿؼ�
        self.label_recruit = Label(self.page_recruit, (0, 12, 180, 18), "����ҳ�棺���ѷ�ļ")

        self.check_accelerate = Check(self.page_recruit, (0, 85, 80, 22), "����")
        self.label_recruit_plan = Label(self.page_recruit, (115, 50, 80, 18), "��ļ�ƻ�")
        self.recruit_plan = Combobox(self.page_recruit, (105, 80, 100, 32))
        self.recruit_plan.addItems(["0��", "100��", "200��", "300��", "400��", "500��", "600��", "700��"])

        self.button_history = TransPicButton(
            self.page_recruit, (220, 45, 30, 30),
            "assets/main_window/ui/history.png", (25, 25))
        self.button_directory = TransPicButton(
            self.page_recruit, (220, 85, 30, 30),
            "assets/main_window/ui/directory.png", (25, 25))


class Reward:
    def __init__(self, stack):
        # ��ʼ������
        self.page_reward = Widget(stack)
        stack.addWidget(self.page_reward)
        # ��ӿؼ�
        self.label_reward = Label(self.page_reward, (0, 12, 180, 18), "����ҳ�棺ÿ�չ���")
        self.label_reward_tip = Label(self.page_reward, (90, 80, 220, 27), "ÿ�չ��� ����������Ŀ��")


class Network:
    def __init__(self, stack):
        # ��ʼ������
        self.page_network = Widget(stack)
        stack.addWidget(self.page_network)
        # ��ӿؼ�
        self.label_network = Label(self.page_network, (0, 12, 180, 18), "����ҳ�棺��������")
        self.label_network_tip = Label(self.page_network, (90, 80, 220, 27), "�������� ����������Ŀ��")


class Mail:
    def __init__(self, stack):
        # ��ʼ������
        self.page_mail = Widget(stack)
        stack.addWidget(self.page_mail)
        # ��ӿؼ�
        self.label_mail = Label(self.page_mail, (0, 12, 180, 18), "����ҳ�棺��ȡ�ʼ�")
        self.label_mail_tip = Label(self.page_mail, (90, 80, 220, 27), "��ȡ�ʼ� ����������Ŀ��")


class Roll:
    def __init__(self, stack):
        # ��ʼ������
        self.page_roll = Widget(stack)
        stack.addWidget(self.page_roll)
        # ��ӿؼ�
        self.label_roll = Label(self.page_roll, (0, 12, 180, 18), "����ҳ�棺�鿨��¼")
        self.button_arrange = Button(self.page_roll, (0, 45, 180, 30), "�����鿨��¼ΪExcel")
        self.button_open_roll = (
            TransPicButton(self.page_roll, (185, 45, 30, 30),
                           "assets/main_window/ui/directory.png", (25, 25)))
        self.label_roll_tip = Label(self.page_roll, (90, 100, 220, 27), "�鿨��¼ ����������Ŀ��")


class KleinStack(Local, Fight, Disp, Review, Market, Recruit, Reward, Network, Mail, Roll):
    def __init__(self, widget, location):
        # ���ܶѵ�����
        self.stack = Stack(widget, location)
        Local.__init__(self, self.stack)
        Fight.__init__(self, self.stack)
        Disp.__init__(self, self.stack)
        Review.__init__(self, self.stack)
        Market.__init__(self, self.stack)
        Recruit.__init__(self, self.stack)
        Reward.__init__(self, self.stack)
        Network.__init__(self, self.stack)
        Mail.__init__(self, self.stack)
        Roll.__init__(self, self.stack)
