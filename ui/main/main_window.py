# -*- coding:gbk -*-
from ui.element.control import *
from ui.element.ui_part import *
import time
from tools.environment import logger


# 主窗口
class MainWindow:  # FramelessWindow
    def __init__(self):
        # 主窗口初始化
        self.main_window = MWindow()
        self.button_set_home = OverallButton(self.main_window)  # 全局/模块 设置按钮
        self.button_history = PicButton(self.main_window, (693, 0, 56, 56),  # 历史信息按钮
                                        r"assets\main_window\ui\history.png", (25, 25))
        self.button_sponsor = PicButton(self.main_window, (751, 0, 56, 56),  # 赞赏按钮
                                        r"assets\main_window\ui\support.png", (25, 25))
        self.window_support = Support()
        self.button_statement = Button(self.main_window, (809, 0, 96, 27), "使用须知")
        self.button_instructions = Button(self.main_window, (809, 29, 96, 27), "使用说明")
        self.label_status = Picture(self.main_window, (485, 430, 150, 150),   # 指示图标
                                    r"assets\main_window\ui\ico\0.png")
        self.box_info = InfoBox(self.main_window)  # 指示信息窗口
        self.stack_setting = Stack(self.main_window, (5, 0, 620, 570))
        self.state = \
            {"name": ["mix", "kleins", "genshin", "maa", "m7a"],
             "prefix": ["00", "01", "02", "03", "04"],
             "mix":     {"load": False, "prefix": "00"},
             "kleins":   {"load": False, "prefix": "01"},
             "genshin": {"load": False, "prefix": "02"},
             "maa":     {"load": False, "prefix": "03"},
             "m7a":     {"load": False, "prefix": "04"},
             "plan":    {},    "serial": [],   "single":    [],
             "stack":   None,  "locked": None, "hwnd":      None,
             "text":    None,  "index":  None, "wait_time": 1}
        self.config = type[dir]
        self.task = {}
        self.overall = None

        # 信息栏显示信息
    def indicate(self, msg="", mode=0, log=True, write=True):
        if log:
            logger.info(msg)
        txt = open(r"personal\history.txt", 'a+', encoding='utf-8')
        if mode == 0:  # 时间前缀的信息持续追加
            msg = time.strftime("%H:%M:%S ", time.localtime()) + msg
            msg = msg.replace("\n", "\n- ")
            self.box_info.append(msg)
            # self.send.emit(msg)
            self.box_info.ensureCursorVisible()
            if write:
                txt.write(msg + "\n")
        elif mode == 1:  # 时间前缀的信息单项追加
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.box_info.append(now_time)
            # self.send.emit(now_time)
            if msg:
                self.box_info.append(msg)
                self.box_info.append(" ")
                # self.send.emit(msg)
                # self.send.emit(" ")
                self.box_info.ensureCursorVisible()
            if write:
                txt.write(f"{now_time}\n")
                if msg:
                    txt.write(f"{msg}\n\n")
        elif mode == 2:  # 直接追加信息
            self.box_info.append(msg)
            # self.send.emit(msg)
            self.box_info.ensureCursorVisible()
            if write:
                txt.write("\n")
        elif mode == 3:
            self.box_info.clear()
        else:
            pass
