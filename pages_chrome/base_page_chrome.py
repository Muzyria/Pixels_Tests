from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework_chrome.driver_chrome import DriverChrome


class PageChrome:
    wait = WebDriverWait(DriverChrome.chrome_instance, 10, poll_frequency=1)


    @classmethod
    def open(cls, url: str) -> None:
        DriverChrome.chrome_instance.get(url)

    # @classmethod
    # def is_opened(cls):
    #     cls.wait.until(EC.url_to_be(self.PAGE_URL)