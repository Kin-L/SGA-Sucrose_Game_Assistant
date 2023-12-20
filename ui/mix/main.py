# -*- coding:gbk -*-
from ui.element.control import *
from .list import MixList
from .stack import MixStack


# ԭ��ģ�����ô���
class Mix:
    def __init__(self, stack, icon, main):
        # ��������
        self.widget_mix = Widget()
        stack.addWidget(self.widget_mix)
        self.button_mix = PicButton(icon, (0, 0, 50, 50),
                                    r"assets\main_window\ui\mix-icon.png", (50, 50))
        self.list = None
        self.set = None

    def load_window(self):
        self.list = MixList(self.widget_mix, (0, 0, 215, 515))
        self.set = MixStack(self.widget_mix, (225, 0, 395, 515))
        Line(self.widget_mix, (215, 5, 3, 505), False)

    def load_single(self, single):
        # �����б����ü���
        self.list.combobox_mix_config0.addItems(["<δѡ��>"] + single)
        self.list.combobox_mix_config1.addItems(["<δѡ��>"] + single)
        self.list.combobox_mix_config2.addItems(["<δѡ��>"] + single)
        self.list.combobox_mix_config3.addItems(["<δѡ��>"] + single)
        self.list.combobox_mix_config4.addItems(["<δѡ��>"] + single)

    def add_item(self, name):
        self.list.combobox_mix_config0.addItem(name)
        self.list.combobox_mix_config1.addItem(name)
        self.list.combobox_mix_config2.addItem(name)
        self.list.combobox_mix_config3.addItem(name)
        self.list.combobox_mix_config4.addItem(name)

    def remove_item(self, name):
        self.list.combobox_mix_config0.removeItem(self.list.combobox_mix_config0.findText(name))
        self.list.combobox_mix_config1.removeItem(self.list.combobox_mix_config0.findText(name))
        self.list.combobox_mix_config2.removeItem(self.list.combobox_mix_config0.findText(name))
        self.list.combobox_mix_config3.removeItem(self.list.combobox_mix_config0.findText(name))
        self.list.combobox_mix_config4.removeItem(self.list.combobox_mix_config0.findText(name))

    def rename_item(self, old_name, new_name):
        self.list.combobox_mix_config0.rename(old_name, new_name)
        self.list.combobox_mix_config1.rename(old_name, new_name)
        self.list.combobox_mix_config2.rename(old_name, new_name)
        self.list.combobox_mix_config3.rename(old_name, new_name)
        self.list.combobox_mix_config4.rename(old_name, new_name)

    def input_config(self, config):
        print(config)
        self.list.combobox_mix_config0.setCurrentText(config["����0"]["name"])
        self.list.combobox_mix_config1.setCurrentText(config["����1"]["name"])
        self.list.combobox_mix_config2.setCurrentText(config["����2"]["name"])
        self.list.combobox_mix_config3.setCurrentText(config["����3"]["name"])
        self.list.combobox_mix_config4.setCurrentText(config["����4"]["name"])

        run_list = config["����"]
        self.set.independent.check_mute.setChecked(run_list[0])
        self.set.independent.combo_after.setCurrentIndex(run_list[2])
        self.set.independent.check_kill_sga.setChecked(run_list[3])

    def output_config(self):
        config = dict()
        config["ģ��"] = 0
        config["����0"] = dict()
        config["����1"] = dict()
        config["����2"] = dict()
        config["����3"] = dict()
        config["����4"] = dict()
        config["����0"]["name"] = self.list.combobox_mix_config0.currentText()
        config["����1"]["name"] = self.list.combobox_mix_config1.currentText()
        config["����2"]["name"] = self.list.combobox_mix_config2.currentText()
        config["����3"]["name"] = self.list.combobox_mix_config3.currentText()
        config["����4"]["name"] = self.list.combobox_mix_config4.currentText()
        config["����"] = [self.set.independent.check_mute.isChecked(),
                        True,
                        self.set.independent.combo_after.currentIndex(),
                        self.set.independent.check_kill_sga.isChecked()]
        return config
