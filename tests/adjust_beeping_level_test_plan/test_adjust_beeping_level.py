import pytest
from pages_chrome import PageChrome
from pages_android import Page
import time
from datetime import datetime
import subprocess
from framework_appium.driver_appium import DriverAppium

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.coursemap_page_360 import CourseMapSyncWise360
from pages_chrome.device_setup_page_360 import DeviceSetupSyncWise360
from pages_chrome.asset_tracker_page_360 import AssetTrackerSyncWise360

from common_test_steps import DeviceScripts

import android_utils


class TestAdjustBeepingLevel:
    @staticmethod
    def log_to_file(message):
        with open('log.txt', 'a') as log_file:
            log_file.write(message)

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def run_adb_logcat():
        # Запуск команды adb logcat
        process = subprocess.Popen('adb logcat -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        return output.decode('utf-8', errors='ignore')

    @staticmethod
    def check_for_message(message_to_find, interval=30, timeout=600):
        """
        Проверка adb логов на наличие определённого сообщения.

        :param message_to_find: Сообщение, которое необходимо найти.
        :param interval: Интервал в секундах между выполнением команды adb logcat.
        :param timeout: Время ожидания в секундах до прекращения поиска.
        :return: True, если сообщение найдено, False - если тайм-аут истек.
        """

        start_time = time.time()
        start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Начало ожидания сообщения в {start_time_readable}, тайм-аут: {timeout} секунд")

        last_adb_execution_time = 0  # Время последнего выполнения команды

        while time.time() - start_time < timeout:
            current_time = time.time()

            # Выполняем adb logcat с интервалом
            if current_time - last_adb_execution_time >= interval:
                android_utils.swipe_screen_up_to_down()
                android_utils.swipe_screen_down_to_up()

                last_adb_execution_time = current_time
                try:
                    output = TestAdjustBeepingLevel.run_adb_logcat()
                    if message_to_find in output:
                        end_time = time.time()
                        end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                        duration = int(end_time - start_time)
                        print(
                            f"Сообщение '{message_to_find}' найдено в {end_time_readable}, время ожидания: {duration} секунд")
#                         TestAdjustBeepingLevel.log_to_file(f"""*Expected result:*
# * {message_to_find}. - *Confirmed at {TestAdjustBeepingLevel.get_current_time()}*
# * No audible signal is emitted. - *Confirmed*\n\n""")
                        return True
                except Exception as e:
                    print(f"Ошибка при поиске сообщения в логе: {e}")

            # Ждем 1 секунду перед повторной проверкой
            time.sleep(1)
            android_utils.device_send_coordinate("50.08066353581793, 36.23103477093396")

        print(f"Сообщение '{message_to_find}' не найдено за {timeout} секунд.")
        return False

    # 360 ----------------------------------------------------------------------------------------------------
    @staticmethod
    def set_beeping_level_360(beeping_level: str):
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()

        CourseMapSyncWise360().click_button_menu_icon().click_button_menu_icon_device_setup()
        DeviceSetupSyncWise360().select_beeping_level(beeping_level.title())
        DeviceSetupSyncWise360().click_save_button()
        time.sleep(5)

        LoginPageSyncWise360().click_logout_button()
        time.sleep(3)

    @pytest.mark.parametrize("beeping_level", ["high", "medium", "low"])
    def test_adjust_beeping_level(self, request, beeping_level) -> None:
        print()
        print(f"START {request.node.name}")

        TestAdjustBeepingLevel.set_beeping_level_360(beeping_level)
        DeviceScripts.device_full_app_reset()
        time.sleep(10)

        TestAdjustBeepingLevel.check_for_message(f'"beepingLevel":"{beeping_level}"')
        time.sleep(3)

        print(f"FINISH {request.node.name}")


#  writeEvent level_changed STREAM_MUSIC 3    sound
#  writeEvent level_changed STREAM_MUSIC 7    no sound

    @pytest.mark.debug("BECAUSE DEBUG")
    def test_debug(self, request):
        # print()
        print(f"\nSTART {request.node.name}")
        TestAdjustBeepingLevel.set_beeping_level_360("high")
        time.sleep(5)
