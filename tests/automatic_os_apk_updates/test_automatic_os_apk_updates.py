import pytest
from pages_chrome import PageChrome
import time

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl


class TestAutomaticOsApkUpdates(PageChrome):
    @staticmethod
    def login_and_select_device(device_id: str):
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
        TestAutomaticOsApkUpdates.login_and_select_device(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_os_version(os_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set os ota version {os_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def set_app_ota_version(device_id: str, app_version: str) -> None:
        TestAutomaticOsApkUpdates.login_and_select_device(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_app_version(app_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set app ota version {app_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def remove_os_ota_version(device_id: str) -> None:
        TestAutomaticOsApkUpdates.login_and_select_device(device_id)
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
        TestAutomaticOsApkUpdates.login_and_select_device(device_id)
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
        TestAutomaticOsApkUpdates.login_and_select_device(device_id)
        DeviceDetailsPageControl().click_button_info()
        # get info
        info_fw_version = DeviceDetailsPageControl().get_info_fw_version()
        info_app_version = DeviceDetailsPageControl().get_info_app_version()
        print(f"{info_fw_version=} {info_app_version=}")
        # time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)
        return {"info_fw_version": info_fw_version, "info_app_version": info_app_version}

    def test_first(self, request) -> None:
        """
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
        ## ---------------------------------------------------------------------------------------


        print("finish first")

    @pytest.mark.skip
    def test_second(self, request) -> None:
        print("TEST AUTOMATION second")

        print(request.config.firmware_version)
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        time.sleep(10)
        print(request.config.firmware_version)
        print("finish second")
