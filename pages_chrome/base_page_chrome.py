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
    def find_elements(cls, locator):
        return DriverChrome.chrome_instance.find_elements(*locator)

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

    def invisibility_of_element(self, locator: tuple[str, str]) -> WebElement:
        return self._get_wait().until(EC.invisibility_of_element(locator))

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

    # ------------------------------------------------------------------------------------------------------------------
    #
    # def open(self):
    #     self.driver.get(self.url)
    #     # self.driver.maximize_window()
    #
    # def open_new_url(self, url):
    #     self.driver.get(url)
    #
    # def refresh_tab(self):
    #     self.driver.refresh()
    #
    # def visibility_of_element_located(self, locator, timeout=30):
    #     return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    #
    # def visibility_of_all_elements_located(self, locator, timeout=30):
    #     return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    #
    # def presence_of_element_located(self, locator, timeout=30):
    #     return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    #
    # def presence_of_all_elements_located(self, locator, timeout=30):
    #     return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    #
    # def invisibility_of_element_located(self, locator, timeout=30):
    #     return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    #
    # def element_to_be_clickable(self, locator, timeout=30):
    #     return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #
    # def go_to_element(self, element):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #
    # def switch_to_new_tab(self):
    #     """Opens a new tab and switches to new tab"""
    #     self.driver.switch_to.new_window('tab')
    #
    # def get_window_handle(self):
    #     """Get window handle"""
    #     return self.driver.current_window_handle
    #
    # def switching_tab(self, handle):
    #     """Switching tabs"""
    #     self.driver.switch_to.window(handle)
    #
    # def move_coursor_to_elrment(self, element):
    #     div_rect = element.rect
    #     # Получаем координаты центра элемента
    #     center_x = div_rect['x'] + div_rect['width'] // 2
    #     center_y = div_rect['y'] + div_rect['height'] // 2
    #     # Перемещаем курсор в центр элемента
    #     pyautogui.moveTo(center_x, center_y, duration=0.5)
    #
    # def scroll_element_by_mouse(self, element):
    #     div_rect = element.rect
    #     # Получаем координаты центра элемента
    #     center_x = div_rect['x'] + div_rect['width'] // 2
    #     center_y = div_rect['y'] + div_rect['height'] // 2
    #     # Перемещаем курсор в центр элемента
    #     pyautogui.moveTo(center_x, center_y, duration=0.5)
    #     # Выполняем прокрутку колесика мыши
    #     pyautogui.scroll(-500)
    #     time.sleep(1)
    #
    # def action_double_click(self, element):
    #     action = ActionChains(self.driver)
    #     action.double_click(element)
    #     action.perform()
    #
    # def action_right_click(self, element):
    #     action = ActionChains(self.driver)
    #     action.context_click(element)
    #     action.perform()
    #
    # def take_page_screenshot(self, file_name):
    #     self.driver.save_screenshot(file_name)
    #     print(f"Скриншот сохранен: {file_name}")
    #
    #
    # def take_element_screenshot(self, locator, file_name):
    #     try:
    #         element = self.visibility_of_element_located(locator)
    #         element.screenshot(file_name)
    #         print(f"Скриншот элемента сохранен: {file_name}")
    #     except Exception as e:
    #         print(f"Ошибка при создании скриншота элемента: {e}")