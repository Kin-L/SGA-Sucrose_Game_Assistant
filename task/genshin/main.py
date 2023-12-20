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
            _list = self.task["功能"]
            if _list[0]:
                self.genshin_team()
                self.indicate("队伍切换完成。")
            if _list[1]:
                self.genshin_dispatch()
                self.indicate("探索派遣检查完成。")
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
                self.indicate("伐木完成。")
            self.indicate("执行完成。")
            env.OCR.disable()
        except:
            self.indicate("原神任务执行异常")
            logger.error("任务执行异常：\n%s" % traceback.format_exc())
        if self.task["运行"][1]:
            self.indicate("尝试关闭游戏。")
            s, n = 15, 2
            if env.soft.kill(s, n):
                self.indicate("游戏已关闭。")
            else:
                self.indicate(f"error：游戏关闭超时（{s * n}s）。")
        
    def genshin_launch(self):
        # 路径修正
        env.set_soft(None, (0, "UnityWndClass", "原神"))
        _path = self.task["启动"][1]
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
                    self.indicate("原神，无效启动路径。")
                    self.kill(3)
            else:
                self.indicate("原神，无效启动路径。")
                self.kill(3)
        else:
            self.indicate("原神，无效启动路径。")
            self.kill(3)
        # 启动游戏
        cond = env.soft.run()
        if cond == 1:
            self.indicate("游戏早已启动。")
            wait(1000)
        elif cond == 2:
            self.indicate("游戏启动成功。")
            self.indicate("等待加载，10秒后开始识别游戏状态。")
            wait(10000)
        elif cond == 0:
            self.indicate("游戏启动超时。")
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
        # 登录&进入游戏
        self.indicate("开始识别游戏状态。")
        server = self.task["启动"][0]
        for i in range(second):
            sc = screenshot()
            if server == 0:
                if ocr((897, 989, 1027, 1048))[0] == "点击进入":
                    server = 2
                    click(930, 630)
                    self.indicate("开门。")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if find_pic(r"assets\genshin\picture\login2.png", (863, 370, 1059, 467), sc)[1] >= 0.6:
                    click(953, 659)
                    self.indicate("登录B服账号。")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
                if ocr((897, 989, 1027, 1048))[0] == "点击进入":
                    server = 2
                    click(930, 630)
                    self.indicate("开门。")
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
                self.indicate("今日月卡领取成功。")
                os.remove(sc)
                sc = screenshot()
            if find_pic(r"assets\genshin\picture\world.png", (57, 998, 179, 1075), sc)[1] >= 0.6:
                self.indicate("加载到世界。")
                os.remove(sc)
                click(509, 313)
                wait(300)
                click(509, 313)
                wait(300)
                break
            if find_pic(r"assets\genshin\picture\home\home.png", (0, 0, 97, 88), sc)[1] >= 0.6:
                self.indicate("加载到主界面。")
                os.remove(sc)
                click(509, 313)
                wait(300)
                click(509, 313)
                wait(300)
                break
            os.remove(sc)
            if i == second - 1:
                self.indicate(f"登录超时。（{second * 2}s）")
                self.kill(3)
            wait(2000)
            

if __name__ == '__main__':
    logger.enable_console()
    logger.hr("欢迎使用 砂糖代理v1.1\n"
              "https://github.com/Kin-L/SGA-Sucrose_Game_Assistant\n"
              "此程序为免费开源项目 如果你付了钱请立刻退款", 0)
    pass
