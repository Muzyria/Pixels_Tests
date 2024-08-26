from pages_android import Page
from android_utils import touch_screen_by_coordinate


class MainPage(Page):
    def __init__(self):
        super().__init__()

        self.menu_button_id = "buttonMenu"
        self.flag_button_coordinate = "1000 100"

        self.text_no_active_downloads_id = "textViewNoActiveDownloads"

        # com.l1inc.yamatrack3d:id/autoUpdateCellOs
        # com.l1inc.yamatrack3d:id/imageButtonComplete
        # (//android.widget.ImageButton[@resource-id="com.l1inc.yamatrack3d:id/imageButtonComplete"])[2]

        # com.l1inc.yamatrack3d:id/autoUpdateCellApk
        # (//android.widget.ImageButton[@resource-id="com.l1inc.yamatrack3d:id/imageButtonComplete"])[1]
        # //android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewPercentage"]


        # spinner com.l1inc.yamatrack3d:id/imageViewLoading


    def press_button(self, id_button) -> None:
        self.find_element_by_id(id_button).click()

    def press_menu_button(self) -> "MainPage":
        # self.press_button(self.menu_button_id)
        self.find_element_by_id(self.menu_button_id).click()
        return self

    def press_flag_button(self) -> None:
        touch_screen_by_coordinate(self.flag_button_coordinate)

    def get_text_no_active_downloads(self):
        return self.find_element_by_id(self.text_no_active_downloads_id).text






