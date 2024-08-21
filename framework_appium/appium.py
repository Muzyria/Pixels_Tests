from appium.webdriver.appium_service import AppiumService


class Appium:
    service = AppiumService()
    # HOST = '0.0.0.0'
    HOST = '127.0.0.1'
    # PORT = '48777'
    PORT = '4723'

    @classmethod
    def start(cls) -> None:
        cls.service.start(
            args=['-a', cls.HOST, '-p', cls.PORT, '--relaxed-security', '--allow-insecure', 'adb_shell']

        )

    @classmethod
    def stop(cls) -> None:
        cls.service.stop()
