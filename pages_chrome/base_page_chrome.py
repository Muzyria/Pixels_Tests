from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from framework_chrome.driver_chrome import DriverChrome


class PageChrome:
    TIMEOUT = 30

    @classmethod
    def _get_wait(cls) -> WebDriverWait:
        return WebDriverWait(DriverChrome.chrome_instance, cls.TIMEOUT, poll_frequency=1)

    @classmethod
    def open(cls, url: str) -> None:
        DriverChrome.chrome_instance.get(url)

    @classmethod
    def refresh(cls) -> None:
        DriverChrome.chrome_instance.refresh()

    @classmethod
    def back(cls) -> None:
        DriverChrome.chrome_instance.back()

    @classmethod
    def forward(cls) -> None:
        DriverChrome.chrome_instance.forward()

    @classmethod
    def is_opened(cls, url):
        cls._get_wait().until(EC.url_to_be(url))

    @classmethod
    def close(cls):
        DriverChrome.chrome_instance.close()

    # def wait_for_page_load(self):
    #     self._get_wait().until(
    #         lambda d: d.execute_script("return document.readyState") == "complete"
    #     )
    #     print("__PAGE_IS_LOADED__")

    def visibility_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        return self._get_wait().until(EC.visibility_of_element_located(locator))

    def visibility_of_all_elements_located(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._get_wait().until(EC.visibility_of_all_elements_located(locator))

    def presence_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        return self._get_wait().until(EC.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._get_wait().until(EC.presence_of_all_elements_located(locator))

    def invisibility_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        return self._get_wait().until(EC.invisibility_of_element_located(locator))

    def element_to_be_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self._get_wait().until(EC.element_to_be_clickable(locator))

    @staticmethod
    def go_to_element(element: WebElement) -> None:
        DriverChrome.chrome_instance.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def action_double_click(element: WebElement) -> None:
        action = ActionChains(DriverChrome.chrome_instance)
        action.double_click(element)
        action.perform()

    @staticmethod
    def action_right_click(element: WebElement):
        action = ActionChains(DriverChrome.chrome_instance)
        action.context_click(element)
        action.perform()

    def visibility_of(self, element: WebElement):
        print("visibility_of")
        self._get_wait().until(EC.visibility_of(element))
