import sys
from tools.environment import *


class Task:
    def __init__(self):
        self.task_all = None
        self.task = None

    @staticmethod
    def indicate(msg: str, mode=0):
        logger(msg)

    @staticmethod
    def kill(mode):
        logger("结束")
        sys.exit()
