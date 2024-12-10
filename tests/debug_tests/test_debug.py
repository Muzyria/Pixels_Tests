import time

import pytest

from common_test_steps import DeviceScripts
from pages_android.main_screen import MainPage


class TestDebug:
    @pytest.mark.parametrize("i", range(50))
    def test_debug(self, request, i):
        print()
        print(f"START {request.node.name}")

        DeviceScripts.device_full_app_reset()
        MainPage().wait_spinner_to_invisible()
        time.sleep(3)
        assert MainPage().check_menu_button_is_visible(), "Play Golf is not loaded"  # check loads application

        print(f"FINISH {request.node.name}")
