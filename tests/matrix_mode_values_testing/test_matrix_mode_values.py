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
from pages_chrome.general_setting_page_360 import GeneralSettingSyncWise360
from pages_chrome.asset_tracker_page_360 import AssetTrackerSyncWise360


import android_utils


class TestMatrixMode:
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
                    output = TestMatrixMode.run_adb_logcat()
                    if message_to_find in output:
                        end_time = time.time()
                        end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                        duration = int(end_time - start_time)
                        print(
                            f"Сообщение '{message_to_find}' найдено в {end_time_readable}, время ожидания: {duration} секунд")
                        TestMatrixMode.log_to_file(f"""*Expected result:*
* {message_to_find}. - *Confirmed at {TestMatrixMode.get_current_time()}*
* No audible signal is emitted. - *Confirmed*\n\n""")
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
    def set_matrix_mode_360(speed_value: str, brake_value: str):
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        CourseMapSyncWise360().click_settings_icon()
        GeneralSettingSyncWise360().click_asset_tracker_button()
        AssetTrackerSyncWise360().click_speed_and_braking_mode_button()

        AssetTrackerSyncWise360().select_dropdown_speed(speed_value)
        AssetTrackerSyncWise360().select_dropdown_brake(brake_value)

        AssetTrackerSyncWise360().click_save_modal_button()
        time.sleep(10)

        LoginPageSyncWise360().click_logout_button()
        time.sleep(3)

    @pytest.mark.parametrize("speed, brake, matrix_mode", [
                    ("10", "Max", "1"),
                    ("11", "Max", "2"),
                    ("12", "Max", "3"),
                    ("13", "Max", "4"),
                    ("14", "Max", "5"),
                    ("10", "High", "6"),
                    ("11", "High", "7"),
                    ("12", "High", "8"),
                    ("13", "High", "9"),
                    ("14", "High", "10"),
                    ("10", "Medium", "11"),
                    ("11", "Medium", "12"),
                    ("12", "Medium", "13"),
                    ("13", "Medium", "14"),
                    ("14", "Medium", "15"),
                    ("10", "Low", "16"),
                    ("11", "Low", "17"),
                    ("12", "Low", "18"),
                    ("13", "Low", "19"),
                    ("14", "Low", "20"),
                    ("10", "Lowest", "21"),
                    ("11", "Lowest", "22"),
                    ("12", "Lowest", "23"),
                    ("13", "Lowest", "24"),
                    ("14", "Lowest", "25"),
    ])
    def test_matrix_mode_check_values(self, request, speed, brake, matrix_mode) -> None:
        print()
        print(f"START {request.node.name}")

        TestMatrixMode.set_matrix_mode_360(speed, brake)
        TestMatrixMode.log_to_file(f"""*Test Case {matrix_mode}: Verifying matrixMode {matrix_mode}*
*Steps:*
# Set the parameters at the site: "Max Speed {speed}", "{brake} Regenerative Braking". - *Confirmed at {TestMatrixMode.get_current_time()}*
# Wait for synchronization with the tablet.
# Verify that CartCommand MATRIX_MODE = {matrix_mode}.
# Verify that no audible signal is emitted.\n""")

        TestMatrixMode.check_for_message(f"CartCommand MATRIX_MODE = {matrix_mode}")
        time.sleep(10)

        print(f"FINISH {request.node.name}")


#  writeEvent level_changed STREAM_MUSIC 3    sound
#  writeEvent level_changed STREAM_MUSIC 7    no sound


    @pytest.mark.debug
    def test_debug(self, request):
        # print()
        print(f"\nSTART {request.node.name}")

        # Открываем страницу и выполняем авторизацию
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        time.sleep(10)  # Ожидаем, пока данные загружаются

        # Завершаем тест
        LoginPageSyncWise360().click_logout_button()
        time.sleep(3)