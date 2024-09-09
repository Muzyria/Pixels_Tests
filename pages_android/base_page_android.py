import subprocess
import time

from appium.webdriver import WebElement

# from appium.webdriver.common.appiumby import AppiumBy


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction


from framework_appium.driver_appium import DriverAppium


class Page:

    TIMEOUT = 60

    @classmethod
    def _wait(cls) -> WebDriverWait:
        return WebDriverWait(DriverAppium.appium_instance, cls.TIMEOUT)

    # def find_element_by_id(self, element_id: str):
    #     resource_id = self._get_resource_id(element_id)
    #     return self._wait_for_element(AppiumBy.ID, resource_id)
    #
    # def find_element_by_xpath(self, xpath: str):
    #     return self._wait_for_element(AppiumBy.XPATH, xpath)

    # @classmethod
    # def _wait_for_element(cls, strategy: str, selector: str):
    #     return WebDriverWait(DriverAppium.appium_instance, cls.TIMEOUT).until(
    #         expected_conditions.presence_of_element_located((strategy, selector))
    #     )

    # @staticmethod
    # def send_keys(element: WebElement, value: str) -> None:
    #     element.clear().send_keys(value)
    #
    # @staticmethod
    # def _get_resource_id(element_id: str) -> str:
    #     print(f'{DriverAppium.app_package}:id/{element_id}')
    #     print("com.l1inc.yamatrack3d:id/buttonMenu")
    #     return f'{DriverAppium.app_package}:id/{element_id}'

    # --------------------------------------------------------------------------------------------

    def visibility_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        return self._wait().until(EC.visibility_of_element_located(locator))

    def visibility_of_all_elements_located(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._wait().until(EC.visibility_of_all_elements_located(locator))

    def presence_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        return self._wait().until(EC.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._wait().until(EC.presence_of_all_elements_located(locator))

    def invisibility_of_element_located(self, locator: tuple[str, str]) -> WebElement:
        return self._wait().until(EC.invisibility_of_element_located(locator))

    def invisibility_of_element(self, locator: tuple[str, str]) -> WebElement:
        return self._wait().until(EC.invisibility_of_element(locator))

    def element_to_be_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self._wait().until(EC.element_to_be_clickable(locator))

    @staticmethod
    def get_name_current_activity() -> str:
        """return name activity"""
        return DriverAppium.appium_instance.current_activity

    @staticmethod
    def toggle_wifi():
        DriverAppium.appium_instance.toggle_wifi()
        print("toggle wifi")

    @staticmethod
    def get_network_connection() -> int:
        """return name connection
        0 — нет соединения.
        1 — только самолетный режим.
        2 — только Wi-Fi.
        4 — только мобильные данные.
        5 - самолетный режим и зпрет передачи по мобильным данным
        6 — Wi-Fi и мобильные данные.
        7 — Wi-Fi, мобильные данные с запретом передачи и самолетный режим включены одновременно.
        """
        return DriverAppium.appium_instance.network_connection

    @staticmethod
    def find_element(locator):
        return DriverAppium.appium_instance.find_element(*locator)

    @staticmethod
    def find_elements(locator):
        return DriverAppium.appium_instance.find_elements(*locator)

    @staticmethod
    def wait_activity(name_activity: str, timeout: int) -> bool:
        """Wait for an activity"""
        return DriverAppium.appium_instance.wait_activity(name_activity, timeout)

    @staticmethod
    def swipe(x1=500, y1=700, x2=500, y2=100, speed=250):
        DriverAppium.appium_instance.swipe(x1, y1, x2, y2, speed)

    @staticmethod
    def long_press_key(key: int | str) -> None:
        """
        MAIN_BUTTON = 3 #
        """
        DriverAppium.appium_instance.long_press_keycode(key)
        # DriverAppium.appium_instance.toggle_wifi()

    @staticmethod
    def press_key(key: int | str) -> None:
        """
        MENU = 187
        EMERGENCY = 4
        MAIN_BUTTON = 3 #
        VOLUME = 24, 25
        BLUETOOTH = 131
        """
        DriverAppium.appium_instance.press_keycode(key)

    @staticmethod
    def save_screenshot(file_name, extra_name=''):     # Пример использования: self.save_screenshot('screenshot')
        path_directory = 'tests/automatic_os_apk_updates/screenshots/'
        try:
            DriverAppium.appium_instance.save_screenshot(f"{path_directory}{file_name}{extra_name}.jpg")
            print(f"Screenshot is saved: {file_name}")
        except Exception as e:
            print(f"Error when creating a screenshot: {e}")

    # ------------------------------------------------------------------------------------------------------------------

    # def touch_action(self, coordinate):
    #     action = TouchAction(self.appium_driver)
    #     action.tap(x=coordinate[0], y=coordinate[1]).perform()
    #
    # def swipe_screen_with_coordinate(self, start_coordinate=None, end_coordinate=None, duration=1000):  # Продолжительность свайпа в миллисекундах
    #     print(self.appium_driver.get_window_size()['width'])
    #     print(self.appium_driver.get_window_size()['height'])
    #     self.appium_driver.swipe(start_coordinate[0], start_coordinate[1], end_coordinate[0], end_coordinate[1], duration)
    #
    # def swipe_screen_down(self, duration=200):  # Продолжительность свайпа в миллисекундах
    #     start_x = self.appium_driver.get_window_size()['width'] // 2
    #     start_y = self.appium_driver.get_window_size()['height'] * 0.8
    #     end_y = self.appium_driver.get_window_size()['height'] * 0.2
    #     self.appium_driver.swipe(start_x, start_y, start_x, end_y, duration)  # Прокрутка вниз
    #     time.sleep(1)
    #
    # def swipe_screen_up(self, duration=200):  # Продолжительность свайпа в миллисекундах
    #     start_x = self.appium_driver.get_window_size()['width'] // 2
    #     start_y = self.appium_driver.get_window_size()['height'] * 0.8
    #     end_y = self.appium_driver.get_window_size()['height'] * 0.2
    #     self.appium_driver.swipe(start_x, end_y, start_x, start_y, duration)  # Прокрутка вверх
    #     time.sleep(1)
    #
    #
    # def take_element_screenshot(self, locator, file_name, extra_name=''): # Пример использования:  # self.take_element_screenshot((MobileBy.ID, 'element_id'), 'element_screenshot.png')
    #     path_directory = 'screenshots/'
    #     try:
    #         element = self.element_is_visible(locator)
    #         element.screenshot(f"{path_directory}{file_name}{extra_name}.jpg")
    #         print(f"Скриншот элемента сохранен: {file_name}")
    #     # except TimeoutException:
    #     #     print(f"Элемент {locator} не найден для создания скриншота.")
    #     except Exception as e:
    #         print(f"Ошибка при создании скриншота элемента: {e}")
    #
    # def check_element_is_visible(self, locator):
    #     try:
    #         element = self.element_is_visible(locator)
    #         # Проверка видимости элемента
    #         if element.is_displayed():
    #             print("Элемент видим на экране")
    #         # Проверка активности элемента
    #         if element.is_enabled():
    #             print("Элемент активен")
    #         return True
    #     except(Exception):
    #         print('Элемент не найден')
    #         return False
