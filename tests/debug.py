import os
import subprocess
from android_utils import *
import subprocess

# udid = "192.168.0.100"


def cart_mode() -> bool:

    while True:
        result = subprocess.run(["adb", "-s", udid, "shell", "pidof", "com.l1inc.yamatrack3d"], capture_output=True, text=True)
        if result.stdout.strip():  # Если приложение запущено
            print(f"Приложение com.l1inc.yamatrack3d запущено.")
            time.sleep(5)
            print("READY ______")
            return True
        print("Ожидание запуска приложения...")
        time.sleep(5)  # Проверяем каждые 5 секунд




if __name__ == '__main__':
    get_udid()
    print(cart_mode())
