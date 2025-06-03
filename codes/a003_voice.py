# --------------- basic info --------------- *
# auther: wegener 
# time & date: 2025-02-09, 16:47
# project: a002_编译.py, PyCharm, a003_voice 
iii = 0


# --------------- debug-func --------------- *
def aa():
    print("a try\n")


def bb():
    global iii
    print("try order %d \n" % (iii))
    iii = iii + 1


# --------------- information if it's copied--------------- *

# * website of the project: 
# * name of the original author(can be LLM):

# ------------------------------end predefine------------------------------

# start import --- *
from math import *


# end import ----- *

def play_voice(voice: str):
    import pyttsx3
    """
    播放输入的语音内容
    :param voice: 要播放的语音内容
    """
    engine = pyttsx3.init()  # 初始化语音引擎
    engine.say(voice)  # 添加要播放的语音内容
    engine.runAndWait()  # 播放语音
