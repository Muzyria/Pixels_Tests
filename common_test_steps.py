import time

import pytest
import android_utils

from framework_appium.driver_appium import DriverAppium

from pages_android.main_screen import MainPage
from pages_android.menu_screen import MenuPage
from pages_android.settings_screen import SettingsPage
from pages_android.request_log_files_screen import RequestLogFilesPage


from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl


def reboot_device_and_restart_appium() -> None:
    """Device Reboot and restart appium"""
    # Device Reboot
    DriverAppium.finish()
    android_utils.device_reboot()  # Device Reboot
    time.sleep(70)  # wait for device reboot
    android_utils.wait_for_the_device_to_boot()
    DriverAppium.start(android_utils.get_driver_appium_options())
    MainPage().wait_map_activity()
