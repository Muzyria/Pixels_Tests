import pytest
from pages_chrome import PageChrome
from pages_android import Page
import time

from framework_appium.driver_appium import DriverAppium

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.coursemap_page_360 import CourseMapSyncWise360
from pages_chrome.general_setting_page_360 import GeneralSettingSyncWise360
from pages_chrome.asset_tracker_page_360 import AssetTrackerSyncWise360


import android_utils


class TestMatrixMode:

    # 360 ----------------------------------------------------------------------------------------------------
    @staticmethod
    def set_matrix_mode_360():
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        CourseMapSyncWise360().click_settings_icon()
        GeneralSettingSyncWise360().click_asset_tracker_button()
        AssetTrackerSyncWise360().click_speed_and_braking_mode_button()
        AssetTrackerSyncWise360().click_close_modal_button()
        time.sleep(3)
        LoginPageSyncWise360().click_logout_button()
        time.sleep(3)



    def test_matrix_mode_check_values(self, request) -> None:
        print()
        print(f"START {request.node.name}")

        TestMatrixMode.set_matrix_mode_360()

        print(f"FINISH {request.node.name}")
