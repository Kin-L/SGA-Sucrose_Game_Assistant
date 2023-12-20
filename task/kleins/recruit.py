from tools.environment import *
from ..default_task import Task
import os
import time
import shutil


class Recruit(Task):
    def __init__(self):
        super().__init__()

    def kleins_recruit(self):
        self.indicate("开始检查:舍友访募")
        click(1469, 697)
        wait(2000)
        _vf, _cf = True, self.task["访募"][0]
        _z1 = [(197, 281, 351, 323), (197, 392, 351, 431), (197, 499, 351, 540)]
        _z2 = [(171, 234, 379, 338), (174, 346, 378, 445), (172, 455, 377, 556)]
        for n in range(3):
            x, y = [(129, 290), (126, 395), (131, 501)][n]
            if ocr(_z1[n])[0] == "访募完成":
                self.indicate("访募%s:完成尝试领取" % (n+1))
                self.receive_recruit(x, y)
            while 1:
                if find_pic("assets/kleins/picture/recruit/new.png", _z2[n])[1] >= 0.6:
                    self.indicate("访募%s:空闲尝试开始访募" % (n+1))
                    click(x, y)
                    wait(1000)
                    if find_color("2F2C30", (480, 253, 499, 273))[0]:
                        self.indicate("普通访募")
                        _vf = self.create_recruit()
                        if (not _cf) or (not _vf):
                            break
                        else:
                            self.indicate("尝试使用高速显影剂")
                            click(743, 811)
                            wait(1000)
                            if find_pic("assets/kleins/picture/recruit/lack.png", (903, 70, 1021, 141))[1] >= 0.6:
                                self.indicate("缺少高速显影剂")
                                _cf = False
                            else:
                                self.indicate("高速显影剂使用成功")
                                self.receive_recruit(x, y)
                    else:
                        if find_color("purple", (480, 253, 499, 273))[0]:
                            self.indicate("发现必出SR访募")
                        elif find_color("orange+yellow", (480, 253, 499, 273))[0]:
                            self.indicate("发现必出SSR访募!")
                        break
                else:
                    self.indicate("访募%s:进行中" % (n+1))
                    break
            if not _vf:
                break
        click(296, 75)
        wait(1000)
        self.indicate("检查完成:舍友访募")

    def create_recruit(self):
        for i in range(self.task["访募"][1]):
            click(990, 626)
            wait(100)
        click(871, 818)
        wait(800)
        if find_pic("assets/kleins/picture/recruit/lack.png", (903, 70, 1021, 141))[1] >= 0.6:
            self.indicate("缺少格或外显记录")
            return False
        else:
            self.indicate("舍友访募开始")
            return True
        
    def receive_recruit(self, x, y):
        click(x, y)
        wait(2500)
        sc = screenshot()
        nv = find_pic("assets/kleins/picture/recruit/N.png", (252, 444, 421, 553), sc)[1]
        rv = find_pic("assets/kleins/picture/recruit/R.png", (252, 444, 421, 553), sc)[1]
        srv = find_pic("assets/kleins/picture/recruit/SR.png", (252, 444, 421, 553), sc)[1]
        rrv = find_pic("assets/kleins/picture/recruit/SSR.png", (252, 444, 468, 553), sc)[1]
        _name = ocr((268, 513, 651, 600), sc)[0].rstrip(" ")
        _list = (nv, rv, srv, rrv)
        max_val = max(_list)
        if max_val:
            now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            max_index = _list.index(max_val)
            if max_index == 0:
                self.indicate(f"访募到N卡 {_name}")
            elif max_index == 1:
                self.indicate(f"访募到R卡 {_name}")
            else:
                shutil.copyfile(sc, f"personal/kleins/recruit/{now_time}.png")
                if max_index == 2:
                    self.indicate("访募到SR卡 {_name}\n  可在文件夹“personal/kleins/recruit”中查看")
                else:
                    self.indicate("访募到SSR卡! {_name}\n  可在文件夹“personal/kleins/recruit”中查看")
            f = open("personal/kleins/recruit/history.txt", 'a+', encoding='utf-8')
            r = ["N", "R", "SR", "SSR"][max_index]
            f.write(f"{now_time}  {r}  {_name}\n")
            f.close()
        else:
            now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            shutil.copyfile(sc, f"personal/kleins/recruit/{now_time}.png")
            self.indicate(f"error:舍友访募未知错误 ({now_time}.png)")
        os.remove(sc)
        click(273, 903)
        wait(1500)
        click(273, 903)
        wait(1500)
