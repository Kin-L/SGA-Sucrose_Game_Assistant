from tools.environment import *
from task.genshin.genshin import Genshin


class Sumeru(Genshin):
    # 柽木
    def athel(self):
        self.indicate("采集：柽木×12")
        self.home()
        self.open_sub("冒险之证")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("赤金的废墟")
        click(371, 837)
        wait(800)
        self.tp_point(0)
        keydown("A")
        wait(1300)
        keyup("A")
        wait(500)
        keydown("W")
        wait(6300)
        keyup("W")
        wait(500)
        press("Z")
        wait(500)

    # 刺葵木
    def mountain_date(self):
        self.home()
        self.indicate("采集：刺葵木×12")
        self.open_sub("冒险之证")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("赤金的废墟")
        click(46, 649)
        wait(800)
        click(1084, 982)
        wait(800)
        self.tp_point(0)
        keydown("D")
        wait(4500)
        keyup("D")
        wait(300)
        keydown("W")
        wait(3600)
        keyup("W")
        wait(300)
        press("Z")
        wait(500)
        # 第二段
        self.home()
        self.open_sub("冒险之证")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("熔铁的孤塞")
        click(1009, 726)
        wait(800)
        self.tp_point(0)
        keydown("D")
        wait(6000)
        keyup("D")
        wait(300)
        keydown("W")
        wait(4000)
        keyup("W")
        wait(300)
        keydown("D")
        wait(5500)
        keyup("D")
        wait(300)
        keydown("W")
        wait(7900)
        keyup("W")
        wait(300)
        press("Z")
        wait(500)

    # 证悟木
    def adhigama(self):
        self.home()
        self.indicate("采集：证悟木×9")
        self.open_sub("冒险之证")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("缘觉塔")
        click(694, 504)
        wait(800)
        self.tp_point(0)
        press("Z")
        wait(500)

    # 业果木_辉木
    def karmaphala_bright(self):
        self.home()
        self.indicate("采集：业果木×15,辉木×12")
        self.open_sub("冒险之证")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("缘觉塔")
        click(243, 939)
        wait(800)
        self.tp_point(0)
        keydown("W")
        wait(8500)
        keyup("W")
        wait(300)
        press("Z")
        wait(300)
        keydown("S")
        wait(500)
        keyup("S")
        wait(300)
        keydown("D")
        wait(2500)
        keyup("D")
        wait(11500)
        press("Z")
        wait(500)