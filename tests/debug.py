import time
from android_utils import *
import subprocess


def is_wifi_connected():
    # Выполнение команды adb shell ip addr show wlan0
    result = subprocess.run(["adb", '-s', udid, "shell", "ip", "addr", "show", "wlan0"], capture_output=True, text=True)
    # Проверка подключения Wi-Fi
    if "inet " in result.stdout:
        print("Устройство подключено к Wi-Fi")
        return True
    else:
        print("Устройство не подключено к Wi-Fi")
        return False


def is_cellular_connected():
    # Выполнение команды adb shell ip addr show rmnet_data0
    result = subprocess.run(["adb", '-s', udid, "shell", "ip", "addr", "show", "rmnet_data0"], capture_output=True, text=True)
    if "inet " in result.stdout:
        print("Устройство подключено к сотовому интернету")
        return True
    else:
        print("Устройство не подключено к сотовому интернету")
        return False


if __name__ == '__main__':
    # get_udid()
    is_wifi_connected()
    is_cellular_connected()
