import os
import random
import time

import android_utils
from android_utils import *
import subprocess


def convert_time(time_str):
    # Если длина строки 3, добавляем ведущий ноль
    if len(time_str) == 3:
        time_str = '0' + time_str

    # Разбиваем строку на часы и минуты
    hours = time_str[:-2]  # все символы кроме последних двух
    minutes = time_str[-2:]  # последние два символа

    # Возвращаем результат в формате HH:MM
    return f"{hours}:{minutes}"






if __name__ == '__main__':
    # get_udid()
    # android_utils.get_wakefulness_status()
    # android_utils.wake_up_device()
    # Пример использования
    time_str = "103"
    print(convert_time(time_str))  # Вывод: 01:23

