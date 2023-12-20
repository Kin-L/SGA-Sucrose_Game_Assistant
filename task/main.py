from task.maa.main import TaskMAA
from task.genshin.main import TaskGenshin
from task.kleins.main import TaskKleins
from task.m7a.main import TaskM7A


class TaskRun(TaskKleins, TaskGenshin, TaskMAA, TaskM7A):
    def task_start(self, task):
        # 运行
        if task["模块"] == 0:
            for i in range(5):
                single_task = task["配置%s" % i]
                if single_task["name"] == "<未选择>":
                    self.indicate(f"计划{i+1}未选择。")
                else:
                    single_task["运行"][1] = True
                    self.single_run(single_task)
        else:
            self.single_run(task)
        # 结束
        self.kill(1)

    def single_run(self, task):
        if task["模块"] == 1:
            TaskKleins.__init__(self)
            self.kleins_start(task)
        elif task["模块"] == 2:
            TaskGenshin.__init__(self)
            self.genshin_start(task)
        elif task["模块"] == 3:
            TaskMAA.__init__(self)
            self.maa_start(task)
        elif task["模块"] == 4:
            TaskM7A.__init__(self)
            self.m7a_start(task)
        else:
            self.indicate("error:未知模块。")
            self.kill(3)


if __name__ == '__main__':
    pass
