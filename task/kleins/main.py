# -*- coding:gbk -*-
from tools.environment import *
from ..default_task import Task
from .fight import Fight
from .dispatch import Dispatch
from .review import Review
from .market import Market
from .recruit import Recruit
from .reward import Reward
from .network import Network
from .mail import Mail
from .roll import Roll
import os
import traceback


class TaskKleins(Fight, Dispatch, Review, Market, Recruit, Reward, Network, Mail, Roll):
    def __init__(self):
        super().__init__()

    def kleins_start(self, task: type[dir]):
        self.task = task
        # print(self.task)
        self.kleins_launch()
        env.enable_ocr()
        try:
            self.kleins_log(60)
            # 触发舍友互动
            click(969, 374)
            wait(500)
            click(969, 374)
            wait(500)
            _list = self.task["功能"]
            if _list[0]:
                self.kleins_fight()
            if _list[1]:
                self.kleins_dispatch()
            if _list[2]:
                self.kleins_review()
            if _list[3]:
                self.kleins_get_market()
            if _list[4]:
                self.kleins_recruit()
            if _list[5]:
                self.kleins_reward()
            if _list[6]:
                self.kleins_market_network()
            if _list[7]:
                self.kleins_get_mail()
            if _list[8]:
                self.kleins_get_roll()
            self.indicate("执行完成")
            env.OCR.disable()
        except:
            self.indicate("原神任务执行异常")
            logger.error("任务执行异常：\n%s" % traceback.format_exc())
        if self.task["运行"][1]:
            self.indicate("尝试关闭游戏")
            s, n = 15, 2
            if env.soft.kill(s, n):
                self.indicate("游戏已关闭")
            else:
                self.indicate(f"error:游戏关闭超时（{s * n}s）")

    def kleins_launch(self):
        # 路径修正
        env.set_soft(None, (0, "UnityWndClass", "环行旅舍"))
        _path = self.task["启动"][1]
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "环行旅舍.exe":
                env.soft.set_path(_path)
            elif name == "kleins.exe":
                path = dire + "/Games/环行旅舍.exe"
                if os.path.isfile(path):
                    env.soft.set_path(path)
                else:
                    self.indicate("环行旅舍，无效启动路径")
                    self.kill(3)
            else:
                self.indicate("环行旅舍，无效启动路径")
                self.kill(3)
        else:
            self.indicate("环行旅舍，无效启动路径")
            self.kill(3)
        # 启动游戏
        cond = env.soft.run()
        if cond == 1:
            self.indicate("游戏启动成功")
            self.indicate("等待加载,10秒后开始识别游戏状态")
            wait(1000)
            env.soft.foreground()
            wait(9000)
        elif cond == 2:
            self.indicate("游戏早已启动")
            env.soft.foreground()
            wait(1000)
        elif cond == 0:
            self.indicate("游戏启动超时")
            self.kill(3)
        env.mode(1)

    def kleins_log(self, second: int):
        # 登录&进入游戏
        self.indicate("开始识别游戏状态")
        server = self.task["启动"][0]
        for i in range(second):
            sc = screenshot()
            if server == 0:
                if find_pic("assets/kleins/picture/startgame1.png",
                            (835, 582, 1093, 695), sc)[1] >= 0.6:
                    wait(300)
                    click(930, 630)
                    self.indicate("登录游戏")
                    wait(5000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if find_pic("assets/kleins/picture/startgame2.png",
                            (830, 582, 1093, 695), sc)[1] >= 0.6:
                    wait(300)
                    click(960, 633)
                    self.indicate("登录账号")
                    wait(1500)
                    os.remove(sc)
                    sc = screenshot()
                if find_color("blue", (910, 658, 992, 704))[0]:
                    wait(300)
                    click(958, 679)
                    self.indicate("登录游戏")
                    wait(5000)
                    os.remove(sc)
                    sc = screenshot()
            if ocr((832, 211, 1090, 313), sc)[0] == "签到奖励":  # 签到奖励
                click(1469, 551)
                wait(1500)
                click(1789, 120)
                self.indicate("签到成功")
                wait(1000)
                os.remove(sc)
                sc = screenshot()
            (x, y), sim = find_pic("assets/kleins/picture/close/close2.png", search_path=sc)
            if sim >= 0.6:
                click(x, y)
                wait(1500)
                os.remove(sc)
                sc = screenshot()
            if find_pic("assets/kleins/picture/home.png", (1739, 37, 1814, 98), sc)[1] >= 0.7:
                wait(1500)
                os.remove(sc)
                sc = screenshot()
                if find_pic("assets/kleins/picture/home.png", (1739, 37, 1814, 98), sc)[1] >= 0.7:
                    self.indicate("加载到主界面")
                    os.remove(sc)
                    break
            os.remove(sc)
            wait(1500)


if __name__ == '__main__':
    pass
