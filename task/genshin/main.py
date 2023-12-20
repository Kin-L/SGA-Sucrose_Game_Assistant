# -*- coding:gbk -*-
from tools.environment import *
import traceback
import os
from .team import Team
from .dispatch import Dispatch
from .transformer import Transformer
from .crystalfly import CatchFly
from .condensed import Condensed
from .rambler import Rambler
from .cut_tree.main import CutTree
from .mail import Mail


class TaskGenshin(Team, Dispatch, Transformer, CatchFly, Condensed, Rambler, Mail, CutTree):
    def __init__(self):
        super().__init__()

    def genshin_start(self, task: type[dir]):
        self.task = task
        # print(self.task)
        self.genshin_launch()
        env.enable_ocr()
        try:
            self.genshin_log(60)
            _list = self.task["����"]
            if _list[0]:
                self.genshin_team()
                self.indicate("�����л���ɡ�")
            if _list[1]:
                self.genshin_dispatch()
                self.indicate("̽����ǲ�����ɡ�")
            if _list[2]:
                self.genshin_transformer()
            if _list[3]:
                self.genshin_catch_fly()
            if _list[4]:
                self.genshin_make_condensed()
            if _list[5]:
                self.genshin_rambler()
            if _list[6]:
                self.genshin_mail()
            if _list[7]:
                self.genshin_cut_tree()
                self.indicate("��ľ��ɡ�")
            self.indicate("ִ����ɡ�")
            env.OCR.disable()
        except:
            self.indicate("ԭ������ִ���쳣")
            logger.error("����ִ���쳣��\n%s" % traceback.format_exc())
        if self.task["����"][1]:
            self.indicate("���Թر���Ϸ��")
            s, n = 15, 2
            if env.soft.kill(s, n):
                self.indicate("��Ϸ�ѹرա�")
            else:
                self.indicate(f"error����Ϸ�رճ�ʱ��{s * n}s����")
        
    def genshin_launch(self):
        # ·������
        env.set_soft(None, (0, "UnityWndClass", "ԭ��"))
        _path = self.task["����"][1]
        # print(_path)
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "YuanShen.exe":
                env.soft.set_path(_path)
            elif name == "launcher.exe":
                path = dire + "/Genshin Impact Game/YuanShen.exe"
                if os.path.isfile(path):
                    env.soft.set_path(path)
                else:
                    self.indicate("ԭ����Ч����·����")
                    self.kill(3)
            else:
                self.indicate("ԭ����Ч����·����")
                self.kill(3)
        else:
            self.indicate("ԭ����Ч����·����")
            self.kill(3)
        # ������Ϸ
        cond = env.soft.run()
        if cond == 1:
            self.indicate("��Ϸ����������")
            wait(1000)
        elif cond == 2:
            self.indicate("��Ϸ�����ɹ���")
            self.indicate("�ȴ����أ�10���ʼʶ����Ϸ״̬��")
            wait(10000)
        elif cond == 0:
            self.indicate("��Ϸ������ʱ��")
            self.kill(3)
        for i in range(10):
            env.soft.foreground()
            wait(1000)
            if env.mode(1):
                break
            else:
                env.soft.foreground()
                wait(2000)
        
    def genshin_log(self, second: int):
        # ��¼&������Ϸ
        self.indicate("��ʼʶ����Ϸ״̬��")
        server = self.task["����"][0]
        for i in range(second):
            sc = screenshot()
            if server == 0:
                if ocr((897, 989, 1027, 1048))[0] == "�������":
                    server = 2
                    click(930, 630)
                    self.indicate("���š�")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if find_pic(r"assets\genshin\picture\login2.png", (863, 370, 1059, 467), sc)[1] >= 0.6:
                    click(953, 659)
                    self.indicate("��¼B���˺š�")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
                if ocr((897, 989, 1027, 1048))[0] == "�������":
                    server = 2
                    click(930, 630)
                    self.indicate("���š�")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            if find_pic(r"assets\genshin\picture\sighin.png", (865, 240, 1060, 470), sc)[1] >= 0.6:
                click(930, 850)
                wait(800)
                click(930, 850)
                wait(100)
                click(930, 850)
                wait(1000)
                click(930, 850)
                wait(800)
                self.indicate("�����¿���ȡ�ɹ���")
                os.remove(sc)
                sc = screenshot()
            if find_pic(r"assets\genshin\picture\world.png", (57, 998, 179, 1075), sc)[1] >= 0.6:
                self.indicate("���ص����硣")
                os.remove(sc)
                click(509, 313)
                wait(300)
                click(509, 313)
                wait(300)
                break
            if find_pic(r"assets\genshin\picture\home\home.png", (0, 0, 97, 88), sc)[1] >= 0.6:
                self.indicate("���ص������档")
                os.remove(sc)
                click(509, 313)
                wait(300)
                click(509, 313)
                wait(300)
                break
            os.remove(sc)
            if i == second - 1:
                self.indicate(f"��¼��ʱ����{second * 2}s��")
                self.kill(3)
            wait(2000)
            

if __name__ == '__main__':
    logger.enable_console()
    logger.hr("��ӭʹ�� ɰ�Ǵ���v1.1\n"
              "https://github.com/Kin-L/SGA-Sucrose_Game_Assistant\n"
              "�˳���Ϊ��ѿ�Դ��Ŀ ����㸶��Ǯ�������˿�", 0)
    pass
