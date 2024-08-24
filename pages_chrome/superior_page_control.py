
from pages_chrome import PageChrome
from .config import LinksControl


class SuperiorPageControl(PageChrome):
    PAGE_URL = LinksControl.SUPERIOR_COMPANY_PAGE

    BUTTON_DEVICE_MANAGER = ("xpath", '//div[text()="Manage Devices"]')
    BOX_COMPANY_DEVICES = ("xpath", '//div[@class="box company_devices"]')

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _get_device_id(devise_id: str) -> tuple[str, str]:
        return "xpath", f'//*[text()="{devise_id}"]'

    def click_button_device_manager(self):
        self.check_box_company_devices()
        self.element_to_be_clickable(self.BUTTON_DEVICE_MANAGER).click()

    def check_box_company_devices(self):
        self.visibility_of(self.visibility_of_element_located(self.BOX_COMPANY_DEVICES))

    def click_device_id_in_box(self, devise_id):
        self.element_to_be_clickable(self._get_device_id(devise_id)).click()




