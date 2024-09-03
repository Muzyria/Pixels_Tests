import os
import time

import android_utils
from android_utils import *
import subprocess


def long(keycode, duration=300):
    # Нажатие кнопки

    for _ in range(50):
        os.system(f'adb shell input keyevent {keycode}')

if __name__ == '__main__':
    get_udid()
    # android_utils.get_wakefulness_status()
    # android_utils.wake_up_device()

    long(3)
