
from pages_chrome import PageChrome


class DeviceDetailsPageControl(PageChrome):
    BUTTON_EDIT_OTA_VERSION = ("xpath", "(//div[@class='bt edit'])[1]")
    BUTTON_SAVE_OTA_VERSION = ("xpath", '(//div[text()="Save"])[2]')
    LIST_OS_VERSION = ("xpath", '//select[@name="osVersion"]')
    LIST_APP_VERSION = ("xpath", '//select[@name="appVersion"]')
    BUTTON_REMOVE_APP_UPDATE = ("xpath", '//div[@class="bt delete-app-update"]')
    BUTTON_REMOVE_OS_UPDATE = ("xpath", '//div[@class="bt delete-os-update"]')

    # device log
    LIST_DEVICE_LOGS = ("xpath", '//table[@class="style4 center device-logs-tbl"]//tbody')

    # info
    BUTTON_INFO = ("xpath", '//div[text()="Info"]')
    TEXT_FW_VERSION = ("xpath", "//div[text()='FW Version']/following-sibling::div[@class='desc']")
    TEXT_APP_VERSION = ("xpath", "(//div[text()='App Version']/following-sibling::div[@class='desc'])[2]")

    @staticmethod
    def get_app_version_in_list(app_version: str) -> tuple[str, str]:
        return "xpath", f'//select[@name="appVersion"]/option[@value="{app_version}"]'

    @staticmethod
    def get_os_version_in_list(app_version: str) -> tuple[str, str]:
        return "xpath", f'//select[@name="osVersion"]/option[@value="{app_version}"]'

    def __init__(self) -> None:
        super().__init__()

    def click_button_edit_version_ota(self):
        self.element_to_be_clickable(self.BUTTON_EDIT_OTA_VERSION).click()
        return self

    def click_button_save_version_ota(self):
        self.element_to_be_clickable(self.BUTTON_SAVE_OTA_VERSION).click()

    def click_list_os_version(self):
        self.element_to_be_clickable(self.LIST_OS_VERSION).click()
        return self

    def select_os_version(self, os_version: str):
        self.click_list_os_version()
        self.element_to_be_clickable(self.get_os_version_in_list(os_version)).click()

    def click_list_app_version(self):
        self.element_to_be_clickable(self.LIST_APP_VERSION).click()
        return self

    def select_app_version(self, app_version: str):
        self.click_list_app_version()
        self.element_to_be_clickable(self.get_app_version_in_list(app_version)).click()

    #  remove ota ---------------------------------------------------------------------
    def check_button_remove_os_is_displayed(self):
        return True if self.find_elements(self.BUTTON_REMOVE_OS_UPDATE) else False

    def check_button_remove_app_is_displayed(self):
        return True if self.find_elements(self.BUTTON_REMOVE_APP_UPDATE) else False

    def click_button_remove_os_update(self):
        self.visibility_of_element_located(self.BUTTON_REMOVE_OS_UPDATE).click()

    def click_button_remove_app_update(self):
        self.visibility_of_element_located(self.BUTTON_REMOVE_APP_UPDATE).click()

    #  check device info -------------------------------------------------------------
    def click_button_info(self):
        self.element_to_be_clickable(self.BUTTON_INFO).click()

    def get_info_fw_version(self):
        return self.visibility_of_element_located(self.TEXT_FW_VERSION).text

    def get_info_app_version(self):
        return self.visibility_of_element_located(self.TEXT_APP_VERSION).text


