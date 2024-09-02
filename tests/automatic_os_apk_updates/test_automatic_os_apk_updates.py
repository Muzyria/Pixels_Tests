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
    def get_info_control(device_id: str) -> dict[str, str]:
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
    def get_device_info_360(device_name: str) -> dict[str, str]:
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

    @staticmethod
    def device_full_app_reset():
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        android_utils.swipe_screen_down_to_up()
        SettingsPage().press_full_app_reset_button()
        SettingsPage().press_button_yes()

    # test utility -------------------------------------------------------------------------------------------
    @staticmethod
    def check_version_installed_ota(name_check: str, request, check_version_apk: str = None) -> bool | str:
        """Check visible version ota on devise, control, 360"""
        print(f"__STEP_TO_CHECK_VERSION__ {name_check}")
        if name_check == "APK":

            # check version apk on device
            update_result = TestAutomaticOsApkUpdates.get_tablet_apk_os_version()  # check version apk on device
            if not check_version_apk == update_result["tablet_apk_version"]:
                return "Not Confirmed install APK on device"

            # check version apk on control
            update_info_control = TestAutomaticOsApkUpdates.get_info_control(request.config.firmware_version["device_id"])  # check version apk on control
            if not check_version_apk == update_info_control["info_app_version"]:
                return "Not Confirmed check version APK on control"

            # check version apk on 360
            update_info_360 = TestAutomaticOsApkUpdates.get_device_info_360(request.config.firmware_version["device_name"])  # check version apk on 360
            if not check_version_apk == update_info_360["device_info_apk_version"]:
                return "Not Confirmed check version APK on 360"
            return True

    @staticmethod
    def return_current_version_ota_for_tests(name_ota: str, request, off_hole_logic: bool = False, ) -> bool | str:
        """return current version ota for tests.
            for off hole logic use value True
        """
        if name_ota == "APK":
            # return current version APK
            print("return current version APK")
            TestAutomaticOsApkUpdates.remove_app_ota_version(request.config.firmware_version["device_id"])
            TestAutomaticOsApkUpdates.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_current"])  # set que an update APK on Control
            # Full APP Reset and load apk version
            TestAutomaticOsApkUpdates.device_full_app_reset()  # Full APP Reset and load apk version
            MainPage().wait_spinner_to_invisible()
            time.sleep(3)
            assert MainPage().check_menu_button_is_visible(), "Play Golf is not loaded"  # check loads application
            MainPage().press_flag_button()
            # if of hole logic
            if off_hole_logic:
                assert MainPage().get_text_no_active_downloads() == "There are no active downloads", "Loads APK is not empty"
                return True

            MainPage().check_view_button_complete_list()  # check button complete is visible
            # Full APP Reset and install apk version
            TestAutomaticOsApkUpdates.device_full_app_reset()  # Full APP Reset and install apk version
            MainPage().wait_spinner_to_invisible()
            time.sleep(40)
            assert MainPage().check_menu_button_is_visible(), "Play Golf is not loaded"  # check install application
            MainPage().press_flag_button()
            assert MainPage().get_text_no_active_downloads() == "There are no active downloads", "Loads APK is not empty"
            # check version apk on device
            update_result = TestAutomaticOsApkUpdates.get_tablet_apk_os_version()  # check version apk on device
            if not request.config.firmware_version["apk_current"] == update_result["tablet_apk_version"]:
                return "Not Confirmed update APK version for current version"
            return True

    # tests --------------------------------------------------------------------------------------------------

    # @pytest.mark.skip
    @pytest.mark.wifi
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
        # step 3
        android_utils.wake_up_device()  # Wakeup device from Cart Burn sleep
        MainPage().wait_spinner_to_invisible()
        time.sleep(3)
        assert MainPage().check_menu_button_is_visible() is True, "Play Golf is not loaded"  # check loads application
        # step 4
        # step 5
        MainPage().press_flag_button()
        # MainPage().check_view_progress_list()
        MainPage().check_view_button_complete_list()  # check button complete is visible
        # step 6
        android_utils.cart_burn_sleep_mode()  # Put Device in Cart Burn Sleep
        time.sleep(10)
        android_utils.wake_up_device()  # Wakeup device from Cart Burn sleep
        MainPage().wait_spinner_to_invisible()
        time.sleep(40)  # wait for update APK

        # step to check ________________________________________________________________________________________________
        print("next step to check")
        check_version = request.config.firmware_version["apk_to_update"]
        result = self.check_version_installed_ota("APK", request, check_version)
        assert result is True, f"Error: {result}"

        # return current version APK ___________________________________________________________________________________
        self.return_current_version_ota_for_tests("APK", request)

        print(f"FINISH {__name__}")

        # self.remove_os_ota_version(request.config.firmware_version["device_id"])
        # self.remove_app_ota_version(request.config.firmware_version["device_id"])
        # --------------------------------------------------------------------------------------
        # res = self.get_info_control(request.config.firmware_version["device_id"])
        # print(res)
        # ---------------------------------------------------------------------------------------

    # @pytest.mark.skip
    @pytest.mark.wifi
    def test_2_apk_off_hole_sleep(self, request) -> None:
        """
        *APK*
        *CASE B: Off Hole Sleep*
        1. With device awake, que an update within Control - *Confirmed*
        2. Confirm device recognizes an update available (via logs within Android studio) when falling into Off Hole sleep - *Confirmed*
        3. Wake up device, and confirm the Play Golf screen brightens again - *Confirmed*
        4. Confirm download status bar is updating during download - *Confirmed*
        - Confirm there is no kind of disruption when download is in process (User shouldn't even know it's occurring, unless icons status is open) - *Confirmed*
        - Confirm download status bar is updating during download - *Confirmed*
        - Confirm when download is complete, icon indicates download was successful - *Confirmed*
        Note: Device will never install an update when waking up from/going into Off Hole sleep (it may when going to sleep, but only if sleep period is very short)
        """
        print()
        print(f"START {__name__}")
        self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_to_update"])  # set que an update APK on Control
        # step 1
        android_utils.cart_of_hole_sleep_mode()  # Put Device in Off Hole Sleep
        # step 2
        MainPage().wait_spinner_to_invisible()
        time.sleep(3)
        assert MainPage().check_menu_button_is_visible() is True, "Play Golf is not loaded"  # check loads application
        # step 3
        MainPage().press_flag_button()
        MainPage().check_view_button_complete_list()  # check button complete is visible
        # step 4
        android_utils.cart_of_hole_sleep_mode()  # Put Device in Off Hole Sleep
        MainPage().wait_spinner_to_invisible()
        time.sleep(3)
        assert MainPage().check_menu_button_is_visible() is True, "Play Golf is not loaded"  # check loads application
        # step 3
        MainPage().press_flag_button()
        MainPage().check_view_button_complete_list()  # check button complete is visible

        print("next step to check")
        check_version = request.config.firmware_version["apk_current"]
        result = self.check_version_installed_ota("APK", request, check_version)
        assert result is True, f"Error: {result}"

        # update_result = self.get_tablet_apk_os_version()  # check version apk on device
        # assert request.config.firmware_version["apk_current"] == update_result["tablet_apk_version"], "Not Confirmed ___"
        # update_info_control = self.get_info_control(request.config.firmware_version["device_id"])
        # assert request.config.firmware_version["apk_current"] == update_info_control["info_app_version"]
        # update_info_360 = self.get_device_info_360(request.config.firmware_version["device_name"])
        # assert request.config.firmware_version["apk_current"] == update_info_360["device_info_apk_version"]
        # return current version APK ___________________________________________________________________________________

        # return current version APK ___________________________________________________________________________________
        # ----------------------------
        self.return_current_version_ota_for_tests("APK", request, off_hole_logic=True)

        print(f"FINISH {__name__}")
        # -----------------------------
        # print("return current version APK ____________________________________________________________")
        # self.remove_app_ota_version(request.config.firmware_version["device_id"])
        # self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_current"])  # set que an update APK on Control
        # android_utils.cart_of_hole_sleep_mode()  # Put Device in Off Hole Sleep
        # MainPage().wait_spinner_to_invisible()
        # time.sleep(3)
        # assert MainPage().check_menu_button_is_visible() is True, "Play Golf is not loaded"  # check loads application
        # MainPage().press_flag_button()
        # assert MainPage().get_text_no_active_downloads() == "There are no active downloads", "Loads APK is not empty"
        #
        # update_result = self.get_tablet_apk_os_version()  # check version apk on device
        # print("---check---")
        # assert request.config.firmware_version["apk_current"] == update_result["tablet_apk_version"], "Not Confirmed update APK version for current version"
        # print(f"FINISH {__name__}")

    @pytest.mark.skip("NOT READY")
    @pytest.mark.wifi
    def test_3_apk_upon_boot_up(self, request) -> None:
        """
        *APK*
        *CASE C: Upon Boot Up*
        1. With device in ship mode/powered off, que an update - *Confirmed*
        2. Confirm device recognizes an update available (via logs, or by tapping the flag to display the download icon status) when powering on - *Confirmed*
        3. Confirm there is no visible interference with the Play Golf/APK while download is taking place - *Confirmed*
        4. Confirm download status bar is updating during download - Note: ER=Unknown for this specific step, I don't believe this will apply - *Confirmed*
        5. Confirm when download is complete, icon indicates download was successful - *Confirmed*
        6. Confirm device installs download upon falling/waking up from sleep - *Confirmed*
        - Confirm updated software version is displayed in APK Asset Details, 360, and Control - *Confirmed*
        """
        print()
        print(f"START {__name__}")
        # MainPage().long_press_key("3")
        # MainPage().press_key(131)

        # self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_to_update"])  # set que an update APK on Control
        # step 1
        # android_utils.cart_burn_sleep_mode()  # Put Device in Cart Burn Sleep
        # time.sleep(10)
        # # step 2
        # # step 3
        # android_utils.wake_up_device()  # Wakeup device from Cart Burn sleep
        # MainPage().wait_spinner_to_invisible()
        # time.sleep(3)
        # assert MainPage().check_menu_button_is_visible() is True, "Play Golf is not loaded"  # check loads application
        # # step 4
        # # step 5
        # MainPage().press_flag_button()
        # # MainPage().check_view_progress_list()
        # MainPage().check_view_button_complete_list()  # check button complete is visible
        # # step 6
        # android_utils.cart_burn_sleep_mode()  # Put Device in Cart Burn Sleep
        # time.sleep(10)
        # android_utils.wake_up_device()  # Wakeup device from Cart Burn sleep
        # MainPage().wait_spinner_to_invisible()
        # time.sleep(40)  # wait for update APK
        #
        # # step to check ________________________________________________________________________________________________
        # print("next step to check")
        # check_version = request.config.firmware_version["apk_to_update"]
        # result = self.check_version_installed_ota("APK", request, check_version)
        # assert result is True, f"Error: {result}"
        #
        # # return current version APK ___________________________________________________________________________________
        # self.return_current_version_ota_for_tests("APK", request)
        #
        print(f"FINISH {__name__}")

    # @pytest.mark.skip
    @pytest.mark.wifi
    def test_4_apk_full_app_resset(self, request) -> None:
        """
        *APK*
        *CASE D: Full App Reset*
        1. With device awake, que an update in Control - *Confirmed*
        2. Select Full App Reset within the APK, Menu options. - *Confirmed*
        3. Confirm the app resets, and checks/loads any updates. Note this process may be a little longer than normal as it is downloading and installing the updated SW version. - *Confirmed*
        4. Confirm app loads completely on Play Golf screen, and does not again reattempt to install software update at a later time. - *Confirmed*
        5. Confirm the device installed the updated software version - *Confirmed*
        - Confirm updated software version is displayed in APK Asset Details, 360, and Control - *Confirmed*
        """
        print()
        print(f"START {__name__}")
        self.set_app_ota_version(request.config.firmware_version["device_id"], request.config.firmware_version["apk_to_update"])  # set que an update APK on Control
        # step 1
        self.device_full_app_reset()  # Full APP Reset
        MainPage().wait_spinner_to_invisible()
        time.sleep(3)
        assert MainPage().check_menu_button_is_visible(), "Play Golf is not loaded"  # check loads application
        # step 2
        MainPage().press_flag_button()
        MainPage().check_view_button_complete_list()  # check button complete is visible
        # step 4
        self.device_full_app_reset()  # Full APP Reset
        MainPage().wait_spinner_to_invisible()
        time.sleep(40)  # wait for update APK
        # step 5
        assert MainPage().check_menu_button_is_visible(), "Play Golf is not loaded"  # check loads application
        MainPage().press_flag_button()
        assert MainPage().get_text_no_active_downloads() == "There are no active downloads", "Loads APK is not empty"

        # step to check ________________________________________________________________________________________________
        print("next step to check")
        check_version = request.config.firmware_version["apk_to_update"]
        result = self.check_version_installed_ota("APK", request, check_version)
        assert result is True, f"Error: {result}"

        # return current version APK ___________________________________________________________________________________
        self.return_current_version_ota_for_tests("APK", request)

        print(f"FINISH {__name__}")

    @pytest.mark.skip("BECAUSE DEBUG")
    @pytest.mark.parametrize("times", list(range(10)))
    def test_debug(self, request, times) -> None:
        update_info_360 = self.get_device_info_360(request.config.firmware_version["device_name"])  # check version apk on 360
        assert request.config.firmware_version["apk_current"] == update_info_360["device_info_apk_version"], "Not Confirmed check version APK on 360"

