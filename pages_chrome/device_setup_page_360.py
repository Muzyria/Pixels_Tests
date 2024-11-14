from pages_chrome import PageChrome


class DeviceSetupSyncWise360(PageChrome):

    SPINNER = ("xpath", "//div[@class='loader']")

    # SAVE_BUTTON = ("xpath", '//div[@class="savebtn ng-star-inserted"]')
    SAVE_BUTTON = ("xpath", '//button[text()="Save"]')

    SELECT_BEEPING_LEVEL = ("xpath", '(//select[@class="ng-untouched ng-pristine ng-valid"])[2]')

    def __init__(self) -> None:
        super().__init__()

    def click_save_button(self):
        self.visibility_of_element_located(self.SAVE_BUTTON).click()
        print("CLICK SAVE BUTTON ____________________")
        self.check_spinner_is_invisible()

    def select_beeping_level(self, beeping_level):
        DeviceSetupSyncWise360.select_option_by_text(self.SELECT_BEEPING_LEVEL, beeping_level)

    def check_spinner_is_invisible(self):
        self.invisibility_of_element_located(self.SPINNER)
        print("spinner is invisible on device setup page")
