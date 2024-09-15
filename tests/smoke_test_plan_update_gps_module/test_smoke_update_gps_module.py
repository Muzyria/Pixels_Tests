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

from ..config_data import firmware_gps


class TestSmokeUpdateGPSModule:

    @pytest.fixture()
    def get_current_gps_version(self, request):
        print("fixture get current gps version")
        device_gps_version = DeviceScripts.get_tablet_asset_info()["tablet_gps_version"]
        print(f"{device_gps_version=}")
        request.config.firmware_version["device_gps"] = device_gps_version
        request.config.firmware_version["test_data"] = self.get_list_gps_version_ota(device_gps_version)

    @staticmethod
    def get_list_gps_version_ota(device_gps_version: str) -> list:
        another_gps_version = []
        for key, value in firmware_gps.items():
            if device_gps_version not in value:
                another_gps_version.append(value[0])
            else:
                index = value.index(device_gps_version)
                another_gps_version.insert(0, value[1 - index])
        return another_gps_version

    @staticmethod
    def get_name_gps_module(device_gps_version: str) -> str:
        for k, v in firmware_gps.items():
            if device_gps_version in v:
                return k

    # device -----------------------------------------------------------------------------------------------------------
    # tests ------------------------------------------------------------------------------------------------------------

    def test_1_check_version_gps(self, request, get_current_gps_version):
        """
        1) Connect GPS module LC79H (GPS FW 1 - please note current FW version) to the device and confirm:
        - module detected -
        - confirm GPS FW version in Asset Details Yamatrack -
        - confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel  -
        - confirm GPS FW version and GPS type in 360  -
        """
        print()
        print(f"START {request.node.name}")
        assert request.config.firmware_version["device_gps"] is not None

        ControlScripts.login_and_select_device_control(request.config.firmware_version["device_id"])
        device_info_control = ControlScripts.get_info_control()

        assert device_info_control["info_gps_version"] == request.config.firmware_version["device_gps"]
        assert device_info_control["info_gps_module"] == self.get_name_gps_module(request.config.firmware_version["device_gps"])

        device_info_360 = SyncWise360Scripts.get_info_360(request.config.firmware_version["device_name"])
        assert device_info_360["device_info_gps_version"] == request.config.firmware_version["device_gps"]

        print(f"FINISH {request.node.name}")

    # @pytest.mark.skip
    def test_2_update_gps(self, request):
        """
        2) Change in Control Panel GPS FW version GPS module LC79H from FW 1 to from FW 2 note FW version
        - Confirm if GPS module LC79H updated successfuly - *Confirmed*
        - module detected - *Confirmed*
        - confirm GPS FW version in Asset Details Yamatrack - *Confirmed LC79HALNR11A02S*
        - confirm GPS TYPE, GPS FW, GPS MODULE in Control Panel - *Confirmed*
        - confirm GPS FW version and GPS type in 360 - *Confirmed*
        """
        gps_version_to_update = request.config.firmware_version["test_data"][0]

        print()
        print(f"START {request.node.name}")

        print(request.config.firmware_version["test_data"])

        ControlScripts.set_gps_ota_version(request.config.firmware_version["device_id"], gps_version_to_update)  # Set GPS update

        DeviceScripts.reboot_device_and_restart_appium(300)  # Device reboot and install GPS new version

        # check --------------------------------------------------------------------------------------------------------
        device_gps_version = DeviceScripts.get_tablet_asset_info()["tablet_gps_version"]
        assert device_gps_version == gps_version_to_update

        ControlScripts.login_and_select_device_control(request.config.firmware_version["device_id"])
        device_info_control = ControlScripts.get_info_control()

        assert device_gps_version == device_info_control["info_gps_version"]
        assert device_info_control["info_gps_module"] == self.get_name_gps_module(device_gps_version)

        device_info_360 = SyncWise360Scripts.get_info_360(request.config.firmware_version["device_name"])
        assert device_gps_version == device_info_360["device_info_gps_version"]

        ControlScripts.remove_gps_ota_version(request.config.firmware_version["device_id"])

        print(f"FINISH {request.node.name}")

    # @pytest.mark.skip
    def test_3_wrong_update_gps_part_1(self, request):
        """
        3) after step 2 - Change in Control Panel GPS FW version GPS module LC79H to LC79D
        - try update module and confirm if update is not available - Expected - *Confirmed*
        """
        gps_version_to_update = request.config.firmware_version["test_data"][1]
        print()
        print(f"START {request.node.name}")

        print(request.config.firmware_version["test_data"])

        ControlScripts.set_gps_ota_version(request.config.firmware_version["device_id"],
                                           gps_version_to_update)  # Set GPS update

        DeviceScripts.reboot_device_and_restart_appium(120)  # Device reboot and install GPS new version

        # check --------------------------------------------------------------------------------------------------------
        device_gps_version = DeviceScripts.get_tablet_asset_info()["tablet_gps_version"]
        assert device_gps_version == request.config.firmware_version["test_data"][0]

        ControlScripts.login_and_select_device_control(request.config.firmware_version["device_id"])
        device_info_control = ControlScripts.get_info_control()

        assert device_gps_version == device_info_control["info_gps_version"]
        assert device_info_control["info_gps_module"] == self.get_name_gps_module(device_gps_version)

        device_info_360 = SyncWise360Scripts.get_info_360(request.config.firmware_version["device_name"])
        assert device_gps_version == device_info_360["device_info_gps_version"]

        ControlScripts.remove_gps_ota_version(request.config.firmware_version["device_id"])

        print(f"FINISH {request.node.name}")

    # @pytest.mark.skip
    def test_4_wrong_update_gps_part_2(self, request):
        """
        4) after step 3 - Change in Control Panel GPS FW version GPS module LC79D to Ublox
        - try update module and confirm if update is not available - Expected - *Confirmed*
        """
        gps_version_to_update = request.config.firmware_version["test_data"][2]
        print()
        print(f"START {request.node.name}")

        ControlScripts.set_gps_ota_version(request.config.firmware_version["device_id"],
                                           gps_version_to_update)  # Set GPS update

        DeviceScripts.reboot_device_and_restart_appium(120)  # Device reboot and install GPS new version

        # check --------------------------------------------------------------------------------------------------------
        device_gps_version = DeviceScripts.get_tablet_asset_info()["tablet_gps_version"]
        assert device_gps_version == request.config.firmware_version["test_data"][0]

        ControlScripts.login_and_select_device_control(request.config.firmware_version["device_id"])
        device_info_control = ControlScripts.get_info_control()

        assert device_gps_version == device_info_control["info_gps_version"]
        assert device_info_control["info_gps_module"] == self.get_name_gps_module(device_gps_version)

        device_info_360 = SyncWise360Scripts.get_info_360(request.config.firmware_version["device_name"])
        assert device_gps_version == device_info_360["device_info_gps_version"]

        ControlScripts.remove_gps_ota_version(request.config.firmware_version["device_id"])

        print(f"FINISH {request.node.name}")

    @pytest.mark.skip
    def test_debug(self, request):
        print()
        print(f"START {request.node.name}")

        # DeviceScripts.reboot_device_and_restart_appium(120)
        # DeviceScripts.get_tablet_asset_info()
        print(request.config.firmware_version["test_data"])
        print(f"FINISH {request.node.name}")
