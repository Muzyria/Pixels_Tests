import os
import subprocess
from android_utils import *
import subprocess

# udid = "dbe407da"


def cart_burn_sleep_mode() -> None:
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'am', 'broadcast', '-a', 'com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )


if __name__ == '__main__':
    get_udid()
    wake_up_device()
