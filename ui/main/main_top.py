from .main_up import MainUp
from tools.environment import *
import sys
from tools.software import *
from PyQt5.QtGui import QPixmap


class MainTop(MainUp):
    def __init__(self):
        super().__init__()
        self.cycle = None
        self.sga_run = None
        self.kill = None

    def function_connect(self):
        # 主面板操作
        self.button_set_home.toggled.connect(self.change_interface)
        self.button_sponsor.clicked.connect(self.window_support.show)
        self.button_statement.clicked.connect(self.show_statement)
        self.button_instructions.clicked.connect(lambda: cmd_run("start "" SGA使用说明.docx"))
        self.button_history.clicked.connect(lambda: cmd_run("start /d \"personal\" history.txt"))
        # 全局设置操作
        self.overall.timer.apply.clicked.connect(self.apply_timer)
        # 配置操作
        self.button_config_delete.clicked.connect(self.delete_plan)
        self.box_config_change.currentTextChanged.connect(self.config_change)
        self.button_config_lock.clicked.connect(lambda: self.set_config_lock(False))
        self.button_config_unlock.clicked.connect(lambda: self.set_config_lock(True))
        self.button_config_save.clicked.connect(self.save_config)
        self.button_start.clicked.connect(lambda: self.start())
        self.button_pause.clicked.connect(lambda: self.pause(2))
        # 切换面板
        self.mix.button_mix.clicked.connect(lambda: self.change_module(0))
        self.kleins.button_klein.clicked.connect(lambda: self.change_module(1))
        self.genshin.button_genshin.clicked.connect(lambda: self.change_module(2))
        self.maa.button_maa.clicked.connect(lambda: self.change_module(3))
        self.m7a.button_m7a.clicked.connect(lambda: self.change_module(4))

    def start(self):
        self.cycle.terminate()
        self.task = self.get_config_run()
        self.task["name"] = ""
        self.task["current_mute"] = get_mute()
        if self.task["运行"][0] and not self.task["current_mute"]:
            change_mute()
        self.box_info.clear()
        self.indicate("", 1)
        _name = self.task["name"]
        if _name:
            self.indicate(f"开始执行定时计划：\n  {_name}")
            notify("开始定时任务", f"任务名：{_name}")
        else:
            self.indicate("开始执行实时计划。")
        pixmap = QPixmap(r"assets\main_window\ui\ico\0.png")
        self.label_status.setPixmap(pixmap)
        self.button_pause.show()
        self.button_start.hide()

        self.kill.start()
        self.sga_run.start()

    def pause(self, mode: int):
        self.state["wait_time"] = 5
        SetForegroundWindow(self.state["hwnd"])
        if mode == 2:
            self.sga_run.terminate()
            self.kill.terminate()
            pixmap = QPixmap(r"assets\main_window\ui\ico\2.png")
            self.indicate("手动终止。")
            self.indicate(" ", 2, True)
            self.button_pause.hide()
            self.button_start.show()
            self.label_status.setPixmap(pixmap)
        else:
            if mode == 1:
                pixmap = QPixmap(r"assets\main_window\ui\ico\1.png")
                _str0 = "完成"
            elif mode == 3:
                _str0 = "异常"
                pixmap = QPixmap(r"assets\main_window\ui\ico\3.png")
            else:
                logger.critical("无效模式")
                sys.exit(1)
            self.label_status.setPixmap(pixmap)
            # 通知
            if self.task["name"]:
                _text = f"定时计划执行{_str0}。"
                notify(_text, "任务名："+self.task["name"])
                self.indicate(_text)
                self.indicate("  任务名：" + self.task["name"], 2)
            else:
                _text = f"实时计划执行{_str0}。"
                notify(f"实时计划执行{_str0}。", " ")
                self.indicate(_text)
            if self.task["运行"][2] == 1:
                self.indicate("  任务完成，20s后熄屏。", 2, False)
                self.indicate("  可按组合键“ctrl+/”取消。", 2, False)
            elif self.task["运行"][2] == 2:
                self.indicate("  任务完成，60s后睡眠。", 2, False)
                self.indicate("  可按组合键“ctrl+/”取消。", 2, False)
            now_mute = get_mute()
            if (now_mute != self.task["current_mute"]) and (now_mute == self.task["运行"][0]):
                wait(1000)
                move(50, 50)
                wait(200)
                change_mute()
            # 结束
            if self.task["运行"][2] == 1:
                wait(20000)
                self.kill.terminate()
                self.button_pause.hide()
                self.button_start.show()
                if self.task["运行"][3]:
                    self.indicate("SGA关闭 电脑熄屏", 2, False)
                    self.indicate(" ", 2, True)
                    cmd_run("start "" /d \"assets/main_window/bat_scr\" screen_off.vbs")
                    sys.exit(0)
                else:
                    self.indicate("SGA等待 电脑熄屏", 2, False)
                    self.indicate(" ", 2, True)
                    screen_off()
            elif self.task["运行"][2] == 2:
                wait(60000)
                self.kill.terminate()
                self.button_pause.hide()
                self.button_start.show()
                if self.task["运行"][3]:
                    self.indicate("SGA关闭 电脑睡眠", 2, False)
                    self.indicate(" ", 2, True)
                    cmd_run("start "" /d \"assets/main_window/bat_scr\" sleep.vbs")
                    sys.exit(0)
                else:
                    self.indicate("SGA等待 电脑睡眠", 2, False)
                    self.indicate(" ", 2, True)
                    self.state["wait_time"] = 5
                    self.cycle.start()
                    cmd_run("start "" /d \"assets/main_window/bat_scr\" sleep.vbs")
            else:
                self.kill.terminate()
                if self.task["运行"][3]:
                    self.indicate("SGA关闭 电脑无操作", 2, False)
                    self.indicate(" ", 2, True)
                    sys.exit(0)
                else:
                    self.button_pause.hide()
                    self.button_start.show()
                    self.state["wait_time"] = 5
                    self.indicate("SGA等待 电脑无操作", 2, False)
                    self.indicate(" ", 2, True)
                    self.cycle.start()
