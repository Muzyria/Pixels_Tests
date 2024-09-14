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
    @staticmethod
    def get_another_gps_version_ota(device_gps_version: str):
        another_gps_version = ""
        # Список пар значений
        pairs = [
            ('LC79DANR01A06S_BETA0322', 'LC79DANR01A07S'),
            ('LC79HALNR11A01S', 'LC79HALNR11A02S'),
            ('UDR1.00', 'UDR1.31')
        ]

        for pair in pairs:
            if device_gps_version in pair:
                index = pair.index(device_gps_version)
                another_gps_version = pair[1 - index]
                print(f"will select {another_gps_version}")

        return another_gps_version

    # device -----------------------------------------------------------------------------------------------------------

    # tests --------------------------------------------------------------------------------------------------

    # @pytest.mark.skip
    def test_1_update_gps(self, request):
        """
        1) Connect GPS module LC79H (GPS FW 1 - please note current FW version) to the device and confirm:
        - module detected -
        - confirm GPS FW version in Asset Details Yamatrack -
        - confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel  -
        - confirm GPS FW version and GPS type in 360  -
        """
        print()
        print(f"START {request.node.name}")
        # ControlScripts.login_and_select_device_control(request.config.firmware_version["device_id"])
        device_gps_version = DeviceScripts.get_tablet_asset_info()["tablet_gps_version"]
        print(f"{device_gps_version=}")
        request.config.firmware_version["device_gps"] = device_gps_version
        print(request.config.firmware_version)

        self.get_another_gps_version_ota(device_gps_version)


        # --------------------------------------------------------------------------------------------------------------

        print(f"FINISH {request.node.name}")

    @pytest.mark.skip
    def test_debug(self, request):
        print()
        print(f"START {request.node.name}")

        # DeviceScripts.reboot_device_and_restart_appium(120)
        DeviceScripts.get_tablet_asset_info()

        print(f"FINISH {request.node.name}")
