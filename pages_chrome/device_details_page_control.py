
from pages_chrome import PageChrome


class DeviceDetailsPageControl(PageChrome):
    BUTTON_EDIT_OTA_VERSION = ("xpath", "(//div[@class='bt edit'])[1]")
    BUTTON_SAVE_OTA_VERSION = ("xpath", '(//div[text()="Save"])[2]')

    def __init__(self) -> None:
        super().__init__()

    def click_button_version_ota(self):
        self.element_to_be_clickable(self.BUTTON_EDIT_OTA_VERSION).click()

    def click_button_save_version_ota(self):
        self.element_to_be_clickable(self.BUTTON_SAVE_OTA_VERSION).click()
