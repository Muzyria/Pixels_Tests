import time

from framework_appium.driver_appium import DriverAppium
from android_utils import *

from pages_android import Page
import pytest
import pages_android

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options


from pages_chrome.login_page import LoginPageSyncwise360

@pytest.mark.skip
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
    print("test complete")


@pytest.mark.skip
def test_something_2():
    print("test something 2")
    print(DriverChrome.chrome_instance.session_id)
    time.sleep(5)
    DriverChrome.finish()
    time.sleep(5)
    DriverChrome.start(get_driver_chrome_options())
    time.sleep(5)
    print("test complete")


def test_something_login():
    print("test something LOGIN")
    LoginPageSyncwise360.open(LoginPageSyncwise360.PAGE_URL)
    # LoginPageSyncwise360().enter_login()
    LoginPageSyncwise360().enter_login().enter_password().click_login_button()
    time.sleep(10)

    print("test complete LOGIN")
