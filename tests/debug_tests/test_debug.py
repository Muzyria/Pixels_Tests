import time

import pytest

from common_test_steps import DeviceScripts

import android_utils
from pages_android.base_page_android import Page


class TestDebug:
    def test_debug(self, request):
        print()
        print(f"START {request.node.name}")

        # time.sleep(120)

        android_utils.is_wifi_connected()
        print("---------------------------------- DEBUG")
        Page.toggle_wifi()
        # print("----------------------------------------OK")
        # android_utils.is_wifi_connected()
        # print("----------------")


        # DeviceScripts.reboot_device_and_restart_appium()


        print(f"FINISH {request.node.name}")
