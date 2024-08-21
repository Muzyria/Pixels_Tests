import pytest

from pages import IntroPage, LoginPage
from framework.appium import Appium
from framework.driver import Driver
from android_utils import get_driver_options, reset_app


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption('--login', action='store_true', default=False, help='Reset app and login before tests session')


def login() -> None:
    reset_app(Driver.app_package)
    Driver.launch_app()
    Driver.grant_application_permissions()

    IntroPage().click_login_button()
    LoginPage().login()


@pytest.fixture(scope='session')
def appium_service():
    Appium.start()
    yield
    Appium.stop()


@pytest.fixture(scope='function', autouse=True)
def driver(appium_service, request: pytest.FixtureRequest):
    Driver.start(get_driver_options())
    if request.config.option.login:
        login()

    else:
        Driver.terminate_app()
        Driver.launch_app()
    yield
    Driver.finish()
