from tools.environment import *
from .genshin import Genshin


class Mail(Genshin):
    def genshin_mail(self):
        self.indicate("检查邮件")
        self.home()
        if find_color("red", (12, 560, 107, 648))[1]:
            click(46, 607)
            wait(2000)
            click(239, 1020)
            wait(2000)
            click(931, 1007)
            wait(2000)
            click(1843, 44)
            wait(2000)
            self.indicate("邮件领取完成")
        else:
            self.indicate("暂无邮件可领取")

