from contextlib import suppress

from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from appium.webdriver.appium_connection import AppiumConnection
from selenium.common.exceptions import WebDriverException

from framework_appium.appium import Appium


class DriverAppium:
    app_package = "com.l1inc.yamatrack3d"
    appium_instance: Remote = None

    @classmethod
    def start(cls, options: UiAutomator2Options) -> None:
        print("__start_appium__")
        cls.appium_instance = Remote(AppiumConnection(f'{Appium.HOST}:{Appium.PORT}'), options=options)

    @classmethod
    def finish(cls) -> None:
        # cls.appium_instance.terminate_app(cls.app_package)
        print("__finish_apium__")
        cls.appium_instance.quit()
        cls.appium_instance = None

    @classmethod
    def launch_app(cls, app_package: str = None) -> None:
        if app_package:
            cls.appium_instance.activate_app(app_package)
        else:
            cls.appium_instance.activate_app(cls.app_package)

    @classmethod
    def terminate_app(cls, app_package: str = None) -> None:
        if app_package:
            with suppress(WebDriverException):
                cls.appium_instance.terminate_app(app_package)
        else:
            with suppress(WebDriverException):
                cls.appium_instance.terminate_app(cls.app_package)

    @classmethod
    def grant_application_permissions(cls) -> None:
        permissions = [
            'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'READ_EXTERNAL_STORAGE',
            'WRITE_EXTERNAL_STORAGE', 'CAMERA', 'READ_CONTACTS'
        ]
        platform_version = cls.appium_instance.capabilities['platformVersion']

        if int(platform_version) >= 10:
            permissions.append('ACCESS_BACKGROUND_LOCATION')

        if int(platform_version) >= 13:
            permissions.append('POST_NOTIFICATIONS')

        for permission in permissions:
            with suppress(WebDriverException):
                cls.appium_instance.execute_script(
                    'mobile: shell',
                    {'command': 'pm grant', 'args': [f'{cls.app_package} android.permission.{permission}']}
                )
