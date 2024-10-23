from pages_chrome import PageChrome


class GeneralSettingSyncWise360(PageChrome):

    SPINNER = ("xpath", "//div[@class='loader']")

    ASSET_TRACKER_BUTTON = ("xpath", '//button[@aria-label="asset-tracker"]')

    def __init__(self) -> None:
        super().__init__()

    def click_asset_tracker_button(self):
        self.visibility_of_element_located(self.ASSET_TRACKER_BUTTON).click()
        self.check_spinner_is_invisible()

    def check_spinner_is_invisible(self):
        self.invisibility_of_element_located(self.SPINNER)
        print("spinner is invisible on general setting page")
