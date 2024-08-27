from pages_android import Page
from android_utils import touch_screen_by_coordinate


class MainPage(Page):
    def __init__(self):
        super().__init__()

    MENU_BUTTON_ID = ("id","com.l1inc.yamatrack3d:id/buttonMenu")
    FLAG_BUTTON_COORDINATE = ('1000', '100')

    TEXT_NO_ACTIVE_DOWNLOADS = ("id", "com.l1inc.yamatrack3d:id/textViewNoActiveDownloads")

        # com.l1inc.yamatrack3d:id/autoUpdateCellOs
        # com.l1inc.yamatrack3d:id/imageButtonComplete
        # (//android.widget.ImageButton[@resource-id="com.l1inc.yamatrack3d:id/imageButtonComplete"])[2]

        # com.l1inc.yamatrack3d:id/autoUpdateCellApk
        # (//android.widget.ImageButton[@resource-id="com.l1inc.yamatrack3d:id/imageButtonComplete"])[1]
        # //android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewPercentage"]

        # spinner com.l1inc.yamatrack3d:id/imageViewLoading

    def press_menu_button(self) -> "MainPage":
        self.presence_of_element_located(self.MENU_BUTTON_ID).click()
        return self

    def press_flag_button(self) -> None:
        touch_screen_by_coordinate(*self.FLAG_BUTTON_COORDINATE)

    def get_text_no_active_downloads(self):
        return self.presence_of_element_located(self.TEXT_NO_ACTIVE_DOWNLOADS).text






