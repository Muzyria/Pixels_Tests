import os
import time

import android_utils
from android_utils import *
import subprocess



if __name__ == '__main__':
    get_udid()
    # android_utils.get_wakefulness_status()
    # android_utils.wake_up_device()
    s = android_utils.get_current_activity()
    print(s)

    android_utils.touch_screen_by_coordinate(200, 400)