import os
import subprocess
from android_utils import *
import subprocess

# udid = "dbe407da"


def wake_up_device() -> None:
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )


if __name__ == '__main__':
    get_udid()
    wake_up_device()
