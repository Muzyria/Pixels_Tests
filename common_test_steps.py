import time

import pytest
import android_utils

from framework_appium.driver_appium import DriverAppium

from pages_android.main_screen import MainPage
from pages_android.menu_screen import MenuPage
from pages_android.settings_screen import SettingsPage
from pages_android.asset_details_screen import AssetDetailsPage

from pages_android.uua_main_screen import UUAMainPage
from pages_android.uua_update_firmware_screen import UUAUpdateFirmwarePage

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.coursemap_page_360 import CourseMapSyncWise360
from pages_chrome.assets_page_360 import AssetsSyncWise360

from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl


class DeviceScripts:
    @staticmethod
    def restart_appium(func):
        def inner(*args, **kwargs):
            DriverAppium.finish()
            func(*args, **kwargs)
            DriverAppium.start(android_utils.get_driver_appium_options())
        return inner

    @staticmethod
    def reboot_device_and_restart_appium(wait_time: int = 70) -> None:
        """Device Reboot and restart appium (for update GPS use time 300 and 120)"""
        # Device Reboot
        DriverAppium.finish()
        android_utils.device_reboot()  # Device Reboot
        time.sleep(wait_time)  # wait for device reboot
        android_utils.wait_for_the_device_to_boot()
        DriverAppium.start(android_utils.get_driver_appium_options())
        MainPage().wait_map_activity()

    @staticmethod
    def device_full_app_reset():
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        android_utils.swipe_screen_down_to_up()
        SettingsPage().press_full_app_reset_button()
        SettingsPage().press_button_yes()

    @staticmethod
    def get_tablet_asset_info() -> dict:
        """
        return device asset info
        """
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        SettingsPage().press_assets_details_button()

        tablet_os_version = AssetDetailsPage().get_os_version()
        tablet_apk_version = AssetDetailsPage().get_apk_version()
        tablet_cable_version = AssetDetailsPage().get_cable_version()
        tablet_gps_version = AssetDetailsPage().get_gps_version()

        # print(f'{tablet_os_version=} {tablet_apk_version=} {tablet_cable_version} {tablet_gps_version}')
        AssetDetailsPage().press_button_cancel()
        SettingsPage().press_button_cancel()
        MenuPage().press_play_golf_button()
        return {"tablet_os_version": tablet_os_version,
                "tablet_apk_version": tablet_apk_version,
                "tablet_cable_version": tablet_cable_version,
                "tablet_gps_version": tablet_gps_version}


class ControlScripts:
    @staticmethod
    def login_and_select_device_control(device_id: str):
        """login on site Control and select device manager"""
        LoginPageControl.open(LoginPageControl.PAGE_URL)  # open Control
        LoginPageControl().enter_login().enter_password().click_login_button()  # check URL
        LoginPageControl.is_opened(LoginPageControl.MAIN_PAGE)
        SuperiorPageControl.open(SuperiorPageControl.PAGE_URL)  # open Superior
        SuperiorPageControl.is_opened(SuperiorPageControl.PAGE_URL)  # check URL
        SuperiorPageControl().click_button_device_manager()
        SuperiorPageControl().click_device_id_in_box(device_id)
        time.sleep(5)


class SyncWise360Scripts:
    # @staticmethod
    # def get_device_info_360(device_name: str) -> dict[str, str]:
    #     LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
    #     LoginPageSyncWise360().enter_login().enter_password().click_login_button()
    #     CourseMapSyncWise360().click_assets_button()
    #     AssetsSyncWise360().click_name_car_in_list(device_name)
    #     CourseMapSyncWise360().click_tab_asset_details()
    #     # get device info
    #     device_info_os_version = CourseMapSyncWise360().get_device_info_os_version()
    #     device_info_apk_version = CourseMapSyncWise360().get_device_info_apk_version()
    #     print(f"{device_info_os_version=} {device_info_apk_version=}")
    #
    #     LoginPageSyncWise360().click_logout_button()
    #     time.sleep(3)
    #     return {"device_info_os_version": device_info_os_version, "device_info_apk_version": device_info_apk_version}
    ...
