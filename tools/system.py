# -*- coding:gbk -*-
from pyautogui import press as papress
from sys import exit
from pyuac import isUserAdmin, runAsAdmin
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import windll
from win10toast import ToastNotifier
from subprocess import run
from win32api import MessageBox
from win32con import MB_OK
# pyuic5 -o SGA_demo.py SGA_demo.ui
import win32com


# windows��ʾ
def notify(title, massage):
    toaster = ToastNotifier()
    toaster.show_toast(title, massage,
                       icon_path="assets/main_window/ui/ico/SGA.ico",
                       duration=5,
                       threaded=True)


def message_box(text):
    MessageBox(0, text, "ɰ�Ǵ���", MB_OK)


# ��ѯ����״̬
def get_mute():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMute()


# �л�����״̬
def change_mute():
    papress('volumemute')


# Ϩ��
def screen_off():
    power_off = 2
    windll.user32.PostMessageW(0xffff, 0x0112, 0xF170, power_off)
    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe', 'USER32', '', 5)


# cmd����
def cmd_run(cmd_str):
    run(cmd_str, shell=True)


# ��ȡ�������źͷֱ���
def get_resolution_zoom():
    from ctypes import windll
    user32 = windll.user32
    now_wid = user32.GetSystemMetrics(0)
    now_hig = user32.GetSystemMetrics(1)
    user32.SetProcessDPIAware()
    ori_wid = user32.GetSystemMetrics(0)
    ori_hig = user32.GetSystemMetrics(1)
    return (ori_wid, ori_hig), (now_wid, now_hig), round(ori_wid / now_wid, 2)


class System:
    def __init__(self):
        # ������־
        from tools.logger.log import Logger
        self.logger = Logger().get_logger()
        # ��������
        self.OCR = None
        self.workdir = None
        self.resolution_compile = None
        self.frame, self.zoom = None, None
        self.soft = type[classmethod]
        # ��ȡ����ǰ��ֱ��ʣ����ű���
        self.resolution_origin = None
        self.resolution_now = None
        self.zoom_desktop = None

    def set_soft(self, path=None, mode_cls_tit=list[0, None, None]):
        from .software import Software
        self.soft = Software(self.resolution_compile)
        _pb = path is None
        _pc = mode_cls_tit[1:] == (None, None)
        if _pb and _pc:
            print("set_soft ��Ч���á�")
        else:
            if not _pb:
                self.soft.set_path(path)
            self.soft.set_hwnd_find(mode_cls_tit[0], mode_cls_tit[1], mode_cls_tit[2])

    # ��׼�ֱ���
    def set_compile(self, wide, high):
        self.resolution_compile = (wide, high)

    def get_workdir(self):
        from os import getcwd
        self.workdir = getcwd()

    # ��ȡ����ԱȨ��
    def get_user_admin(self):
        if isUserAdmin():
            self.logger.debug("����ԱȨ��������")
        else:
            self.logger.debug("�ǹ���ԱȨ�����������Ի�ȡ����ԱȨ�ޡ�")
            runAsAdmin(wait=False)
            if isUserAdmin():
                self.logger.debug("�ɹ���ȡ����ԱȨ�ޡ�")
            else:
                self.logger.debug("��ȡ����ԱȨ��ʧ�ܡ�")
                self.logger.debug("�˳���")
                exit(1)

    # ����������
    def axis_zoom(self, x, y):
        if self.zoom != 1:
            x, y = int(x * self.zoom), int(y * self.zoom)
        return x, y

    # �������ƶ�
    def axis_translation(self, x, y):
        if self.frame != (0, 0):
            x, y = x + self.frame[0], y + self.frame[1]
        return x, y

    # ���������Ų��ƶ�
    def axis_change(self, x, y):
        if self.zoom != 1:
            x, y = int(x * self.zoom), int(y * self.zoom)
        if self.frame != (0, 0):
            x, y = x + self.frame[0], y + self.frame[1]
        return x, y


if __name__ == '__main__':
    pass
    # frame, zoom, Ocr, logger = None, None, None, None
    # env = Environment(1920, 1080)
    # env.soft.set_hwnd_find(True, ("UnityWndClass", "ԭ��"))
