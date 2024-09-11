# from config_data import firmware
from ..config_data import firmware
import pytest

from framework_appium.appium import Appium
from framework_appium.driver_appium import DriverAppium
from android_utils import get_udid, get_driver_appium_options

from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options


def pytest_configure(config):
    # Выполняется один раз перед всеми тестами
    config.firmware_version = firmware
    print(f"Устанавливаем глобальную прошивку: {config.firmware_version}")


# def pytest_addoption(parser: pytest.Parser) -> None:
#     parser.addoption('--login', action='store_true', default=False, help='Reset app and login before tests session')


# def login() -> None:
#     reset_app(DriverAppium.app_package)
#     DriverAppium.launch_app()
#     DriverAppium.grant_application_permissions()
#
#     IntroPage().click_login_button()
#     LoginPage().login()


@pytest.fixture(scope='session')
def appium_service():
    Appium.start()
    yield
    Appium.stop()


@pytest.fixture(scope='function', autouse=True)
def driver_appium(appium_service, request: pytest.FixtureRequest):
    print()
    print("__START DRIVER APPIUM__")
    get_udid()
    DriverAppium.start(get_driver_appium_options())

    # DriverAppium.terminate_app()
    # DriverAppium.launch_app()
    yield
    print()
    print("__FINISH DRIVER APPIUM__")
    DriverAppium.finish()


@pytest.fixture(scope='function', autouse=True)
def driver_chrome(request: pytest.FixtureRequest):
    print()
    print("__START DRIVER CHROME for automation__")
    DriverChrome.start(get_driver_chrome_options())
    yield
    print()
    print("__FINISH DRIVER CHROME for automation__")
    DriverChrome.finish()


# @pytest.fixture(scope='function', autouse=True)
# def driver_appium(appium_service, request: pytest.FixtureRequest):
#     print("__START DRIVER APPIUM__")
#     get_udid()
#     DriverAppium.start(get_driver_appium_options())
#     if request.config.option.login:
#         login()
#
#     else:
#         DriverAppium.terminate_app()
#         DriverAppium.launch_app()
#     yield
#     DriverAppium.finish()
