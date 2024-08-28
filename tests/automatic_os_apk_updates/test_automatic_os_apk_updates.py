import pytest
from pages_chrome import PageChrome
from pages_android import Page
import time

from framework_appium.driver_appium import DriverAppium

from pages_android.main_screen import MainPage
from pages_android.menu_screen import MenuPage
from pages_android.settings_screen import SettingsPage
from pages_android.asset_details_screen import AssetDetailsPage


from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.coursemap_page_360 import CourseMapSyncWise360
from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl
from pages_chrome.assets_page_360 import AssetsSyncWise360

import android_utils


class TestAutomaticOsApkUpdates:
    # control ----------------------------------------------------------------------------------------------
    @staticmethod
    def login_and_select_device_control(device_id: str):
        LoginPageControl.open(LoginPageControl.PAGE_URL)  # open Control
        LoginPageControl().enter_login().enter_password().click_login_button()  # check URL
        LoginPageControl.is_opened(LoginPageControl.MAIN_PAGE)
        SuperiorPageControl.open(SuperiorPageControl.PAGE_URL)  # open Superior
        SuperiorPageControl.is_opened(SuperiorPageControl.PAGE_URL)  # check URL
        SuperiorPageControl().click_button_device_manager()
        SuperiorPageControl().click_device_id_in_box(device_id)
        time.sleep(5)

    @staticmethod
    def set_os_ota_version(device_id: str, os_version: str) -> None:
        TestAutomaticOsApkUpdates.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_os_version(os_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set os ota version {os_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def set_app_ota_version(device_id: str, app_version: str) -> None:
        """Set que an update APK on Control"""
        TestAutomaticOsApkUpdates.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_app_version(app_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set app ota version {app_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def remove_os_ota_version(device_id: str) -> None:
        TestAutomaticOsApkUpdates.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        if DeviceDetailsPageControl().check_button_remove_os_is_displayed():
            DeviceDetailsPageControl().click_button_remove_os_update()
            time.sleep(2)
            print()
            print("REMOVE OS UPDATE IS DONE")
        else:
            print()
            print("REMOVE OS UPDATE IS NOT AVAILABLE")
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def remove_app_ota_version(device_id: str) -> None:
        TestAutomaticOsApkUpdates.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        if DeviceDetailsPageControl().check_button_remove_app_is_displayed():
            DeviceDetailsPageControl().click_button_remove_app_update()
            time.sleep(2)
            print()
            print("REMOVE APP UPDATE IS DONE")
        else:
            print()
            print("REMOVE APP UPDATE IS NOT AVAILABLE")
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def get_info_control(device_id: str) -> dict[str: str]:
        TestAutomaticOsApkUpdates.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_info()
        # get info
        info_fw_version = DeviceDetailsPageControl().get_info_fw_version()
        info_app_version = DeviceDetailsPageControl().get_info_app_version()
        print(f"{info_fw_version=} {info_app_version=}")

        LoginPageControl().click_logout_button()
        time.sleep(3)
        return {"info_fw_version": info_fw_version, "info_app_version": info_app_version}

    # 360 ----------------------------------------------------------------------------------------------------
    @staticmethod
    def get_device_info_360(device_name: str) -> dict[str: str]:
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        CourseMapSyncWise360().click_assets_button()
        AssetsSyncWise360().click_name_car_in_list(device_name)
        CourseMapSyncWise360().click_tab_asset_details()
        # get device info
        device_info_os_version = CourseMapSyncWise360().get_device_info_os_version()
        device_info_apk_version = CourseMapSyncWise360().get_device_info_apk_version()
        print(f"{device_info_os_version=} {device_info_apk_version=}")

        LoginPageSyncWise360().click_logout_button()
        time.sleep(3)
        return {"device_info_os_version": device_info_os_version, "device_info_apk_version": device_info_apk_version}

    # device -------------------------------------------------------------------------------------------------
    @staticmethod
    def get_tablet_apk_os_version():
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        SettingsPage().press_assets_details_button()
        tablet_os_version = AssetDetailsPage().get_os_version()
        tablet_apk_version = AssetDetailsPage().get_apk_version()

        print(f'{tablet_os_version=} {tablet_apk_version=}')
        AssetDetailsPage().press_button_cancel()
        SettingsPage().press_button_cancel()
        MenuPage().press_play_golf_button()
        return {"tablet_os_version": tablet_os_version, "tablet_apk_version": tablet_apk_version}

    def test_1_apk_cart_burn_sleep(self, request) -> None:
        """
        *Wi-Fi*
        *APK*
        *CASE A: Cart Barn Sleep*
        1. With device awake, que an update within Control - *Confirmed*
        2. Confirm device recognizes an update available (via logs within Android studio) when falling into cart barn sleep - *Confirmed*
        3. Wake up device, and confirm the Play Golf screen loads - *Confirmed*
        4. Confirm download status bar is updating during download - *Confirmed*
        - Confirm there is no kind of disruption when download is in process (User shouldn't even know it's occurring, unless icons status is open) - *Confirmed*
        5. Confirm when download is complete, icon indicates download was successful - *Confirmed*
        6. Confirm device installs upon waking up from Cart Barn Sleep - *Confirmed*
        - Confirm updated software version is displayed in APK Asset Details, 360, and Control - *Confirmed*
        9. Put the device into Cart Barn sleep and que another update - *Confirmed*
        10. Wake up device, and confirm it downloaded the update (check the download icon status on PlayGolf screen) - *Confirmed*
        """
        print()
        print(f"START {__name__}")
        self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_to_update"])  # set que an update APK on Control
        # step 1
        android_utils.cart_burn_sleep_mode()  # Put Device in Cart Burn Sleep
        time.sleep(10)
        # step 2
        android_utils.wake_up_device()

        MainPage().wait_spinner_to_invisible()
        time.sleep(3)
        MainPage().check_menu_button()
        # step 3
        MainPage().press_flag_button()
        # MainPage().check_view_progress_list()

        MainPage().check_view_button_complete_list()
        # step 4

        # return ____________________________________________________________
        self.remove_app_ota_version(request.config.firmware_version["device_id"])
        self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_current"])  # set que an update APK on Control
        android_utils.cart_burn_sleep_mode()  # Put Device in Cart Burn Sleep
        android_utils.wake_up_device()
        # ___________________________________________________________________
        print(f"FINISH {__name__}")

        # self.remove_os_ota_version(request.config.firmware_version["device_id"])
        # self.remove_app_ota_version(request.config.firmware_version["device_id"])
        # --------------------------------------------------------------------------------------
        # res = self.get_info_control(request.config.firmware_version["device_id"])
        # print(res)
        # ---------------------------------------------------------------------------------------
        # res = self.get_device_info_360(request.config.firmware_version["device_name"])
        # print(res)
        # -----------------------------------------------------------------------------------------
        # devise ----------------------------------------------------------------------------------

        # print("first check")
        # self.get_tablet_apk_os_version()
        #
        # DriverAppium.finish()
        # # android_utils.cart_burn_sleep_mode()
        # # time.sleep(10)
        # # android_utils.wake_up_device()
        # android_utils.device_reboot()
        # android_utils.wait_for_the_device_to_boot()
        # time.sleep(60)
        #
        # DriverAppium.start(android_utils.get_driver_appium_options())
        # # добавить проверку что все скачалось
        #
        # # android_utils.cart_burn_sleep_mode()
        # # time.sleep(10)
        # # android_utils.wake_up_device()
        #
        # DriverAppium.finish()
        # android_utils.device_reboot()
        # android_utils.wait_for_the_device_to_boot()
        # time.sleep(120)
        # android_utils.wait_for_the_device_to_boot()
        #
        # DriverAppium.start(android_utils.get_driver_appium_options())
        # print("second check")
        # self.get_tablet_apk_os_version()
        #
        #
        # # MainPage().press_flag_button()
        # # res = MainPage().get_text_no_active_downloads()
        # # print(f"{res=}")
        # print("finish first")

    @pytest.mark.skip
    def test_second(self, request) -> None:
        """
                WiFi
                OS
                CASE A: Cart Barn Sleep
                1. With device awake, que an update within Control
                2. Confirm device recognizes an update available (via logs within Android studio) when falling into cart barn sleep
                3. Wake up device, and confirm the Play Golf screen loads
                4. Confirm download status bar is updating during download
                - Confirm there is no kind of disruption when download is in process (User shouldn't even know it's occurring, unless icons status is open)
                5. Confirm when download is complete, icon indicates download was successful
                6. Confirm device installs upon waking up from Cart Barn Sleep
                - Confirm updated software version is displayed in APK Asset Details, 360, and Control
                """
        print()
        print("TEST AUTOMATION first")
        # self.set_os_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["os_to_update"])
        # self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_to_update"])
        # # --------------------------------------------------------------------------------------
        # self.remove_os_ota_version(request.config.firmware_version["device_id"])
        # self.remove_app_ota_version(request.config.firmware_version["device_id"])
        # # --------------------------------------------------------------------------------------
        # res = self.get_info_control(request.config.firmware_version["device_id"])
        # print(res)
        # ---------------------------------------------------------------------------------------
        # res = self.get_device_info_360(request.config.firmware_version["device_name"])
        # print(res)
        # -----------------------------------------------------------------------------------------
        # devise ----------------------------------------------------------------------------------

        print("first check")
        self.get_tablet_apk_os_version()

        DriverAppium.finish()
        # android_utils.cart_burn_sleep_mode()
        # time.sleep(10)
        # android_utils.wake_up_device()
        android_utils.device_reboot()
        android_utils.wait_for_the_device_to_boot()
        time.sleep(60)

        DriverAppium.start(android_utils.get_driver_appium_options())
        # добавить проверку что все скачалось

        # android_utils.cart_burn_sleep_mode()
        # time.sleep(10)
        # android_utils.wake_up_device()

        DriverAppium.finish()
        android_utils.device_reboot()
        android_utils.wait_for_the_device_to_boot()
        time.sleep(120)
        android_utils.wait_for_the_device_to_boot()

        DriverAppium.start(android_utils.get_driver_appium_options())
        print("second check")
        self.get_tablet_apk_os_version()

        # MainPage().press_flag_button()
        # res = MainPage().get_text_no_active_downloads()
        # print(f"{res=}")
        print("finish first")
