from pages_android import Page
from android_utils import touch_screen_by_coordinate


class SettingsPage(Page):
    def __init__(self):
        super().__init__()

    SUBMIT_PASSWORD_BUTTON = ("id", "com.l1inc.yamatrack3d:id/buttonSubmit")

    ASSETS_DETAILS_BUTTON = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewName" and @text="ASSET DETAILS"]')
    UPDATES_BUTTON = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewName" and @text="UPDATES"]')
    FULL_APP_RESET_BUTTON = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewName" and @text="FULL APP RESET"]')

    YES_BUTTON = ("id", "com.l1inc.yamatrack3d:id/buttonYes")
    CANCEL_BUTTON = ('id', 'com.l1inc.yamatrack3d:id/imageButtonCancel')

    @staticmethod
    def _get_number_button_id(number: str) -> tuple[str, str]:
        return "id", f"com.l1inc.yamatrack3d:id/button{number}"

    def enter_settings_password(self) -> None:
        for number in "123999":
            self.presence_of_element_located(self._get_number_button_id(number)).click()
        self.press_submit_password_button()

    def press_submit_password_button(self) -> None:
        self.presence_of_element_located(self.SUBMIT_PASSWORD_BUTTON).click()

    def press_assets_details_button(self):
        self.visibility_of_element_located(self.ASSETS_DETAILS_BUTTON).click()

    def press_full_app_reset_button(self):
        self.visibility_of_element_located(self.FULL_APP_RESET_BUTTON).click()

    def press_button_yes(self):
        self.visibility_of_element_located(self.YES_BUTTON).click()

    def press_button_cancel(self):
        self.visibility_of_element_located(self.CANCEL_BUTTON).click()
