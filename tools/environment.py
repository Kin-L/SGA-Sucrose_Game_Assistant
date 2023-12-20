from .operate import Operate
from .system import *


class Environment(Operate):
    def __init__(self, wide, high):
        super().__init__()
        self.get_user_admin()
        self.get_workdir()
        self.set_compile(wide, high)
        (self.resolution_origin,
         self.resolution_now,
         self.zoom_desktop) = get_resolution_zoom()
        self.mode()

    # 键鼠及识图缩放模式（全屏复刻模式：0， 软件窗口模式：1， 全屏普通模式：2）
    def mode(self, mode_num: int = 0):
        if mode_num == 0:
            self.frame = (0, 0) + self.resolution_origin
            self.zoom = self.resolution_origin[0] / self.resolution_compile[0]
            return True
        elif mode_num == 1:
            if self.soft.hwnd:
                if self.soft.get_window_information():
                    self.frame, self.zoom = self.soft.frame, self.soft.zoom
                    self.logger.debug(f"mode 1: {self.frame}*{self.zoom}")
                    return True
                else:
                    return False
            else:
                self.logger.error("未识别到软件/未开启软件")
                return False
        elif mode_num == 2:
            self.frame = (0, 0) + self.resolution_origin
            self.zoom = 1
            return True
        else:
            self.logger.error("无效参数 mode_num")
            return False

    def enable_ocr(self):
        from tools.ocr.ocr import OCR
        self.OCR = OCR()


env = Environment(1920, 1080)
logger = env.logger
axis_zoom, axis_translation, axis_change = env.axis_zoom, env.axis_translation, env.axis_change
move, click, drag, roll, roll_h = env.move, env.click, env.drag, env.roll, env.roll_h
press, keydown, keyup, key_add, wait = env.press, env.keydown, env.keyup, env.key_add, env.wait
ocr, screenshot, find_pic, find_color = env.ocr, env.screenshot, env.find_pic, env.find_color
center, click_pic, click_text = env.center, env.click_pic, env.click_text
