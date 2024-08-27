from pages_android import Page
from android_utils import touch_screen_by_coordinate


class MenuPage(Page):
    def __init__(self):
        super().__init__()

    PLAY_GOLF_BUTTON_ID = ("id", "com.l1inc.yamatrack3d:id/linearLayoutPlayGolf")
    SETTINGS_BUTTON_ID = ("id", "com.l1inc.yamatrack3d:id/linearLayoutSettings")

    def press_play_golf_button(self) -> None:
        self.presence_of_element_located(self.PLAY_GOLF_BUTTON_ID).click()

    def press_settings_button(self) -> None:
        self.presence_of_element_located(self.SETTINGS_BUTTON_ID).click()









