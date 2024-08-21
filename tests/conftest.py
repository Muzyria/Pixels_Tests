import pytest

from pages_android import IntroPage, LoginPage
from framework_appium.appium import Appium
from framework_appium.driver_appium import DriverAppium
from android_utils import get_udid, get_driver_appium_options, reset_app


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
    print("__START DRIVER APPIUM__")
    get_udid()
    DriverAppium.start(get_driver_appium_options())

    DriverAppium.terminate_app()
    DriverAppium.launch_app()
    yield
    DriverAppium.finish()

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
