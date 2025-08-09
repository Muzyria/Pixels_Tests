import time
import pytest
from common_test_steps import DeviceScripts

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.coursemap_page_360 import CourseMapSyncWise360


class TestDebug2:
    def test_scroll_number(self, request: pytest.FixtureRequest):
        print(f"\nTEST STARTED {request.node.name}")
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()

        CourseMapSyncWise360().click_search_button().click_input_search_asset_name()
        print("CLICK SEARCH BUTTON")
        print("CLICK INPUT ASSET NAME")
        list_names = CourseMapSyncWise360().get_list_of_names_in_input_asset_name()
        print(list_names)
        CourseMapSyncWise360().move_to_select_asset_name_in_list_asset_name("82")




        time.sleep(5)
        print(f"\nTEST PASSED {request.node.name}")
