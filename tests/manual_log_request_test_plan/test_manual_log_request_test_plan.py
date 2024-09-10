import pytest

from pages_android.main_screen import MainPage
from pages_android.menu_screen import MenuPage
from pages_android.settings_screen import SettingsPage


from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl


class TestManualLogRequest:

    # tests --------------------------------------------------------------------------------------------------
    # Basic Functionality ------------------------------------------------------------------------------------
    @pytest.mark.skip
    @pytest.mark.wifi
    def test_1_request_logs(self):
        """
        1) Confirm in Settings Menu new option to “Request Logs”
        2) Confirm UI
        3) Confirm press to “Request Logs” opens page “Request Logs Files”
        4) Confirm On button tap action it will display zipping progress with ZIPPING FILES IN PROGRESS below Status text view
        5) Confirm display download progress with DOWNLOADING FILES IN PROGRESS status message
        6) Confirm then once it completes everything, it will display LOGS SUCCESSFULLY PROCESSED message
        7) Check Control to verify when logs become available
        8) Review logs to confirm they reflect logs for the requested All days
        """
        ...
