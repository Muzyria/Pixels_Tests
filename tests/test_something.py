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



    time.sleep(3)
    get_wakefulness_status()
    print("put in cart burn")
    cart_burn_sleep_mode()
    time.sleep(15)
    print("wake up")
    wake_up_device()
    print("test complite")

