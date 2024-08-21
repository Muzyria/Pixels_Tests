from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from framework.driver import Driver


class Page:

    TIMEOUT = 15

    def find_element_by_id(self, element_id: str):
        resource_id = self._get_resource_id(element_id)
        return self._wait_for_element(AppiumBy.ID, resource_id)

    def find_element_by_xpath(self, xpath: str):
        return self._wait_for_element(AppiumBy.XPATH, xpath)

    @classmethod
    def _wait_for_element(cls, strategy: str, selector: str):
        return WebDriverWait(Driver.appium_instance, cls.TIMEOUT).until(
            expected_conditions.presence_of_element_located((strategy, selector))
        )

    @staticmethod
    def send_keys(element: WebElement, value: str) -> None:
        element.clear().send_keys(value)

    @staticmethod
    def _get_resource_id(element_id: str) -> str:
        return f'{Driver.app_package}:id/{element_id}'
