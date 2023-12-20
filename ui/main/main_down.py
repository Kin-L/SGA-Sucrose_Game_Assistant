from .main_bottom import MainBottom
import json
from tools.environment import *
import os
from time import localtime
from datetime import datetime
from tools.software import find_hwnd


class MainDown(MainBottom):
    def __init__(self):
        super().__init__()

    # 加载设置信息
    def load_main_config(self):
        self.state["hwnd"] = find_hwnd((True, "Qt5152QWindowIcon", "砂糖代理"))
        with open("personal/main_config.json", 'r', encoding='utf-8') as c:
            self.config = json.load(c)
        # 获取设置及分类
        for file in os.listdir("personal/config"):
            name, suffix = os.path.splitext(file)
            if suffix == ".json":
                prefix = name[:2]
                name = name[2:]
                if prefix == "00":
                    self.state["serial"] += [name]
                elif prefix in self.state["prefix"][1:]:
                    self.state["single"] += [name]
                else:
                    continue
                self.state["plan"][name] = prefix
        # 加载配置选框内容
        self.overall.timer.add_items(self.state["serial"] + self.state["single"])
        self.box_config_change.addItems(["点此项新建配置"] + self.state["serial"] + self.state["single"])
        self.change_module(0)
        # 加载模组设置
        self.overall.timer.load_set(self.config["timer"])
        self.overall.auto_update.setChecked(self.config["update"])
        self.stack_setting.setCurrentIndex(1)
        self.state["stack"] = 1
        _text = self.config["config"]
        self.state["text"] = _text
        self.box_config_change.setCurrentText(_text)
        self.state["index"] = self.box_config_change.currentIndex()
        self.set_lock(self.config["lock"])
        self.send_config_dir(self.config["current"])
        # 根据运行路径修改基础文件
        if env.workdir != self.config["work_path"]:
            self.config["work_path"] = env.workdir
            vbs_dir = "%s/assets/main_window/bat_scr" % env.workdir
            vbs_path = "%s/assets/main_window/bat_scr/start-SGA.vbs" % env.workdir
            with open("assets/main_window/schtasks_index.json", 'r', encoding='utf-8') as m:
                xml_dir = json.load(m)
            xml_list = xml_dir["part2"]
            xml_list[32] = "      <Command>" + vbs_path + "</Command>\n"
            xml_list[34] = "      <WorkingDirectory>" + vbs_dir + "</WorkingDirectory>\n"
            xml_dir["part2"] = xml_list
            with open("assets/main_window/schtasks_index.json", 'w', encoding='utf-8') as x:
                json.dump(xml_dir, x, ensure_ascii=False, indent=1)
            f = open("assets/main_window/bat_scr/start-SGA.bat", 'r', encoding='utf-8')
            start_list = f.readlines()
            f.close()
            start_list[5] = "start /d \"%s\" SGA.exe\n" % env.workdir
            f = open("assets/main_window/bat_scr/start-SGA.bat", 'w', encoding='utf-8')
            f.writelines(start_list)
            f.close()
            if os.path.exists("assets/maa"):
                f = open("assets/maa/bat_scr/create.bat", 'r', encoding='ansi')
                bat_list = f.readlines()
                f.close()
                bat_list[1] = f" cd. > {env.workdir}/cache/maa_complete.txt"
                f = open("assets/maa/bat_scr/create.bat", 'w', encoding='ansi')
                f.writelines(bat_list)
                f.close()

    # 保存主设置
    def save_main_data(self):
        self.config["timer"] = self.overall.timer.save_set()
        self.config["config"] = self.state["text"]
        self.config["lock"] = self.state["locked"]
        self.config["current"] = self.get_config_dir()
        self.config["update"] = self.overall.auto_update.isChecked()
        for text in self.state["name"][1:]:
            if self.state[text]["load"]:
                module = eval(f"self.{text}")
                self.config["run"][text] = module.get_run()
        with open("personal/main_config.json", 'w', encoding='utf-8') as c:
            json.dump(self.config, c, ensure_ascii=False, indent=1)

    def exit_save(self):
        self.save_main_data()
        self.indicate("SGA退出，自动保存设置成功", 1)

    def add_path(self, config_dir):
        _name = self.state["name"][config_dir["模块"]]
        config_dir["启动"] = self.config["run"][_name]
        return config_dir

    # 获取运行信息
    def get_config_run(self, text="current"):
        config_dir = self.get_config_dir(text)
        if config_dir["模块"] == 0:
            for i in range(5):
                _name = config_dir["配置%s" % i]["name"]
                if _name == "<未选择>":
                    break
                else:
                    _dir = self.get_config_dir(_name)
                    config_dir["配置%s" % i].update(self.add_path(_dir))
        else:
            config_dir = self.add_path(config_dir)
        return config_dir

    def check_timer(self):
        now_time = localtime()
        for num in range(self.overall.timer.time_item):
            execute = eval("self.overall.timer.execute%s" % num).currentIndex()
            time_str = eval("self.overall.timer.timer%s" % num).getTime().toString()
            timetuple = datetime.strptime(time_str, "%H:%M:%S").timetuple()
            if execute in [now_time[6]+2, 1]:
                if now_time[3:5] == timetuple[3:5]:
                    _text = eval("self.overall.timer.text%s" % num).currentText()
                    if _text != "<未选择>":
                        return _text
        return None
