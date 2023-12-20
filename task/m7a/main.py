# -*- coding:gbk -*-
from ..default_task import Task
from tools.environment import *
from tools.software import get_pid, close
import os
import yaml


class TaskM7A(Task):
    def __init__(self):
        super().__init__()

    def m7a_start(self, task: type[dir]):
        self.task = task
        # print(self.task)
        # MAA�رղ���ʼ��
        pid = get_pid("March7th Assistant.exe")
        if pid is not None:
            self.indicate("����������������,׼������")
            close(pid)
        _path = self.task["����"]
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "March7th Assistant.exe":
                pass
            elif name == "March7th Launcher.exe":
                _path = dire + "/March7th Launcher.exe"
            else:
                self.indicate("����������,��Ч����·��")
                self.kill(3)
        else:
            self.indicate("����������,��Ч����·��")
            self.kill(3)
        env.set_soft(None, [True, "ConsoleWindowClass", "m7a"])
        env.soft.set_path(_path)
        # �޸�M7A��������
        config_yaml = os.path.split(_path)[0] + "/config.yaml"
        with open(config_yaml, 'r', encoding='utf-8') as f:
            _dir = yaml.load(stream=f, Loader=yaml.FullLoader)
        current = _dir["after_finish"]
        _dir["after_finish"] = "Exit"
        with open(config_yaml, 'w', encoding='utf-8', ) as f:
            yaml.dump(_dir, f, encoding='utf-8', allow_unicode=True)
        # ����-����
        _run = env.soft.run(fls=False, tit="m7a")
        if _run:
            self.indicate("����������������...")
            _dire = os.path.split(_path)[0] + "/logs/"
            _name = os.listdir(_dire)[-1]
            _path = _dire + _name
            while 1:
                wait(10000)
                f = open(_path, encoding='utf-8')
                if "��Ϸ�˳��ɹ�" in f.readlines()[-1]:
                    break
            # env.soft.kill()
            self.indicate("�����������������")
        else:
            self.indicate("��������������ʧ��")
            return False
        # �޸Ļ�M7A��������
        with open(config_yaml, 'r', encoding='utf-8') as f:
            _dir = yaml.load(stream=f, Loader=yaml.FullLoader)
        _dir["after_finish"] = current
        with open(config_yaml, 'w', encoding='utf-8', ) as f:
            yaml.dump(_dir, f, encoding='utf-8', allow_unicode=True)


if __name__ == '__main__':
    pass
