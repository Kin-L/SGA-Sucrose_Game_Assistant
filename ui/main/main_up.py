from .main_down import MainDown
from tools.environment import *
import traceback
import shutil
import random
import os
import json
import time
from datetime import timedelta, datetime


class MainUp(MainDown):
    def __init__(self):
        super().__init__()

    # 删除配置项
    def delete_plan(self):
        try:
            _text = self.box_config_change.currentText()
            _index = self.box_config_change.currentIndex()
            _num = len(self.box_config_change.items)
            print(self.state["serial"], type[self.state["serial"]])
            if _num > 2:
                if _text in self.state["single"]:
                    self.state["single"].remove(_text)
                    if self.state["mix"]["load"]:
                        self.mix.remove_item(_text)
                elif _text in self.state["serial"]:
                    self.state["serial"].remove(_text)
                self.overall.timer.delete_overall_plan(_index)
                os.remove(self.get_file_path(_text))
                self.indicate("删除配置：" + _text, 1)
                if _index + 1 == _num:
                    print(1, _index, _num)
                    self.box_config_change.setCurrentIndex(_index-1)
                    self.state["plan"].pop(_text)
                    self.state["text"] = self.box_config_change.currentText()
                    self.state["index"] = self.box_config_change.currentIndex()
                    self.indicate("载入配置：%s" % self.state["text"], 1)
                else:
                    print(2, _index, _num)
                    self.box_config_change.setCurrentIndex(_index+1)
                    self.state["plan"].pop(_text)
                    self.state["text"] = self.box_config_change.currentText()
                    self.state["index"] = self.box_config_change.currentIndex()
                self.box_config_change.removeItem(_index)
                if self.state["locked"]:
                    _dir = self.get_config_dir(self.state["text"])
                    self.send_config_dir(_dir)
            else:
                self.indicate("删除配置失败：最少需要有一项配置", 1)
        except Exception as e:
            self.indicate(f"删除配置异常：{e}", 1)
            logger.error(traceback.format_exc())

    # 选择方案改变 & 重命名 & 新建方案
    def config_change(self):
        index_now = self.box_config_change.currentIndex()
        # 新建方案
        if index_now == 0:
            try:
                newname = "默认配置" + str(random.randint(999, 10000))
                shutil.copyfile(r"assets\main_window\默认配置.json",
                                r"personal\config\00%s.json" % newname)
                # 更新方案列表
                self.state["plan"][newname] = "00"
                self.state["serial"] += [newname]
                self.box_config_change.addItem(newname)
                self.overall.timer.overall_add_item(newname)
                # if prefix == "00" and self.state["mix"]["load"]:
                # self.mix.remove_item(_text)
                self.indicate("新配置已创建：" + newname, 1)
            except Exception as e:
                self.indicate(f"新建配置异常：{e}", 1)
                logger.error(traceback.format_exc())
                return 0
            try:
                # 加载配置
                if self.state["locked"]:
                    _dir = self.get_config_dir(newname)
                    self.send_config_dir(_dir)
                    self.box_config_change.setCurrentText(newname)
                    self.state["text"] = self.box_config_change.currentText()
                    self.state["index"] = self.box_config_change.currentIndex()
                else:
                    self.box_config_change.setCurrentText(self.state["text"])
            except Exception as e:
                self.indicate(f"载入配置异常：{e}", 1)
                logger.error(traceback.format_exc())
                return 0
        # 配置重命名
        elif index_now == -1:
            try:
                text_past = self.state["text"]
                text_now = self.box_config_change.currentText()
                prefix = self.state["plan"][text_past]
                os.rename(r"personal/config/%s.json" % (prefix + text_past),
                          r"personal/config/%s.json" % (prefix + text_now))
                self.box_config_change.setItemText(self.state["index"], text_now)
                self.box_config_change.setCurrentIndex(self.state["index"])
                self.overall.timer.overall_rename_item(text_past, text_now)
                if prefix != "00" and self.state["mix"]["load"]:
                    self.mix.rename_item(text_past, text_now)
                self.state["plan"][text_now] = self.state["plan"].pop(text_past)
                self.state["text"] = text_now
                self.indicate("配置更名：%s >>> %s" % (text_past, text_now), 1)
            except Exception as e:
                self.indicate(f"重命名配置异常：{e}", 1)
                logger.error(traceback.format_exc())
        # 选择方案改变
        else:
            try:
                self.state["text"] = self.box_config_change.currentText()
                self.state["index"] = self.box_config_change.currentIndex()
                if self.state["locked"]:
                    # 加载配置
                    _dir = self.get_config_dir(self.state["text"])
                    self.send_config_dir(_dir)
                    self.indicate("载入配置：%s" % self.state["text"], 1)
            except Exception as e:
                self.indicate(f"载入配置异常：{e}", 1)
                logger.error(traceback.format_exc())

    # 设置锁定模式（并加载配置）
    def set_config_lock(self, mode):
        self.set_lock(mode)
        if mode:
            _text = self.box_config_change.currentText()
            _dir = self.get_config_dir(_text)
            self.send_config_dir(_dir)

    # 保存当前界面设置信息
    def save_config(self):
        try:
            index_now = self.stack_module.currentIndex()
            text = self.box_config_change.currentText()
            prefix_past = self.state["plan"][text]
            name_past = prefix_past + text
            path = "personal/config/%s.json"
            if index_now == int(prefix_past):
                name_new = prefix_past + text
            else:
                new_prefix = self.state["prefix"][index_now]
                self.state["plan"][text] = new_prefix
                name_new = new_prefix + text
                os.rename(path % name_past, path % name_new)
                if prefix_past == "00" and index_now != 0:
                    self.mix.add_item(text)
                else:
                    self.mix.remove_item(name_past)
            with open(path % name_new, 'w', encoding='utf-8') as c:
                json.dump(self.get_config_dir(), c, ensure_ascii=False, indent=1)
            self.indicate("保存配置：%s" % text, 1)
        except Exception as e:
            self.indicate(f"保存异常：{e}", 1)
            logger.error(traceback.format_exc())

    # 应用定时
    def apply_timer(self):
        try:
            with open(r"assets\main_window\schtasks_index.json", 'r', encoding='utf-8') as x:
                xml_dir = json.load(x)
            auto, awake = [], []
            for num in range(self.overall.timer.time_item):
                daily = eval("self.overall.timer.execute%s" % num).currentIndex()
                _text = eval("self.overall.timer.text%s" % num).currentIndex()
                _awake = eval("self.overall.timer.awake%s" % num).isChecked()
                if daily and _text != "<未选择>":
                    if daily == 1:
                        _item = xml_dir["daily"]
                    else:
                        _item = xml_dir["weekly"]
                        week = \
                            ["", "", "Monday", "Tuesday", "Wednesday", "Thursday",
                             "Friday", "Saturday", "Sunday"][daily]
                        _item[5] = "          <" + week + " />\n"
                    _str = eval("self.overall.timer.timer%s" % num).getTime().toString()
                    pydatetime = datetime.strptime(_str, "%H:%M:%S") - timedelta(minutes=2)
                    wake_time = time.strftime("%H:%M", pydatetime.timetuple())
                    _item[1] = f"      <StartBoundary>2023-09-20T{wake_time}</StartBoundary>\n"
                    if _awake:
                        awake += _item
                    else:
                        auto += _item
            if auto or awake:
                if auto:
                    _p2 = xml_dir["part2"]
                    _p2[22] = f"<WakeToRun>false</WakeToRun>"
                    auto = xml_dir["part1"] + auto + _p2
                    xml_path = r"assets\main_window\SGA-auto.xml"
                    f = open(xml_path, 'w', encoding='utf-16')
                    f.writelines(auto)
                    f.close()
                    cmd_run("schtasks.exe /create /tn SGA-auto /xml \"%s\" /f" % xml_path)
                else:
                    cmd_run("schtasks.exe /DELETE /tn SGA-auto /f")
                if awake:
                    _p2 = xml_dir["part2"]
                    _p2[22] = f"<WakeToRun>true</WakeToRun>"
                    awake = xml_dir["part1"] + awake + _p2
                    xml_path = r"assets\main_window\SGA-awake.xml"
                    f = open(xml_path, 'w', encoding='utf-16')
                    f.writelines(awake)
                    f.close()
                    cmd_run("schtasks.exe /create /tn SGA-awake /xml \"%s\" /f" % xml_path)
                else:
                    cmd_run("schtasks.exe /DELETE /tn SGA-awake /f")
                self.indicate("应用定时成功。", 1)
            else:
                cmd_run("schtasks.exe /DELETE /tn SGA-auto /f")
                cmd_run("schtasks.exe /DELETE /tn SGA-awake /f")
                self.indicate("清除定时。", 1)
        except Exception as e:
            self.indicate(f"应用定时异常：{e}", 1)
            logger.error(traceback.format_exc())
