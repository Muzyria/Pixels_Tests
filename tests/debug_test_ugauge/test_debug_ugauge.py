import time
from datetime import datetime

import pytest
import android_utils

from framework_appium.driver_appium import DriverAppium

from pages_android.main_screen import MainPage


class TestUGauge:
    COORDINATE_MIDDLE_HOLE_1 = "41.12679364191967, -73.85881264988095"
    COORDINATE_GEOFENCE_HOLE_1 = "41.12738003995638, -73.8589761778441"

    @staticmethod
    def run_with_timer(seconds, action):
        end_time = time.time() + seconds
        print("Текущее время начала:", datetime.now().strftime("%H:%M:%S"))
        while time.time() < end_time:
            action()
            time.sleep(0.5)  # задержка
        print("Текущее время окончания:", datetime.now().strftime("%H:%M:%S"))

    @staticmethod
    def set_device_on_hole():
        android_utils.device_send_coordinate(TestUGauge.COORDINATE_MIDDLE_HOLE_1)

    @staticmethod
    def set_device_in_geofence():
        android_utils.device_send_coordinate(TestUGauge.COORDINATE_GEOFENCE_HOLE_1)

    # @pytest.mark.skip
    def test_debug_ugauge(self, request):
        print()
        print(f"START {request.node.name}")

        MainPage.toggle_wifi()
        print(DriverAppium.appium_instance.current_activity)

        self.run_with_timer(30, self.set_device_on_hole)

        self.run_with_timer(10, self.set_device_in_geofence)
        self.run_with_timer(10, self.set_device_on_hole)

        self.run_with_timer(10, self.set_device_in_geofence)
        self.run_with_timer(10, self.set_device_on_hole)

        self.run_with_timer(10, self.set_device_in_geofence)
        self.run_with_timer(10, self.set_device_on_hole)

        self.run_with_timer(10, self.set_device_in_geofence)
        self.run_with_timer(10, self.set_device_on_hole)

        self.run_with_timer(10, self.set_device_in_geofence)
        self.run_with_timer(10, self.set_device_on_hole)



        print("-------------------------------------------------------------------------------------------------READY")
        print("-------------------------------------------------------------------------------------------------READY")
        print("-------------------------------------------------------------------------------------------------READY")
        print("-------------------------------------------------------------------------------------------------READY")
        print("-------------------------------------------------------------------------------------------------READY")
        self.run_with_timer(240, self.set_device_on_hole)
        print("-------------------------------------------------------------------------------------------------WIFI_ON")
        print("-------------------------------------------------------------------------------------------------WIFI_ON")
        print("-------------------------------------------------------------------------------------------------WIFI_ON")
        print("-------------------------------------------------------------------------------------------------WIFI_ON")
        print("-------------------------------------------------------------------------------------------------WIFI_ON")

        MainPage.toggle_wifi()


        print(f"FINISH {request.node.name}")
