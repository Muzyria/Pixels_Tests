import time

from android_utils import *
import subprocess

# udid = 'dbe407da'


def cart_of_hole_sleep_mode() -> None:
    """Put device in off hole sleep"""
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'am', 'broadcast', '-a', 'com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    time.sleep(20)  # Период ожидания
    print("Device in Off Hole Sleep Mode")



def device_reboot() -> None:
    """Reboot device"""
    subprocess.run(['adb', '-s', udid, 'reboot'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



if __name__ == '__main__':
    get_udid()
    cart_of_hole_sleep_mode()

