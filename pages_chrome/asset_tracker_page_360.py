from pages_chrome import PageChrome


class AssetTrackerSyncWise360(PageChrome):

    SPINNER = ("xpath", "//div[@class='loader']")

    SPEED_AND_BRAKING_MODE_BUTTON = ("xpath", "//p[text()='Speed And Braking Mode']")
    CLOSE_MODAL_BUTTON = ("xpath", '//button[@class="closeModal"]')
    SAVE_MODAL_BUTTON = ("xpath", '//button[@class="btn"]')


    def __init__(self) -> None:
        super().__init__()

    def click_speed_and_braking_mode_button(self):
        self.visibility_of_element_located(self.SPEED_AND_BRAKING_MODE_BUTTON).click()

    def click_close_modal_button(self):
        self.visibility_of_element_located(self.CLOSE_MODAL_BUTTON).click()

    def click_save_modal_button(self):
        self.visibility_of_element_located(self.SAVE_MODAL_BUTTON).click()



    def check_spinner_is_invisible(self):
        self.invisibility_of_element_located(self.SPINNER)
        print("spinner is invisible on general setting page")
