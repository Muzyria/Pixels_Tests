import time
import subprocess
import pytest
import android_utils

from framework_appium.driver_appium import DriverAppium

from pages_android.main_screen import MainPage
from pages_android.menu_screen import MenuPage
from pages_android.settings_screen import SettingsPage
from pages_android.asset_details_screen import AssetDetailsPage

from pages_android.uua_main_screen import UUAMainPage
from pages_android.uua_update_firmware_screen import UUAUpdateFirmwarePage

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options

from pages_chrome.login_page_360 import LoginPageSyncWise360
from pages_chrome.coursemap_page_360 import CourseMapSyncWise360
from pages_chrome.assets_page_360 import AssetsSyncWise360

from pages_chrome.login_page_control import LoginPageControl
from pages_chrome.superior_page_control import SuperiorPageControl
from pages_chrome.device_details_page_control import DeviceDetailsPageControl


class DeviceScripts:
    @staticmethod
    def restart_appium(func):
        def inner(*args, **kwargs):
            DriverAppium.finish()
            func(*args, **kwargs)
            DriverAppium.start(android_utils.get_driver_appium_options())
        return inner

    @staticmethod
    def reboot_device_and_restart_appium(wait_time: int = 70) -> None:
        """Device Reboot and restart appium (for update GPS use time 300 and 120)"""
        # Device Reboot
        DriverAppium.finish()
        android_utils.device_reboot()  # Device Reboot
        time.sleep(wait_time)  # wait for device reboot
        android_utils.wait_for_the_device_to_boot()
        DriverAppium.start(android_utils.get_driver_appium_options())
        MainPage().wait_map_activity()

    @staticmethod
    def device_full_app_reset():
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        android_utils.swipe_screen_down_to_up()
        SettingsPage().press_full_app_reset_button()
        SettingsPage().press_button_yes()

    @staticmethod
    def get_tablet_asset_info() -> dict:
        """
        return device asset info
        """
        MainPage().press_menu_button()
        MenuPage().press_settings_button()
        SettingsPage().enter_settings_password()
        SettingsPage().press_assets_details_button()

        tablet_os_version = AssetDetailsPage().get_os_version()
        tablet_apk_version = AssetDetailsPage().get_apk_version()
        tablet_cable_version = AssetDetailsPage().get_cable_version()
        tablet_gps_version = AssetDetailsPage().get_gps_version()

        # print(f'{tablet_os_version=} {tablet_apk_version=} {tablet_cable_version} {tablet_gps_version}')
        AssetDetailsPage().press_button_cancel()
        SettingsPage().press_button_cancel()
        MenuPage().press_play_golf_button()
        return {"tablet_os_version": tablet_os_version,
                "tablet_apk_version": tablet_apk_version,
                "tablet_cable_version": tablet_cable_version,
                "tablet_gps_version": tablet_gps_version}


class LogcatMethods:
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
                # self.adb_command.swipe_screen(100, 500, 200, 500, 250)
                # self.adb_command.swipe_screen(200, 500, 100, 500, 250)
                print("-----ADB COMMAND----------------------------------------------")
                last_adb_execution_time = current_time
                try:
                    output = LogcatMethods.run_adb_logcat()
                    if message_to_find in output:
                        end_time = time.time()
                        end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                        duration = int(end_time - start_time)
                        print(
                            f"Сообщение '{message_to_find}' найдено в {end_time_readable}, время ожидания: {duration} секунд")
                        return True
                except Exception as e:
                    print(f"Ошибка при поиске сообщения в логе: {e}")

            # Ждем 1 секунду перед повторной проверкой
            time.sleep(1)

        print(f"Сообщение '{message_to_find}' не найдено за {timeout} секунд.")
        return False



class ControlScripts:
    @staticmethod
    def login_and_select_device_control(device_id: str) -> None:
        """login on site Control and select device manager"""
        LoginPageControl.open(LoginPageControl.PAGE_URL)  # open Control
        LoginPageControl().enter_login().enter_password().click_login_button()  # check URL
        LoginPageControl.is_opened(LoginPageControl.MAIN_PAGE)
        SuperiorPageControl.open(SuperiorPageControl.PAGE_URL)  # open Superior
        SuperiorPageControl.is_opened(SuperiorPageControl.PAGE_URL)  # check URL
        SuperiorPageControl().click_button_device_manager()
        SuperiorPageControl().click_device_id_in_box(device_id)
        time.sleep(5)

    @staticmethod
    def get_info_control() -> dict[str, str]:
        """return info about device OS, APK, GPS version and GPS Module"""
        DeviceDetailsPageControl().click_button_info()
        # get info
        info_fw_version = DeviceDetailsPageControl().get_info_fw_version()
        info_app_version = DeviceDetailsPageControl().get_info_app_version()
        info_gps_version = DeviceDetailsPageControl().get_info_gps_version()
        info_gps_module = DeviceDetailsPageControl().get_info_gps_module()
        print(f"{info_fw_version=} {info_app_version=} {info_gps_version=} {info_gps_module=}")

        LoginPageControl().click_logout_button()
        time.sleep(3)
        return {"info_os_version": info_fw_version,
                "info_app_version": info_app_version,
                "info_gps_version": info_gps_version,
                "info_gps_module": info_gps_module
                }

    @staticmethod
    def set_gps_ota_version(device_id: str, gps_version: str) -> None:
        gps_version = gps_version.replace(" ", "")
        print(f"_____OTA GPS {gps_version=}")
        ControlScripts.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_gps_version(gps_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set gps ota version {gps_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def set_os_ota_version(device_id: str, os_version: str) -> None:
        ControlScripts.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_os_version(os_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set os ota version {os_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def set_app_ota_version(device_id: str, app_version: str) -> None:
        """Set que an update APK on Control"""
        ControlScripts.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        DeviceDetailsPageControl().select_app_version(app_version)
        DeviceDetailsPageControl().click_button_save_version_ota()
        print(f"set app ota version {app_version} for device {device_id} complete")
        time.sleep(5)
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def remove_os_ota_version(device_id: str) -> None:
        ControlScripts.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        if DeviceDetailsPageControl().check_button_remove_os_is_displayed():
            DeviceDetailsPageControl().click_button_remove_os_update()
            time.sleep(2)
            print()
            print("REMOVE OS UPDATE IS DONE")
        else:
            print()
            print("REMOVE OS UPDATE IS NOT AVAILABLE")
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def remove_app_ota_version(device_id: str) -> None:
        ControlScripts.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        if DeviceDetailsPageControl().check_button_remove_app_is_displayed():
            DeviceDetailsPageControl().click_button_remove_app_update()
            time.sleep(2)
            print()
            print("REMOVE APP UPDATE IS DONE")
        else:
            print()
            print("REMOVE APP UPDATE IS NOT AVAILABLE")
        LoginPageControl().click_logout_button()
        time.sleep(3)

    @staticmethod
    def remove_gps_ota_version(device_id: str) -> None:
        ControlScripts.login_and_select_device_control(device_id)
        DeviceDetailsPageControl().click_button_edit_version_ota()
        if DeviceDetailsPageControl().check_button_remove_gps_is_displayed():
            DeviceDetailsPageControl().click_button_remove_gps_update()
            time.sleep(2)
            print()
            print("REMOVE GPS UPDATE IS DONE")
        else:
            print()
            print("REMOVE GPS UPDATE IS NOT AVAILABLE")
        LoginPageControl().click_logout_button()
        time.sleep(3)


class SyncWise360Scripts:

    @staticmethod
    def get_info_360(device_name: str) -> dict[str, str]:
        """return info about device OS, APK, GPS version and GPS Module"""
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        LoginPageSyncWise360().enter_login().enter_password().click_login_button()
        CourseMapSyncWise360().click_assets_button()
        AssetsSyncWise360().click_name_car_in_list(device_name)
        CourseMapSyncWise360().click_tab_asset_details()
        # get device info
        device_info_os_version = CourseMapSyncWise360().get_device_info_os_version()
        device_info_apk_version = CourseMapSyncWise360().get_device_info_apk_version()
        device_info_gps_version = CourseMapSyncWise360().get_device_info_gps_version()
        device_info_cable_version = CourseMapSyncWise360().get_device_info_cable_version()
        print(f"{device_info_os_version=} {device_info_apk_version=} {device_info_gps_version=} {device_info_cable_version=}")

        LoginPageSyncWise360().click_logout_button()
        time.sleep(3)
        return {"device_info_os_version": device_info_os_version,
                "device_info_apk_version": device_info_apk_version,
                "device_info_gps_version": device_info_gps_version,
                "device_info_cable_version": device_info_cable_version
                }

