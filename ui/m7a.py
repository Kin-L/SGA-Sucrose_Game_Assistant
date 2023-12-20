# -*- coding:gbk -*-
from ui.element.control import *
from ui.element.ui_part import Independent


class M7AList:
    def __init__(self, widget, location):
        # 运行列表窗口
        self.scroll_list = Widget(widget, location)
        self.label_m7a = Label(self.scroll_list, (70, 10, 120, 20), "三月七助手", 18)
        Line(widget, (215, 5, 3, 505), False)


class M7AStack:
    def __init__(self, widget, location):
        # 功能堆叠窗口
        self.stack = Stack(widget, location)
        # 功能堆叠窗口
        self.stack = Widget(self.stack, (0, 0, 395, 515))
        self.label_local = Label(self.stack, (0, 12, 220, 18), "设置页面：三月七助手 运行方式")
        Line(self.stack, (0, 41, 395, 3))
        
        self.label_m7a_overall = Label(self.stack, (0, 45, 180, 27), "全局设置：")
        self.label_start = Label(self.stack, (0, 80, 80, 27), "启动路径")
        self.line_start = Lineedit(self.stack, (0, 110, 385, 33))
        Line(self.stack, (0, 152, 395, 3))

        self.label_team_tip = Label(self.stack, (0, 160, 220, 27), "独立运行设置：")
        self.independent = Independent(self.stack, (0, 200, 350, 70), False)


class M7A:
    def __init__(self, stack, icon, main):
        # 三月七助手
        self.widget_m7a = Widget()
        stack.addWidget(self.widget_m7a)
        self.button_m7a = (
            PicButton(icon, (220, 0, 50, 50), 
                      r"assets\m7a\picture\M7A-icon.png", (50, 50)))
        self.list = None
        self.set = None

    def load_window(self):
        self.list = M7AList(self.widget_m7a, (0, 0, 215, 515))
        self.set = M7AStack(self.widget_m7a, (225, 0, 395, 515))
        Line(self.widget_m7a, (215, 5, 3, 505), False)

    def load_run(self, run):
        self.set.line_start.setText(run)
        self.set.line_start.setSelection(0, 0)

    def get_run(self):
        return self.set.line_start.text()

    def input_config(self, config):
        run_list = config["运行"]
        self.set.independent.check_mute.setChecked(run_list[0])
        self.set.independent.combo_after.setCurrentIndex(run_list[2])
        self.set.independent.check_kill_sga.setChecked(run_list[3])

    def output_config(self):
        config = dict()
        config["模块"] = 4
        config["运行"] = [self.set.independent.check_mute.isChecked(),
                        True,
                        self.set.independent.combo_after.currentIndex(),
                        self.set.independent.check_kill_sga.isChecked()]
        return config
