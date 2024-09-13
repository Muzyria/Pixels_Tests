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


from common_test_steps import reboot_device_and_restart_appium

class TestSmokeUpdateGPSModule:



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

    # device -----------------------------------------------------------------------------------------------------------
    # @staticmethod
    # def reboot_device_and_restart_appium():
    #     # Device Reboot
    #     DriverAppium.finish()
    #     android_utils.device_reboot()  # Device Reboot
    #     time.sleep(70)  # wait for device reboot
    #     android_utils.wait_for_the_device_to_boot()
    #     DriverAppium.start(android_utils.get_driver_appium_options())
    #     MainPage().wait_map_activity()

    # tests --------------------------------------------------------------------------------------------------


    @pytest.mark.skip
    @pytest.mark.wifi
    def test_(self, request):
        """

        """
        print()
        print(f"START {request.node.name}")

        # --------------------------------------------------------------------------------------------------------------

        print(f"FINISH {request.node.name}")

    # @pytest.mark.skip
    def test_debug(self, request):
        print()
        print(f"START {request.node.name}")

        reboot_device_and_restart_appium()

        print(f"FINISH {request.node.name}")
