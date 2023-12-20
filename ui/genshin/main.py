# -*- coding:gbk -*-
from .list import GenshinList
from .stack import GenshinStack
from ui.element.control import Line, Widget, PicButton


class Genshin:
    def __init__(self, stack, icon, main):
        self.widget_genshin = Widget()
        stack.addWidget(self.widget_genshin)
        self.button_genshin = (
            PicButton(icon, (110, 0, 50, 50),
                      r"assets\genshin\picture\genshin-icon.png", (50, 50)))
        self.list = None
        self.set = None

    def load_window(self):
        self.list = GenshinList(self.widget_genshin, (0, 0, 215, 515))
        self.set = GenshinStack(self.widget_genshin, (225, 0, 410, 515))
        self.list.set_genshin.clicked.connect(lambda: self.set.stack.setCurrentIndex(0))
        self.list.set_team.clicked.connect(lambda: self.set.stack.setCurrentIndex(1))
        self.list.set_disp.clicked.connect(lambda: self.set.stack.setCurrentIndex(2))
        self.list.set_trans.clicked.connect(lambda: self.set.stack.setCurrentIndex(3))
        self.list.set_fly.clicked.connect(lambda: self.set.stack.setCurrentIndex(4))
        self.list.set_comp.clicked.connect(lambda: self.set.stack.setCurrentIndex(5))
        self.list.set_pot.clicked.connect(lambda: self.set.stack.setCurrentIndex(6))
        self.list.set_mail.clicked.connect(lambda: self.set.stack.setCurrentIndex(7))
        self.list.set_tree.clicked.connect(lambda: self.set.stack.setCurrentIndex(8))
        Line(self.widget_genshin, (215, 5, 3, 505), False)

    def load_run(self, run):
        server, path = run
        self.set.combo_server.setCurrentIndex(server)
        self.set.line_start.setText(path)
        self.set.line_start.setSelection(0, 0)

    def get_run(self):
        sever = self.set.combo_server.currentIndex()
        start = self.set.line_start.text()
        return [sever, start]

    def input_config(self, config):
        run_list = config["运行"]
        self.set.independent.check_mute.setChecked(run_list[0])
        self.set.independent.check_kill_game.setChecked(run_list[1])
        self.set.independent.combo_after.setCurrentIndex(run_list[2])
        self.set.independent.check_kill_sga.setChecked(run_list[3])
        check_list = config["功能"]
        self.list.check_team.setChecked(check_list[0])
        self.list.check_disp.setChecked(check_list[1])
        self.list.check_trans.setChecked(check_list[2])
        self.list.check_fly.setChecked(check_list[3])
        self.list.check_comp.setChecked(check_list[4])
        self.list.check_pot.setChecked(check_list[5])
        self.list.check_mail.setChecked(check_list[6])
        self.list.check_tree.setChecked(check_list[7])
        disp_list = config["派遣"]
        self.set.area0.setCurrentIndex(disp_list[0][0])
        self.set.area1.setCurrentIndex(disp_list[1][0])
        self.set.area2.setCurrentIndex(disp_list[2][0])
        self.set.area3.setCurrentIndex(disp_list[3][0])
        self.set.area4.setCurrentIndex(disp_list[4][0])
        self.set.list_change(self.set.area0, self.set.mat0)
        self.set.list_change(self.set.area1, self.set.mat1)
        self.set.list_change(self.set.area2, self.set.mat2)
        self.set.list_change(self.set.area3, self.set.mat3)
        self.set.list_change(self.set.area4, self.set.mat4)
        self.set.mat0.setCurrentIndex(disp_list[0][1])
        self.set.mat1.setCurrentIndex(disp_list[1][1])
        self.set.mat2.setCurrentIndex(disp_list[2][1])
        self.set.mat3.setCurrentIndex(disp_list[3][1])
        self.set.mat4.setCurrentIndex(disp_list[4][1])
        self.set.redisp.setChecked(disp_list[5])

        trans_list = config["参量质变仪"]
        self.set.LineEdit0.setText(trans_list[0])
        self.set.LineEdit1.setText(trans_list[1])
        self.set.LineEdit2.setText(trans_list[2])
        self.set.LineEdit3.setText(trans_list[3])
        self.set.LineEdit4.setText(trans_list[4])
        fly_list = config["晶蝶"]
        self.set.fly0.setChecked(fly_list[0]), self.set.fly1.setChecked(fly_list[1])
        self.set.fly2.setChecked(fly_list[2]), self.set.fly0.setChecked(fly_list[3])
        self.set.fly4.setChecked(fly_list[4])
        tree_list = config["砍树"]
        self.set.CompactSpinBox.setValue(tree_list[0])
        self.set.tree0.setChecked(tree_list[1][0]), self.set.tree1.setChecked(tree_list[1][1])
        self.set.tree2.setChecked(tree_list[1][2]), self.set.tree3.setChecked(tree_list[1][3])
        self.set.tree4.setChecked(tree_list[1][4]), self.set.tree5.setChecked(tree_list[1][5])
        self.set.tree6.setChecked(tree_list[1][6]), self.set.tree7.setChecked(tree_list[1][7])
        self.set.tree8.setChecked(tree_list[1][8]), self.set.tree9.setChecked(tree_list[1][9])
        self.set.tree10.setChecked(tree_list[1][10]), self.set.tree11.setChecked(tree_list[1][11])
        self.set.tree12.setChecked(tree_list[1][12]), self.set.tree13.setChecked(tree_list[1][13])
        self.set.tree14.setChecked(tree_list[1][14]), self.set.tree15.setChecked(tree_list[1][15])
        self.set.tree16.setChecked(tree_list[1][16]), self.set.tree17.setChecked(tree_list[1][17])
        self.set.tree18.setChecked(tree_list[1][18])

    def output_config(self):
        config = dict()
        config["模块"] = 2
        config["运行"] = [self.set.independent.check_mute.isChecked(),
                        self.set.independent.check_kill_game.isChecked(),
                        self.set.independent.combo_after.currentIndex(),
                        self.set.independent.check_kill_sga.isChecked()]
        config["功能"] = \
            [self.list.check_team.isChecked(), self.list.check_disp.isChecked(),
             self.list.check_trans.isChecked(), self.list.check_fly.isChecked(),
             self.list.check_comp.isChecked(), self.list.check_pot.isChecked(),
             self.list.check_mail.isChecked(), self.list.check_tree.isChecked()]
        config["派遣"] = \
            [[self.set.area0.currentIndex(), self.set.mat0.currentIndex()],
             [self.set.area1.currentIndex(), self.set.mat1.currentIndex()],
             [self.set.area2.currentIndex(), self.set.mat2.currentIndex()],
             [self.set.area3.currentIndex(), self.set.mat3.currentIndex()],
             [self.set.area4.currentIndex(), self.set.mat4.currentIndex()],
             self.set.redisp.isChecked()]
        config["参量质变仪"] = \
            [self.set.LineEdit0.text(), self.set.LineEdit1.text(), self.set.LineEdit2.text(),
             self.set.LineEdit3.text(), self.set.LineEdit4.text()]
        config["晶蝶"] = \
            [self.set.fly0.isChecked(), self.set.fly1.isChecked(),
             self.set.fly2.isChecked(), self.set.fly3.isChecked(),
             self.set.fly4.isChecked()]
        config["砍树"] = \
            [self.set.CompactSpinBox.value(),
             [self.set.tree0.isChecked(), self.set.tree1.isChecked(),
              self.set.tree2.isChecked(), self.set.tree3.isChecked(),
              self.set.tree4.isChecked(), self.set.tree5.isChecked(),
              self.set.tree6.isChecked(), self.set.tree7.isChecked(),
              self.set.tree8.isChecked(), self.set.tree9.isChecked(),
              self.set.tree10.isChecked(), self.set.tree11.isChecked(),
              self.set.tree12.isChecked(), self.set.tree13.isChecked(),
              self.set.tree14.isChecked(), self.set.tree15.isChecked(),
              self.set.tree16.isChecked(), self.set.tree17.isChecked(),
              self.set.tree18.isChecked()]]
        return config
