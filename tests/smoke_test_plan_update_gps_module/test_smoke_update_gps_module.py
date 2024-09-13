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


from common_test_steps import DeviceScripts, ControlScripts, SyncWise360Scripts


class TestSmokeUpdateGPSModule:

    # device -----------------------------------------------------------------------------------------------------------

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

        DeviceScripts.reboot_device_and_restart_appium(120)
        DeviceScripts.get_tablet_info()

        print(f"FINISH {request.node.name}")
