# -*- coding:gbk -*-
import os
from time import sleep
from win32con import PROCESS_ALL_ACCESS, SW_RESTORE
from win32gui import (FindWindow, EnumWindows, GetClassName, GetWindowText,
                      GetWindowRect, IsIconic, ShowWindow, SetForegroundWindow)
from psutil import process_iter
from signal import SIGTERM
from subprocess import run


# ��exe���ƻ�ȡpid
def get_pid(name):
    pids = process_iter()
    for pid in pids:
        if pid.name() == name:
            return pid.pid


# �����رս���
def close(pid, sig=SIGTERM):
    os.kill(pid, sig)


# ��ȡ����pid��·��
def get_process_name(hwnd):
    from win32process import GetWindowThreadProcessId, GetModuleFileNameEx
    from win32api import OpenProcess
    pid = GetWindowThreadProcessId(hwnd)[1]
    mypy_proc = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    path = GetModuleFileNameEx(mypy_proc, 0)
    return pid, path


# ������/������Ҵ��ھ��
def find_hwnd(mode_cls_tit):
    mode, cls, tit = mode_cls_tit
    if mode:
        return FindWindow(cls, tit)
    else:
        hwnd_list = []
        EnumWindows(lambda _hwnd, _hwnd_list: _hwnd_list.append(_hwnd), hwnd_list)
        for hwnd in hwnd_list:
            class_name = GetClassName(hwnd)
            title = GetWindowText(hwnd)
            if cls in class_name and tit in title:
                return hwnd


class Software:
    def __init__(self, compile_resolution):
        self.compile_resolution = compile_resolution
        self.path, self.dir, self.name = None, None, None
        self.pid, self.hwnd = None, None
        self.mode_cls_tit = None
        self.frame, self.wide, self.high, self.zoom = None, None, None, None

    def set_path(self, path: str):
        if os.path.isfile(path):
            self.path, [self.dir, self.name] = path, os.path.split(path)
            return True
        else:
            print("error:Software ��Ч·����")
            return False

    def set_pid(self, hwnd):
        if hwnd:
            self.pid, self.path = get_process_name(hwnd)
            self.dir, self.name = os.path.split(self.path)
        else:
            print("error:Software ����δ������")

    def set_hwnd_find(self, mode, cls, tit):
        if mode == 0:  # ��ȷ����
            self.mode_cls_tit = [True, cls, tit]
        elif mode == 1:
            self.mode_cls_tit = [False, cls, tit]
        elif mode == 2:  # ͨ��·������
            if self.path is not None:
                if self.name == "YuanShen.exe":
                    self.mode_cls_tit = [True, "UnityWndClass", "ԭ��"]
                elif self.name == "��������.exe":
                    self.mode_cls_tit = [True, "UnityWndClass", "��������"]
                elif self.name == "MAA.exe":
                    self.mode_cls_tit = [False, "HwndWrapper[MAA.exe", "MAA"]
                elif self.name == "March7th Assistant.exe":
                    self.mode_cls_tit = [True, "ConsoleWindowClass", ""]
                else:
                    print("error:Software ��֧���Զ�ʶ��������")
            else:
                print("error:Software ��Ч·����")

    def run(self, second=30, num=2, fls=True, tit=None):
        if self.path is None:
            print("error:Software ��Ҫ����������·����")
            return 0
        else:
            if self.hwnd:
                print("�������������")
                return 1
            else:
                if tit is None:
                    cmd = f"start \"\" \"{self.path}\""
                else:
                    cmd = f"start \"{tit}\" \"{self.path}\""
                if fls:
                    cmd = cmd + " -popupwindow"
                for n in range(num):
                    # os.startfile(self.path)
                    run(cmd, shell=True)
                    # run("start /d \"" + self.dir + "\" " + self.name + " -popupwindow", shell=True)
                    for i in range(second):
                        sleep(1)
                        self.hwnd = find_hwnd(self.mode_cls_tit)
                        if self.hwnd:
                            self.set_pid(self.hwnd)
                            print("��������ɹ���")
                            return 2
                print(f"error:������ʱ��({second*num}s)")
                return 0

    def kill(self, second=10, num=2):
        if self.hwnd:
            for n in range(num):
                close(self.pid)
                for i in range(second):
                    sleep(1)
                    self.hwnd = find_hwnd(self.mode_cls_tit)
                    if not self.hwnd:
                        print("����رճɹ���")
                        return True
            print(f"error:�رճ�ʱ��({second*num}s)")
            return False
        else:
            print("�����δ������")

    def get_window_information(self):
        if self.hwnd:
            f = GetWindowRect(self.hwnd)
            w, h = f[2] - f[0], f[3] - f[1]
            if (1.7 <= round(w / h, 3) <= 1.8) and (664 <= h <= 2160):
                x_zoom, y_zoom = w / self.compile_resolution[0], h / self.compile_resolution[1]
                self.zoom = min(x_zoom, y_zoom)
                self.frame, self.wide, self.high = f, w, h
                return True
            else:
                print(f"������ķֱ���: {self.wide} �� {self.high}")
                self.zoom = None
                return False

        else:
            print("error:�����δ������")
            return False

    def foreground(self):
        if IsIconic(self.hwnd):
            ShowWindow(self.hwnd, SW_RESTORE)
        else:
            SetForegroundWindow(self.hwnd)
