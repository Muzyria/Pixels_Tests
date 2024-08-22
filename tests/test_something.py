import time

from framework_appium.driver_appium import DriverAppium
from android_utils import *

from pages_android import Page
import pytest
import pages_android


# @pytest.mark.skip
def test_something():
    print("test something")

    # assert Page().find_element_by_id('menuDrawer')

    get_wakefulness_status()
    print(DriverAppium.appium_instance.session_id)
    print("put in cart burn")
    device_reboot()

    DriverAppium.finish()
    print("wait 120 seconds")
    time.sleep(120)
    print("try to connect")
    get_udid()
    DriverAppium.start(get_driver_appium_options())
    print(DriverAppium.appium_instance.session_id)
    print("wake up")
    wake_up_device()



    print("test complite")

