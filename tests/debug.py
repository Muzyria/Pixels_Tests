import os
import random
import time

import android_utils
from android_utils import *
import subprocess


firmware_gps = dict(LC79D=('LC79DANR01A06S_BETA0322', 'LC79DANR01A07S'),
                    LC79H=('LC79HALNR11A01S', 'LC79HALNR11A02S'),
                    U_BLOX=('UDR1.00', 'UDR1.31'))


def get_list_gps_version_ota(device_gps_version: str) -> list:
    another_gps_version = []
    for key, value in firmware_gps.items():
        if device_gps_version not in value:
            another_gps_version.append(value[0])
        else:
            index = value.index(device_gps_version)
            print(index)
            another_gps_version.insert(0, value[1 - index])

    return another_gps_version



if __name__ == '__main__':
    # get_udid()
    # android_utils.get_wakefulness_status()
    # android_utils.wake_up_device()

    print(get_list_gps_version_ota('LC79DANR01A06S_BETA0322'))
