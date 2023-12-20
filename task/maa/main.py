# -*- coding:gbk -*-
import json
from ..default_task import Task
from tools.environment import *
from tools.software import get_pid, close
import os


class TaskMAA(Task):
    def __init__(self):
        super().__init__()

    def maa_start(self, task: type[dir]):
        self.task = task
        # print(self.task)
        # MAA关闭并初始化
        pid = get_pid("MAA.exe")
        if pid is not None:
            self.indicate("MAA早已启动,进行重启")
            close(pid)
        env.set_soft(None, (1, "HwndWrapper[MAA.exe", "MAA"))
        _path = self.task["启动"]
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "MAA.exe":
                env.soft.set_path(_path)
            else:
                self.indicate("MAA,无效启动路径")
                self.kill(3)
        else:
            self.indicate("MAA,无效启动路径")
            self.kill(3)
        # 修改MAA运行设置
        gui_path = os.path.split(_path)[0] + "/config/gui.json"
        with open(gui_path, 'r', encoding='utf-8') as g:
            maa = json.load(g)
        import copy
        setcurrent = self.task["配置"][0]
        _sga = copy.deepcopy(maa["Configurations"][setcurrent])
        if self.task["运行"][1]:
            after_completed = "ExitEmulatorAndSelf"
        else:
            after_completed = "ExitSelf"
        current = maa["Current"]
        _sga["Start.EndsWithScript"] = env.workdir + "/assets/maa/bat_scr/create.bat"
        _sga["MainFunction.ActionAfterCompleted"] = after_completed
        _sga["Start.RunDirectly"] = "True"
        maa["Configurations"]["SGA-cache"] = _sga
        maa["Current"] = "SGA-cache"
        with open(gui_path, 'w', encoding='utf-8') as g:
            json.dump(maa, g, ensure_ascii=False, indent=1)
        _f = env.workdir + "/cache/maa_complete.txt"
        if os.path.exists(_f):
            os.remove(_f)
        env.soft.run()
        self.indicate("MAA运行中...")
        # 运行-结束
        while 1:
            wait(10000)
            if os.path.exists(_f):
                os.remove(_f)
                break
        with open(gui_path, 'r', encoding='utf-8') as g:
            maa = json.load(g)
        maa["Current"] = current
        with open(gui_path, 'w', encoding='utf-8') as g:
            json.dump(maa, g, ensure_ascii=False, indent=1)
        self.indicate("MAA运行完成")


if __name__ == '__main__':
    pass
