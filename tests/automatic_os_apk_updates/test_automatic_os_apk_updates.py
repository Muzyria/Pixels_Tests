import pytest
from pages_chrome import PageChrome
import time

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.login_page_control import LoginPageControl


class TestAutomaticOsApkUpdates(PageChrome):
    VALUE = None

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
        print("TEST AUTOMATION first")
        print(f"{self.VALUE=}")
        print(request.config.firmware_version)
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        self.VALUE = 1
        print(request.config.firmware_version)
        time.sleep(10)
        print(f"{self.VALUE=}")
        print(request.config.firmware_version)
        print("open control")
        LoginPageControl.open(LoginPageControl.PAGE_URL)
        LoginPageControl().enter_login().enter_password().click_login_button()
        time.sleep(10)
        print(f"{self.VALUE=}")
        print(request.config.firmware_version)
        print("finish first")

    @pytest.mark.skip
    def test_second(self, request) -> None:
        print("TEST AUTOMATION second")
        print(f"{self.VALUE=}")
        print(request.config.firmware_version)
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()

        time.sleep(10)
        print(f"{self.VALUE=}")
        print(request.config.firmware_version)
        print("finish second")