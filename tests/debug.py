import os
import random
import time

import android_utils
from android_utils import *
import subprocess


firmware_gps = dict(LC79D=('LC79DANR01A06S_BETA0322', 'LC79DANR01A07S'),
                    LC79H=('LC79HALNR11A01S', 'LC79HALNR11A02S'),
                    U_BLOX=('UDR1.00', 'UDR1.31'))


def get_list_gps_version_ota(device_gps_version: str):
    for k, v in firmware_gps.items():
        return k if device_gps_version in v else None



if __name__ == '__main__':
    # get_udid()
    # android_utils.get_wakefulness_status()
    # android_utils.wake_up_device()

    print(get_list_gps_version_ota('LC79DANR01A06S_BETA0322'))
