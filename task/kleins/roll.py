from tools.environment import *
from ..default_task import Task
import os
import json


class Roll(Task):
    def __init__(self):
        super().__init__()

    def kleins_get_roll(self):
        self.indicate("开始获取抽卡记录")
        click(1698, 692)
        for i in range(10):
            wait(1000)
            if click_text("联络记录", (294, 994, 428, 1046)):
                break
            elif i < 9:
                wait(1000)
            else:
                self.indicate("error:\n  获取抽卡记录,等待超时")
                self.kill(3)
        wait(1200)
        with open("personal/kleins/roll/history.json", 'r', encoding='utf-8') as m:
            current = json.load(m)
        _list = [360, 407, 452, 498, 543, 589, 634, 680, 725, 771]
        for i in ["定向联络", "常态联络", "初始联络"]:
            click(1385, 219)
            wait(500)
            if click_text(i, (1200, 182, 1346, 321)):
                wait(500)
            else:
                self.indicate("error:\n  获取抽卡记录,界面识别异常")
                self.kill(3)
            _l = current[i]
            _nl = []
            for p in range(30):
                sc = screenshot()
                for y in _list:
                    time = ocr((544, y, 798, y + 37), sc)[0]
                    banner = ocr((836, y, 1011, y + 37), sc)[0]
                    rare = ocr((1070, y, 1125, y + 37), sc)[0]
                    name = ocr((1219, y, 1362, y + 37), sc)[0]
                    if ["", "", "", ""] == [time, banner, rare, name]:
                        print(time, banner, rare, name)
                        break
                    _line = [time.strip(" "), banner.rstrip(r"\u3000").strip(" "),
                             rare.strip(" "), name.rstrip(r"\u3000").strip(" ")]
                    if _line not in _l:
                        _nl = [_line] + _nl
                _text = ocr((903, 839, 1018, 884), sc)[0]
                os.remove(sc)
                _num = int(_text.split("/")[-1])
                if p+1 == _num:
                    break
                else:
                    click(1042, 861)
                    wait(500)
            current[i] = _l+_nl
        with open("personal/kleins/roll/history.json", 'w', encoding='utf-8') as x:
            json.dump(current, x, ensure_ascii=False, indent=1)
        click(1753, 182)
        wait(800)
        click(153, 68)
        wait(2000)
        self.indicate("获取抽卡记录完成")
