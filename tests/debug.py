import time

from android_utils import *
import subprocess

# udid = 'dbe407da'


def wait_for_device_boot(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)

        while True:
            result = subprocess.run(["adb", "-s", udid, "shell", "pidof", "com.l1inc.yamatrack3d"], capture_output=True, text=True)
            if result.stdout.strip():  # Если приложение запущено
                print(f"Приложение com.l1inc.yamatrack3d запущено.")
                time.sleep(5)
                return True
            print("Ожидание запуска приложения...")
            time.sleep(5)  # Проверяем каждые 5 секунд
    return inner



def device_reboot() -> None:
    """Reboot device"""
    subprocess.run(['adb', '-s', udid, 'reboot'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



if __name__ == '__main__':
    get_udid()
    # decorated_function = wait_for_device_boot(device_reboot)
    # decorated_function()

    cart_burn_sleep_mode()
    time.sleep(20)
    wake_up_device()
