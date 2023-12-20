# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from ui.main.main_top import *
from ui.element.control import *
from ui.element.ui_part import *
import traceback
from PyQt5.QtCore import QThread, pyqtSignal
from task.main import TaskRun
import time
# pyinstaller -D -w -i D:\Kin-project\python-SGA\assets\main_window\ui\ico\SGA.ico D:\Kin-project\python-SGA\SGA2.0_main_demo.py


class Kill(QThread):
    send = pyqtSignal(str, int, bool, bool)
    
    def __init__(self, ui):  # mode true：集成运行 false：独立运行
        super().__init__()
        self.ui = ui

    def run(self):
        import keyboard
        keyboard.wait("ctrl+/")
        self.ui.state["wait_time"] = 5
        SetForegroundWindow(self.ui.state["hwnd"])
        self.ui.sga_run.terminate()
        pixmap = QPixmap(r"../assets/main_window/ui/ico/2.png")
        self.indicate("手动终止。")
        self.indicate(" ", 2, True)
        self.ui.button_pause.hide()
        self.ui.button_start.show()
        self.ui.label_status.setPixmap(pixmap)
    
    def indicate(self, msg: str, mode=0, log=True, write=True):
        self.send.emit(msg, mode, log, write)
        

class Cycle(QThread, TaskRun):
    send = pyqtSignal(str, int, bool, bool)

    def __init__(self, ui):  # mode true：集成运行 false：独立运行
        super(Cycle, self).__init__()
        self.ui = ui

    def run(self):
        for i in range(self.ui.state["wait_time"]):
            time.sleep(6)
            self.ui.save_main_data()
        while 1:
            text = self.ui.check_timer()
            if text:
                self.time_to_run(text)
                print(2)
                break
            time.sleep(10)
            self.ui.save_main_data()
            time.sleep(10)

    def indicate(self, msg: str, mode=0, log=True, write=True):
        self.send.emit(msg, mode, log, write)
    
    def time_to_run(self, mode: str = ""):
        self.ui.task = self.ui.get_config_run(mode)
        self.ui.task["name"] = mode
        self.ui.task["current_mute"] = get_mute()
        if self.ui.task["运行"][0] and not self.ui.task["current_mute"]:
            change_mute()
        self.indicate("", 3)
        self.indicate("", 1)
        _name = self.ui.task["name"]
        if _name:
            self.indicate(f"开始执行定时计划：\n  {_name}")
            notify("开始定时任务", f"任务名：{_name}")
        else:
            self.indicate("开始执行实时计划。")
        pixmap = QPixmap(r"../assets/main_window/ui/ico/0.png")
        self.ui.label_status.setPixmap(pixmap)
        self.ui.button_pause.show()
        self.ui.button_start.hide()

        self.ui.kill.start()
        self.ui.sga_run.start()


class SGARun(QThread, TaskRun):
    send = pyqtSignal(str, int, bool, bool)
    pause = pyqtSignal(int)

    def __init__(self, ui):  # mode true：集成运行 false：独立运行
        super(SGARun, self).__init__()
        self.ui = ui

    def run(self):
        try:
            self.task_start(self.ui.task)
        except:
            logger.error("任务执行异常：\n%s" % traceback.format_exc())
            self.kill(3)

    def indicate(self, msg: str, mode=0, log=True, write=True):
        self.send.emit(msg, mode, log, write)

    def kill(self, mode):
        self.ui.state["wait_time"] = 5
        SetForegroundWindow(self.ui.state["hwnd"])
        if mode == 1:
            pixmap = QPixmap(r"../assets/main_window/ui/ico/1.png")
            _str0 = "完成"
        elif mode == 3:
            _str0 = "异常"
            pixmap = QPixmap(r"../assets/main_window/ui/ico/3.png")
        else:
            logger.critical("无效模式")
            sys.exit(1)
        self.ui.label_status.setPixmap(pixmap)
        # 通知
        if self.ui.task["name"]:
            _text = f"定时计划执行{_str0}。"
            notify(_text, "任务名：" + self.ui.task["name"])
            self.indicate(_text)
            self.indicate("  任务名：" + self.ui.task["name"], 2)
        else:
            _text = f"实时计划执行{_str0}。"
            notify(f"实时计划执行{_str0}。", " ")
            self.indicate(_text)
        if self.ui.task["运行"][2] == 1:
            self.indicate("  任务完成，20s后熄屏。", 2, False)
            self.indicate("  可按组合键“ctrl+/”取消。", 2, False)
        elif self.ui.task["运行"][2] == 2:
            self.indicate("  任务完成，60s后睡眠。", 2, False)
            self.indicate("  可按组合键“ctrl+/”取消。", 2, False)
        now_mute = get_mute()
        if (now_mute != self.ui.task["current_mute"]) and (now_mute == self.ui.task["运行"][0]):
            wait(1000)
            move(50, 50)
            wait(200)
            change_mute()
        # 结束
        if self.ui.task["运行"][2] == 1:
            wait(20000)
            self.ui.kill.terminate()
            self.ui.button_pause.hide()
            self.ui.button_start.show()
            if self.ui.task["运行"][3]:
                self.indicate("SGA关闭 电脑熄屏", 2, False)
                self.indicate(" ", 2, True)
                cmd_run("start "" /d \"assets/main_window/bat_scr\" screen_off.vbs")
                sys.exit(0)
            else:
                self.indicate("SGA等待 电脑熄屏", 2, False)
                self.indicate(" ", 2, True)
                screen_off()
        elif self.ui.task["运行"][2] == 2:
            wait(60000)
            self.ui.kill.terminate()
            self.ui.button_pause.hide()
            self.ui.button_start.show()
            if self.ui.task["运行"][3]:
                self.indicate("SGA关闭 电脑睡眠", 2, False)
                self.indicate(" ", 2, True)
                cmd_run("start "" /d \"assets/main_window/bat_scr\" sleep.vbs")
                sys.exit(0)
            else:
                self.indicate("SGA等待 电脑睡眠", 2, False)
                self.indicate(" ", 2, True)
                self.ui.state["wait_time"] = 5
                self.ui.cycle.start()
                cmd_run("start "" /d \"assets/main_window/bat_scr\" sleep.vbs")
        else:
            self.ui.kill.terminate()
            if self.ui.task["运行"][3]:
                self.indicate("SGA关闭 电脑无操作", 2, False)
                self.indicate(" ", 2, True)
                sys.exit(0)
            else:
                self.ui.button_pause.hide()
                self.ui.button_start.show()
                self.ui.state["wait_time"] = 5
                self.indicate("SGA等待 电脑无操作", 2, False)
                self.indicate(" ", 2, True)
                self.ui.cycle.start()


# w = Demo()
# 初始化窗口
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
application = QApplication(sys.argv)
logger.debug("启动SGA用户界面。")
# super().__init__()
sga_ui = MainTop()
sga_ui.main_window.show()
from pyautogui import press as papress
papress("prtsc")
# 加载主配置
try:
    sga_ui.load_main_config()
    logger.debug("主配置加载成功。(4/6)")
except Exception as err:
    message_box("主配置加载失败(3/6)：\n%s" % err)
    logger.critical("主配置加载失败(3/6)：\n%s" % traceback.format_exc())
    sys.exit(1)
# 功能链接
try:
    # 功能键链接
    sga_ui.function_connect()
    logger.debug("状态设置成功。(5/6)")
except Exception as err:
    MessageBox(0, "状态设置失败(4/6)：\n%s" % err, "砂糖代理", MB_OK)
    logger.critical("状态设置失败(4/6)：\n%s" % traceback.format_exc())
    sys.exit(1)
try:
    # 全局设置：退出前保存 & 每10秒自动保存
    import atexit
    atexit.register(sga_ui.exit_save)
    sga_ui.cycle = Cycle(sga_ui)
    sga_ui.kill = Kill(sga_ui)
    sga_ui.sga_run = SGARun(sga_ui)
    sga_ui.kill.send.connect(sga_ui.indicate)
    sga_ui.sga_run.send.connect(sga_ui.indicate)
    sga_ui.cycle.send.connect(sga_ui.indicate)
    # sga_ui.cycle.pause.connect(sga_ui.pause)
    sga_ui.cycle.start()
    logger.debug("后台线程加载完成。(6/6)")
except Exception as err:
    MessageBox(0, "后台线程加载失败(5/6)：\n%s" % err, "砂糖代理", MB_OK)
    logger.critical("后台线程加载失败(5/6)：\n%s" % traceback.format_exc())
    sys.exit(1)
application.exec_()


if __name__ == "__main__":
    pass
