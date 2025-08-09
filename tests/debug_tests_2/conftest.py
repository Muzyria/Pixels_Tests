
import pytest
from framework_chrome.driver_chrome import DriverChrome
from chrome_utils import get_driver_chrome_options


@pytest.fixture(scope='function', autouse=True)
def driver_chrome(request: pytest.FixtureRequest):
    print()
    print("__START DRIVER CHROME for automation__")
    DriverChrome.start(get_driver_chrome_options())
    yield
    print()
    print("__FINISH DRIVER CHROME for automation__")
    DriverChrome.finish()
