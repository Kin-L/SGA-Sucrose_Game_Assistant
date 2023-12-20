# -*- coding:gbk -*-
import os
import json
from ui.element.control import *
from ui.element.ui_part import Independent
import webbrowser

class MAAList:
    def __init__(self, widget, location):
        # �����б���
        self.scroll_list = Widget(widget, location)
        self.label_maa = Label(self.scroll_list, (100, 10, 80, 20), "MAA", 18)
        Line(widget, (215, 5, 3, 505), False)

        self.label_choose = Label(self.scroll_list, (5, 45, 110, 27), "ѡ��MAA����")
        self.refresh = (
            TransPicButton(self.scroll_list, (110, 50, 20, 20),
                           "assets/main_window/ui/refresh.png", (20, 20)))
        self.combox = Combobox(self.scroll_list, (5, 85, 200, 30))


class MAAStack:
    def __init__(self, widget, location):
        # ���ܶѵ�����
        self.stack = Stack(widget, location)
        # ���ܶѵ�����
        self.stack = Widget(self.stack, (0, 0, 395, 515))
        self.label_local = Label(self.stack, (0, 12, 220, 18), "����ҳ�棺MAA ���з�ʽ")
        Line(self.stack, (0, 41, 395, 3))

        self.label_maa_overall = Label(self.stack, (0, 45, 180, 27), "ȫ�����ã�")

        self.label_start = Label(self.stack, (0, 80, 80, 27), "����·��")
        self.line_start = Lineedit(self.stack, (0, 110, 385, 33))
        Line(self.stack, (0, 152, 395, 3))

        self.label_team_tip = Label(self.stack, (0, 160, 220, 27), "�����������ã�")
        self.independent = Independent(self.stack, (0, 200, 350, 70), True)
        self.independent.check_kill_game.setText("��ɺ�ر�ģ����")
        Line(self.stack, (0, 280, 395, 3))
        self.label_tools = Label(self.stack, (0, 285, 220, 27), "ʵ�ù��ߣ�")
        self.button_wiki = Button(self.stack, (0, 320, 70, 30), "BWIKI")
        self.button_mat = Button(self.stack, (80, 320, 70, 30), "һͼ��")
        self.button_turns = Button(self.stack, (160, 320, 100, 30), "�Ű�������")


class MAA:
    def __init__(self, stack, icon, main):
        self.main = main
        # MAA
        self.widget_maa = Widget()
        stack.addWidget(self.widget_maa)
        self.button_maa = PicButton(icon, (165, 0, 50, 50),
                                    r"assets\maa\picture\MAA-icon.png", (50, 50))
        self.list = None
        self.set = None
        
    def load_window(self):
        self.list = MAAList(self.widget_maa, (0, 0, 215, 515))
        self.set = MAAStack(self.widget_maa, (225, 0, 395, 515))
        Line(self.widget_maa, (215, 5, 3, 505), False)

        self.list.refresh.clicked.connect(self.refresh)
        self.set.button_wiki.clicked.connect(self.open_wiki)
        self.set.button_mat.clicked.connect(self.open_yituliu)
        self.set.button_turns.clicked.connect(self.open_turns)

    def refresh(self):
        _path = self.set.line_start.text().strip("\"")
        if os.path.isfile(_path):
            gui_path = os.path.split(_path)[0] + "/config/gui.json"
            with open(gui_path, 'r', encoding='utf-8') as g:
                maa = json.load(g)
            _list = list(maa["Configurations"].keys())
            if "SGA-cache" in _list:
                _list.remove("SGA-cache")
            self.list.combox.clear()
            self.list.combox.addItems(_list)
        self.main.indicate("MAA�����б���ˢ��", 1)

    def open_wiki(self):
        webbrowser.open("https://wiki.biligame.com/arknights/%E9%A6%96%E9%A1%B5")
        self.main.indicate("����ҳ: ���շ��� BWIKI", 1)

    def open_yituliu(self):
        webbrowser.open("https://yituliu.site/")
        self.main.indicate("����ҳ: һͼ��", 1)

    def open_turns(self):
        webbrowser.open("https://yituliu.site/tools/maa")
        self.main.indicate("����ҳ: �Ű�������", 1)

    def load_run(self, run):
        self.set.line_start.setText(run)
        self.set.line_start.setSelection(0, 0)

    def get_run(self):
        return self.set.line_start.text()

    def input_config(self, config):
        run_list = config["����"]
        self.set.independent.check_mute.setChecked(run_list[0])
        self.set.independent.check_kill_game.setChecked(run_list[1])
        self.set.independent.combo_after.setCurrentIndex(run_list[2])
        self.set.independent.check_kill_sga.setChecked(run_list[3])
        self.list.combox.addItems(config["����"][1])
        try:
            self.list.combox.setCurrentText(config["����"][0])
        except:
            self.list.combox.setCurrentIndex(0)

    def output_config(self):
        config = dict()
        config["ģ��"] = 3
        config["����"] = [self.set.independent.check_mute.isChecked(),
                        self.set.independent.check_kill_game.isChecked(),
                        self.set.independent.combo_after.currentIndex(),
                        self.set.independent.check_kill_sga.isChecked()]
        _cur = self.list.combox.currentText()
        _num = self.list.combox.count()
        _list = []
        for i in range(_num):
            _list += [self.list.combox.itemText(i)]
        _item = self.list.combox.count()
        config["����"] = [_cur, _list]
        return config
