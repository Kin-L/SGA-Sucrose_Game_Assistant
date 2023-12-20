from .time_window import TimerWindow
from PyQt5.QtCore import QTime


class Timer(TimerWindow):
    def __init__(self, widget, location):
        super().__init__(widget, location)
        self.add.clicked.connect(lambda: self.item_change(True))
        self.deduce.clicked.connect(lambda: self.item_change(False))

    def item_change(self, add):
        if add:
            if self.time_item < 10:
                self.time_item += 1
                self.widget.setFixedHeight(40 * self.time_item)
            else:
                print("条目数达上限：10", self.time_item)
        else:
            if self.time_item > 3:
                self.time_item -= 1
                self.widget.setFixedHeight(40 * self.time_item)
            else:
                print("条目数达下限：3", self.time_item)

    def add_items(self, filelist):
        # 加载已有方案选项
        self.text0.addItems(filelist)
        self.text1.addItems(filelist)
        self.text2.addItems(filelist)
        self.text3.addItems(filelist)
        self.text4.addItems(filelist)
        self.text5.addItems(filelist)
        self.text6.addItems(filelist)
        self.text7.addItems(filelist)
        self.text8.addItems(filelist)
        self.text9.addItems(filelist)

    def load_set(self, timer_dir):
        # 加载定时设置
        self.time_item = timer_dir["item_num"]
        self.widget.setFixedHeight(40 * self.time_item)
        _dir = timer_dir["execute"]
        self.execute0.setCurrentIndex(_dir[0])
        self.execute1.setCurrentIndex(_dir[1])
        self.execute2.setCurrentIndex(_dir[2])
        self.execute3.setCurrentIndex(_dir[3])
        self.execute4.setCurrentIndex(_dir[4])
        self.execute5.setCurrentIndex(_dir[5])
        self.execute6.setCurrentIndex(_dir[6])
        self.execute7.setCurrentIndex(_dir[7])
        self.execute8.setCurrentIndex(_dir[8])
        self.execute9.setCurrentIndex(_dir[9])
        _dir = timer_dir["time"]
        self.timer0.setTime(QTime.fromString(_dir[0]))
        self.timer1.setTime(QTime.fromString(_dir[1]))
        self.timer2.setTime(QTime.fromString(_dir[2]))
        self.timer3.setTime(QTime.fromString(_dir[3]))
        self.timer4.setTime(QTime.fromString(_dir[4]))
        self.timer5.setTime(QTime.fromString(_dir[5]))
        self.timer6.setTime(QTime.fromString(_dir[6]))
        self.timer7.setTime(QTime.fromString(_dir[7]))
        self.timer8.setTime(QTime.fromString(_dir[8]))
        self.timer9.setTime(QTime.fromString(_dir[9]))
        _dir = timer_dir["text"]
        self.text0.setCurrentText(_dir[0])
        self.text1.setCurrentText(_dir[1])
        self.text2.setCurrentText(_dir[2])
        self.text3.setCurrentText(_dir[3])
        self.text4.setCurrentText(_dir[4])
        self.text5.setCurrentText(_dir[5])
        self.text6.setCurrentText(_dir[6])
        self.text7.setCurrentText(_dir[7])
        self.text8.setCurrentText(_dir[8])
        self.text9.setCurrentText(_dir[9])
        _dir = timer_dir["awake"]
        self.awake0.setChecked(_dir[0])
        self.awake1.setChecked(_dir[1])
        self.awake2.setChecked(_dir[2])
        self.awake3.setChecked(_dir[3])
        self.awake4.setChecked(_dir[4])
        self.awake5.setChecked(_dir[5])
        self.awake6.setChecked(_dir[6])
        self.awake7.setChecked(_dir[7])
        self.awake8.setChecked(_dir[8])
        self.awake9.setChecked(_dir[9])

    def save_set(self):
        _dir = dict()
        _dir["item_num"] = self.time_item
        _list = []
        _list += [self.execute0.currentIndex()]
        _list += [self.execute1.currentIndex()]
        _list += [self.execute2.currentIndex()]
        _list += [self.execute3.currentIndex()]
        _list += [self.execute4.currentIndex()]
        _list += [self.execute5.currentIndex()]
        _list += [self.execute6.currentIndex()]
        _list += [self.execute7.currentIndex()]
        _list += [self.execute8.currentIndex()]
        _list += [self.execute9.currentIndex()]
        _dir["execute"] = _list
        _list = []
        _list += [self.timer0.getTime().toString()]
        _list += [self.timer1.getTime().toString()]
        _list += [self.timer2.getTime().toString()]
        _list += [self.timer3.getTime().toString()]
        _list += [self.timer4.getTime().toString()]
        _list += [self.timer5.getTime().toString()]
        _list += [self.timer6.getTime().toString()]
        _list += [self.timer7.getTime().toString()]
        _list += [self.timer8.getTime().toString()]
        _list += [self.timer9.getTime().toString()]
        _dir["time"] = _list
        _list = []
        _list += [self.text0.currentText()]
        _list += [self.text1.currentText()]
        _list += [self.text2.currentText()]
        _list += [self.text3.currentText()]
        _list += [self.text4.currentText()]
        _list += [self.text5.currentText()]
        _list += [self.text6.currentText()]
        _list += [self.text7.currentText()]
        _list += [self.text8.currentText()]
        _list += [self.text9.currentText()]
        _dir["text"] = _list
        _list = []
        _list += [self.awake0.isChecked()]
        _list += [self.awake1.isChecked()]
        _list += [self.awake2.isChecked()]
        _list += [self.awake3.isChecked()]
        _list += [self.awake4.isChecked()]
        _list += [self.awake5.isChecked()]
        _list += [self.awake6.isChecked()]
        _list += [self.awake7.isChecked()]
        _list += [self.awake8.isChecked()]
        _list += [self.awake9.isChecked()]
        _dir["awake"] = _list
        return _dir

    def delete_overall_plan(self, config_index):
        self.text0.removeItem(config_index)
        self.text1.removeItem(config_index)
        self.text2.removeItem(config_index)
        self.text3.removeItem(config_index)
        self.text4.removeItem(config_index)
        self.text5.removeItem(config_index)
        self.text6.removeItem(config_index)
        self.text7.removeItem(config_index)
        self.text8.removeItem(config_index)
        self.text9.removeItem(config_index)

    def overall_add_item(self, name):
        self.text0.addItem(name)
        self.text1.addItem(name)
        self.text2.addItem(name)
        self.text3.addItem(name)
        self.text4.addItem(name)
        self.text5.addItem(name)
        self.text6.addItem(name)
        self.text7.addItem(name)
        self.text8.addItem(name)
        self.text9.addItem(name)

    def overall_rename_item(self, old_name, new_name):
        self.text0.rename(old_name, new_name)
        self.text1.rename(old_name, new_name)
        self.text2.rename(old_name, new_name)
        self.text3.rename(old_name, new_name)
        self.text4.rename(old_name, new_name)
        self.text5.rename(old_name, new_name)
        self.text6.rename(old_name, new_name)
        self.text7.rename(old_name, new_name)
        self.text8.rename(old_name, new_name)
        self.text9.rename(old_name, new_name)
