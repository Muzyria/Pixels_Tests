from pages_android import Page
from android_utils import touch_screen_by_coordinate


class MainPage(Page):
    def __init__(self):
        super().__init__()

    MENU_BUTTON_ID = ("id","com.l1inc.yamatrack3d:id/buttonMenu")
    FLAG_BUTTON_COORDINATE = ('1000', '100')

    TEXT_NO_ACTIVE_DOWNLOADS = ("id", "com.l1inc.yamatrack3d:id/textViewNoActiveDownloads")

    SPINNER = ("id", 'com.l1inc.yamatrack3d:id/imageViewLoading')

    VIEW_PERCENTAGE_LIST = ("id", "com.l1inc.yamatrack3d:id/textViewPercentage")
    VIEW_PROGRESS_LIST = ("id", "com.l1inc.yamatrack3d:id/progressView")
    VIEW_BUTTON_COMPLETE = ("id", "com.l1inc.yamatrack3d:id/imageButtonComplete")

        # com.l1inc.yamatrack3d:id/autoUpdateCellOs
        # com.l1inc.yamatrack3d:id/imageButtonComplete
        # (//android.widget.ImageButton[@resource-id="com.l1inc.yamatrack3d:id/imageButtonComplete"])[2]

        # com.l1inc.yamatrack3d:id/autoUpdateCellApk

    def check_menu_button_is_visible(self) -> bool:
        self.visibility_of_element_located(self.MENU_BUTTON_ID)
        return True

    def press_menu_button(self) -> "MainPage":
        self.presence_of_element_located(self.MENU_BUTTON_ID).click()
        return self

    def press_flag_button(self) -> None:
        touch_screen_by_coordinate(*self.FLAG_BUTTON_COORDINATE)

    def get_text_no_active_downloads(self):
        return self.presence_of_element_located(self.TEXT_NO_ACTIVE_DOWNLOADS).text

    def check_view_percentage_list(self):
        res = self.find_elements(self.VIEW_PERCENTAGE_LIST)
        print("view_percentage")
        print(res)

    def check_view_progress_list(self):
        res = self.find_elements(self.VIEW_PERCENTAGE_LIST)
        print("view_percentage")
        print(res)

    def check_view_button_complete_list(self):
        res = self.visibility_of_all_elements_located(self.VIEW_BUTTON_COMPLETE)
        print("button_complete")
        print(res)

    def wait_spinner_to_invisible(self):
        self.visibility_of_element_located(self.SPINNER)
        print("__spinner_is_visible__")
        self.invisibility_of_element_located(self.SPINNER)
        print("__spinner_is_invisible__")
