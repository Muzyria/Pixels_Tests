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


class TestManualLogRequest:

    @staticmethod
    def get_start_list_logs(request):
        TestManualLogRequest.login_and_select_device_control(request.config.firmware_version["device_id"])
        DeviceDetailsPageControl().click_button_logs()
        logs_list = DeviceDetailsPageControl().get_device_logs_list()
        res_dict = {k: v.text[:19] for k, v in enumerate(logs_list, 1)}
        request.cls.log_files.update(res_dict)

        LoginPageControl().click_logout_button()
        # time.sleep(3)

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

    # WIFI -------------------------------------------------------------------------------------------------------------
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
        self.get_start_list_logs(request)
        start_count_items_logs = len(request.cls.log_files)

        self.open_request_log_files()
        RequestLogFilesPage().press_request_logs_button()

        assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
        RequestLogFilesPage().wait_zipping_files()
        assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
        RequestLogFilesPage().wait_downloading_files()

        assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"

        # check logs ---------------------------------------------------------------------------------------------------

        self.get_start_list_logs(request)
        assert len(request.cls.log_files) == start_count_items_logs + 1

        # --------------------------------------------------------------------------------------------------------------
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()

        request.cls.log_files = {}

        print(f"FINISH {request.node.name}")

    # @pytest.mark.skip
    @pytest.mark.wifi
    def test_2_request_logs_exit_menu(self, request):
        """
        1) Press "Request Logs"
        2) After process begins exit menu
        3) Re-enter menu and confirm unable to select "Request Logs"
        4) Confirm APK shows current progress/status of Log process
        5) Confirm logs are uploaded to Control
        6) Review logs to confirm they reflect logs for the requested All days
        """
        print()
        print(f"START {request.node.name}")
        self.get_start_list_logs(request)
        start_count_items_logs = len(request.cls.log_files)

        self.open_request_log_files()
        RequestLogFilesPage().press_request_logs_button()
        # step 1

        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()
        # step 2

        self.open_request_log_files()

        assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
        RequestLogFilesPage().wait_zipping_files()
        assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
        RequestLogFilesPage().wait_downloading_files()

        assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"

        # check logs ---------------------------------------------------------------------------------------------------

        self.get_start_list_logs(request)
        assert len(request.cls.log_files) == start_count_items_logs + 1

        # --------------------------------------------------------------------------------------------------------------
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()

        request.cls.log_files = {}

        print(f"FINISH {request.node.name}")

    @pytest.mark.skip
    @pytest.mark.wifi
    def test_3_request_logs_network_disconnected(self, request):
        """
        1) Press "Request Logs"
        2) Confirm zipping progress
        3) Confirm zipping progress completed
        4) Allow device to begin download process, cut network connection (Faraday Cage, Airplane mode, etc)
        5) Confirm if logs appear in Control
        6) Review logs to confirm they reflect logs for he requested All days
        """
        print()
        print(f"START {request.node.name}")
        self.get_start_list_logs(request)
        start_count_items_logs = len(request.cls.log_files)

        self.open_request_log_files()
        RequestLogFilesPage().press_request_logs_button()
        # step 1

        assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
        # step 2
        RequestLogFilesPage().wait_zipping_files()
        # step 3

        time.sleep(3)
        RequestLogFilesPage.toggle_wifi()  # OFF WIFI
        print("Wi-Fi OFF")
        time.sleep(10)
        RequestLogFilesPage.toggle_wifi()  # ON WIFI
        print("Wi-Fi ON")

        assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
        RequestLogFilesPage().wait_downloading_files()

        assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"

        # check logs ---------------------------------------------------------------------------------------------------

        self.get_start_list_logs(request)
        assert len(request.cls.log_files) == start_count_items_logs + 1

        # --------------------------------------------------------------------------------------------------------------
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()

        request.cls.log_files = {}

        print(f"FINISH {request.node.name}")

    @pytest.mark.skip
    @pytest.mark.wifi
    def test_4_request_logs_cut_power_to_device(self, request):
        """
        1) Press "Request Logs"
        2) Confirm Request Log process begins
        3) During middle of process turn off device Disconnect battery
        4) Turn device on
        5) Enter "Request Logs" menu
        6) Confirm if Request Log process is still going
        7) Confirm if logs appear in Control
        8) Review logs to confirm they reflect logs for he requested All days
        """
        print()
        print(f"START {request.node.name}")
        self.get_start_list_logs(request)
        start_count_items_logs = len(request.cls.log_files)

        self.open_request_log_files()
        RequestLogFilesPage().press_request_logs_button()
        # step 1
        assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"

        # step 2

        # reboot device
        DriverAppium.finish()
        android_utils.device_reboot()  # Device Reboot
        time.sleep(70)  # wait for device reboot
        android_utils.wait_for_the_device_to_boot()
        print("TRY TO CHECK BOOT DEVICE")
        DriverAppium.start(android_utils.get_driver_appium_options())
        MainPage().wait_map_activity()
        # step 3
        # step 4

        self.open_request_log_files()

        RequestLogFilesPage().wait_zipping_files()

        assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
        RequestLogFilesPage().wait_downloading_files()

        assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"

        # check logs ---------------------------------------------------------------------------------------------------

        self.get_start_list_logs(request)
        assert len(request.cls.log_files) == start_count_items_logs + 1

        # --------------------------------------------------------------------------------------------------------------
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()

        request.cls.log_files = {}

        print(f"FINISH {request.node.name}")

    # @pytest.mark.skip
    @pytest.mark.wifi
    def test_5_request_logs_exit_application(self, request):
        """
        1) Press "Request Logs"
        2) Confirm Request Log process begins
        3) During middle of process exit application via Asset Details Exit APK
        4) Open YamaTrack Open
        5) Enter Request Logs menu
        6) Confirm if Request Logs process is still executing Confirm Request Logs process still executing
        7) Confirm if logs appear in Control
        8) Review logs to confirm they reflect logs for he requested All days
        """
        print()
        print(f"START {request.node.name}")
        self.get_start_list_logs(request)
        start_count_items_logs = len(request.cls.log_files)

        self.open_request_log_files()
        RequestLogFilesPage().press_request_logs_button()
        # step 1
        assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"

        # step 2

        # Close application
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        SettingsPage().press_exit_application_button()
        SettingsPage().press_button_yes()

        print("APPLICATION IS CLOSED")

        # Open application
        DriverAppium.launch_app()
        MainPage().wait_map_activity()
        self.open_request_log_files()

        RequestLogFilesPage().wait_zipping_files()
        assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
        RequestLogFilesPage().wait_downloading_files()

        assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"

        # check logs ---------------------------------------------------------------------------------------------------

        self.get_start_list_logs(request)
        assert len(request.cls.log_files) >= start_count_items_logs + 1

        # --------------------------------------------------------------------------------------------------------------
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()

        request.cls.log_files = {}

        # wait for double downloads ------------------------------------------------------------------------------------
        self.open_request_log_files()
        RequestLogFilesPage().wait_zipping_files()
        RequestLogFilesPage().wait_downloading_files()
        RequestLogFilesPage().press_button_cancel()
        MenuPage().press_play_golf_button()
        # --------------------------------------------------------------------------------------------------------------

        print(f"FINISH {request.node.name}")

    @pytest.mark.skip("BECAUSE DEBUG")
    def test_debug(self, request):
        print()
        print(f"START {request.node.name}")

        print(request.cls.log_files)
        print(len(request.cls.log_files))
        MainPage.toggle_wifi()

        print(f"FINISH {request.node.name}")

    # CELL -------------------------------------------------------------------------------------------------------------
    # @pytest.mark.cell
    # def test_1_request_logs_cell(self, request):
    #     """
    #     3) Confirm press to “Request Logs” opens page “Request Logs Files”
    #     4) Confirm On button tap action it will display zipping progress with ZIPPING FILES IN PROGRESS below Status text view
    #     5) Confirm display download progress with DOWNLOADING FILES IN PROGRESS status message
    #     6) Confirm then once it completes everything, it will display LOGS SUCCESSFULLY PROCESSED message
    #     7) Check Control to verify when logs become available
    #     8) Review logs to confirm they reflect logs for the requested All days
    #     """
    #     print()
    #     print(f"START {request.node.name}")
    #     self.get_start_list_logs(request)
    #     start_count_items_logs = len(request.cls.log_files)
    #
    #     self.open_request_log_files()
    #     RequestLogFilesPage().press_request_logs_button()
    #
    #     assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_zipping_files()
    #     assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_downloading_files()
    #
    #     assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"
    #
    #     # check logs ---------------------------------------------------------------------------------------------------
    #
    #     self.get_start_list_logs(request)
    #     assert len(request.cls.log_files) == start_count_items_logs + 1
    #
    #     # --------------------------------------------------------------------------------------------------------------
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #
    #     request.cls.log_files = {}
    #
    #     print(f"FINISH {request.node.name}")
    #
    # # @pytest.mark.skip
    # @pytest.mark.cell
    # def test_2_request_logs_exit_menu_cell(self, request):
    #     """
    #     1) Press "Request Logs"
    #     2) After process begins exit menu
    #     3) Re-enter menu and confirm unable to select "Request Logs"
    #     4) Confirm APK shows current progress/status of Log process
    #     5) Confirm logs are uploaded to Control
    #     6) Review logs to confirm they reflect logs for the requested All days
    #     """
    #     print()
    #     print(f"START {request.node.name}")
    #     self.get_start_list_logs(request)
    #     start_count_items_logs = len(request.cls.log_files)
    #
    #     self.open_request_log_files()
    #     RequestLogFilesPage().press_request_logs_button()
    #     # step 1
    #
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #     # step 2
    #
    #     self.open_request_log_files()
    #
    #     assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_zipping_files()
    #     assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_downloading_files()
    #
    #     assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"
    #
    #     # check logs ---------------------------------------------------------------------------------------------------
    #
    #     self.get_start_list_logs(request)
    #     assert len(request.cls.log_files) == start_count_items_logs + 1
    #
    #     # --------------------------------------------------------------------------------------------------------------
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #
    #     request.cls.log_files = {}
    #
    #     print(f"FINISH {request.node.name}")
    #
    # # @pytest.mark.skip
    # @pytest.mark.cell
    # def test_3_request_logs_network_disconnected_cell(self, request):
    #     """
    #     1) Press "Request Logs"
    #     2) Confirm zipping progress
    #     3) Confirm zipping progress completed
    #     4) Allow device to begin download process, cut network connection (Faraday Cage, Airplane mode, etc)
    #     5) Confirm if logs appear in Control
    #     6) Review logs to confirm they reflect logs for he requested All days
    #     """
    #     print()
    #     print(f"START {request.node.name}")
    #     self.get_start_list_logs(request)
    #     start_count_items_logs = len(request.cls.log_files)
    #
    #     self.open_request_log_files()
    #     RequestLogFilesPage().press_request_logs_button()
    #     # step 1
    #
    #     assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
    #     # step 2
    #     RequestLogFilesPage().wait_zipping_files()
    #     # step 3
    #
    #     time.sleep(3)
    #     RequestLogFilesPage.toggle_wifi()  # OFF WIFI
    #     print("Wi-Fi OFF")
    #     time.sleep(10)
    #     RequestLogFilesPage.toggle_wifi()  # ON WIFI
    #     print("Wi-Fi ON")
    #
    #     assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_downloading_files()
    #
    #     assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"
    #
    #     # check logs ---------------------------------------------------------------------------------------------------
    #
    #     self.get_start_list_logs(request)
    #     assert len(request.cls.log_files) == start_count_items_logs + 1
    #
    #     # --------------------------------------------------------------------------------------------------------------
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #
    #     request.cls.log_files = {}
    #
    #     print(f"FINISH {request.node.name}")
    #
    # # @pytest.mark.skip
    # @pytest.mark.cell
    # def test_4_request_logs_cut_power_to_device_cell(self, request):
    #     """
    #     1) Press "Request Logs"
    #     2) Confirm Request Log process begins
    #     3) During middle of process turn off device Disconnect battery
    #     4) Turn device on
    #     5) Enter "Request Logs" menu
    #     6) Confirm if Request Log process is still going
    #     7) Confirm if logs appear in Control
    #     8) Review logs to confirm they reflect logs for he requested All days
    #     """
    #     print()
    #     print(f"START {request.node.name}")
    #     self.get_start_list_logs(request)
    #     start_count_items_logs = len(request.cls.log_files)
    #
    #     self.open_request_log_files()
    #     RequestLogFilesPage().press_request_logs_button()
    #     # step 1
    #     assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
    #
    #     # step 2
    #
    #     # reboot device
    #     DriverAppium.finish()
    #     android_utils.device_reboot()  # Device Reboot
    #     time.sleep(70)  # wait for device reboot
    #     android_utils.wait_for_the_device_to_boot()
    #     print("TRY TO CHECK BOOT DEVICE")
    #     DriverAppium.start(android_utils.get_driver_appium_options())
    #     MainPage().wait_map_activity()
    #     # step 3
    #     # step 4
    #
    #     self.open_request_log_files()
    #
    #     RequestLogFilesPage().wait_zipping_files()
    #
    #     assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_downloading_files()
    #
    #     assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"
    #
    #     # check logs ---------------------------------------------------------------------------------------------------
    #
    #     self.get_start_list_logs(request)
    #     assert len(request.cls.log_files) == start_count_items_logs + 1
    #
    #     # --------------------------------------------------------------------------------------------------------------
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #
    #     request.cls.log_files = {}
    #
    #     print(f"FINISH {request.node.name}")
    #
    # # @pytest.mark.skip
    # @pytest.mark.cell
    # def test_5_request_logs_exit_application_cell(self, request):
    #     """
    #     1) Press "Request Logs"
    #     2) Confirm Request Log process begins
    #     3) During middle of process exit application via Asset Details Exit APK
    #     4) Open YamaTrack Open
    #     5) Enter Request Logs menu
    #     6) Confirm if Request Logs process is still executing Confirm Request Logs process still executing
    #     7) Confirm if logs appear in Control
    #     8) Review logs to confirm they reflect logs for he requested All days
    #     """
    #     print()
    #     print(f"START {request.node.name}")
    #     self.get_start_list_logs(request)
    #     start_count_items_logs = len(request.cls.log_files)
    #
    #     self.open_request_log_files()
    #     RequestLogFilesPage().press_request_logs_button()
    #     # step 1
    #     assert RequestLogFilesPage().get_text_view_status() == "ZIPPING FILES IN PROGRESS"
    #
    #     # step 2
    #
    #     # Close application
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_settings_button()
    #     SettingsPage().enter_settings_password()
    #     SettingsPage().press_exit_application_button()
    #     SettingsPage().press_button_yes()
    #
    #     print("APPLICATION IS CLOSED")
    #
    #     # Open application
    #     DriverAppium.launch_app()
    #     MainPage().wait_map_activity()
    #     self.open_request_log_files()
    #
    #     RequestLogFilesPage().wait_zipping_files()
    #     assert RequestLogFilesPage().get_text_view_status() == "DOWNLOADING FILES IN PROGRESS"
    #     RequestLogFilesPage().wait_downloading_files()
    #
    #     assert RequestLogFilesPage().get_text_view_updated_message() == "LOGS SUCCESSFULLY\nPROCESSED"
    #
    #     # check logs ---------------------------------------------------------------------------------------------------
    #
    #     self.get_start_list_logs(request)
    #     assert len(request.cls.log_files) >= start_count_items_logs + 1
    #
    #     # --------------------------------------------------------------------------------------------------------------
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #
    #     request.cls.log_files = {}
    #
    #     # wait for double downloads ------------------------------------------------------------------------------------
    #     self.open_request_log_files()
    #     RequestLogFilesPage().wait_zipping_files()
    #     RequestLogFilesPage().wait_downloading_files()
    #     RequestLogFilesPage().press_button_cancel()
    #     MenuPage().press_play_golf_button()
    #     # --------------------------------------------------------------------------------------------------------------
    #
    #     print(f"FINISH {request.node.name}")