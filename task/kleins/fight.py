from tools.environment import *
from ..default_task import Task
import os


class Fight(Task):
    def __init__(self):
        super().__init__()
        
    def kleins_fight(self):
        self.indicate("开始检查：作战。")
        text = ocr((1675, 397, 1802, 439))[0]
        if (":" in text) or ("：" in text):
            self.indicate("重游进行中，不能再次开启作战。")
            click(288, 78)
            wait(1500)
            self.indicate("检查完成：作战。")
            return False
        elif text == "完成重游":
            click(1739, 420)
            self.indicate("重游完成，领取重游奖励。")
            wait(2500)
            while 1:
                sc = screenshot()
                if ocr((827, 134, 1088, 262), sc)[0] == "向导等级":
                    self.indicate("等级提升！")
                    click(1282, 690)
                    os.remove(sc)
                    sc = screenshot()
                if ocr((1703, 50, 1832, 97), sc)[0] == "再次重游":
                    wait(500)
                    os.remove(sc)
                    if self.task["作战"][0]:
                        click(1744, 80)
                        wait(1800)
                        sc = screenshot()
                        ((x1, y1), sim1) = find_pic(r"assets\kleins\picture\fight\add.png",
                                                    (1100, 335, 1900, 983), sc)
                        ((x2, y2), sim2) = find_pic(r"assets\kleins\picture\fight\start.png",
                                                    (960, 540, 1920, 1080), sc, True)
                        if sim1 >= 0.6 and sim2 >= 0.6:
                            click(x1 + 120, y1)
                            wait(1000)
                            click(x2, y2)
                            wait(1000)
                            if find_pic(r"assets\kleins\picture\fight\lack.png", (1085, 716, 1256, 846))[1] > 0.75:
                                self.indicate("能源不足。")
                                click(761, 781)
                                wait(1000)
                            else:
                                self.indicate("开始重复上次作战。")
                                self.indicate("检查完成：作战。")
                            click(288, 78)
                            wait(1500)
                        else:
                            self.indicate("(不能识别的界面)")
                            self.indicate("检查完成：作战。")
                            click(288, 78)
                            wait(1500)
                        return True
                    else:
                        click(971, 930)
                        wait(800)
                    break
                os.remove(sc)
                wait(1000)
        else:
            self.indicate("作战空闲中。")
            if self.task["作战"][1]:
                self.indicate("没有再次重游目标。")
        click(1446, 359)
        wait(1500)
        click(737, 1028)
        wait(1500)
        num = self.task["作战"][1]
        x, y = [(519, 545), (885, 554), (1248, 534)][num]
        click(x, y)
        wait(2000)
        click(786, 555)
        wait(1500)
        click(1077, 856)
        wait(1000)
        click(1525, 549)
        wait(500)
        click(1458, 816)
        wait(1000)
        if find_pic(r"assets\kleins\picture\fight\lack.png", (1085, 716, 1256, 846))[1] >= 0.75:
            self.indicate("能源不足。")
            click(761, 781)
            wait(1000)
        else:
            self.indicate("开始作战：获取 "+["格", "风物志", "节"][num])
        click(288, 78)
        wait(1500)
        self.indicate("检查完成：作战。")
