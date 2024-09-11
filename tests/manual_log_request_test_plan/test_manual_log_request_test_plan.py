import time

import pytest
import android_utils

from pages_android.main_screen import MainPage
from pages_android.menu_screen import MenuPage
from pages_android.settings_screen import SettingsPage
from pages_android.request_log_files_screen import RequestLogFilesPage


from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl


class TestManualLogRequest:

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
    @staticmethod
    def open_request_log_files():
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        SettingsPage().press_request_log_files_button()

    # tests --------------------------------------------------------------------------------------------------
    # Basic Functionality ------------------------------------------------------------------------------------
    # @pytest.mark.skip
    @pytest.mark.wifi
    def test_1_request_logs(self, request):
        """
        3) Confirm press to “Request Logs” opens page “Request Logs Files”
        4) Confirm On button tap action it will display zipping progress with ZIPPING FILES IN PROGRESS below Status text view
        5) Confirm display download progress with DOWNLOADING FILES IN PROGRESS status message
        6) Confirm then once it completes everything, it will display LOGS SUCCESSFULLY PROCESSED message
        7) Check Control to verify when logs become available
        8) Review logs to confirm they reflect logs for the requested All days
        """
        print()
        print(f"START {request.node.name}")
        # self.open_request_log_files()
        # RequestLogFilesPage().press_request_logs_button()
        #
        # assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
        # RequestLogFilesPage().wait_zipping_files()
        # assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
        # RequestLogFilesPage().wait_downloading_files()
        #
        # assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"
        # check logs ---------------------------------------------------------------------------------------------------

        self.login_and_select_device_control(request.config.firmware_version["device_id"])
        DeviceDetailsPageControl().click_button_logs()
        logs_list = DeviceDetailsPageControl().get_device_logs_list()

        for i in logs_list:
            res = i.text
            print(res[:19])

        time.sleep(5)



        # --------------------------------------------------------------------------------------------------------------
        # RequestLogFilesPage().press_button_cancel()
        # MenuPage().press_play_golf_button()



        print(f"FINISH {request.node.name}")

    @pytest.mark.skip
    def test_debug(self, request):
        print(request.config.firmware_version["device_id"])



