from pages_chrome import PageChrome
from selenium.webdriver.support.select import Select

class AssetTrackerSyncWise360(PageChrome):

    SPINNER = ("xpath", "//div[@class='loader']")

    SPEED_AND_BRAKING_MODE_BUTTON = ("xpath", "//p[text()='Speed And Braking Mode']")
    CLOSE_MODAL_BUTTON = ("xpath", '//button[@class="closeModal"]')
    SAVE_MODAL_BUTTON = ("xpath", '//button[@class="btn"]')

    SELECT_SPEED = ("xpath", '//div[@class="form-group"][1]/mat-select')
    SELECT_BRAKE = ("xpath", '//div[@class="form-group"][2]/mat-select')


    def __init__(self) -> None:
        super().__init__()

    def click_speed_and_braking_mode_button(self):
        self.visibility_of_element_located(self.SPEED_AND_BRAKING_MODE_BUTTON).click()

    def click_close_modal_button(self):
        self.visibility_of_element_located(self.CLOSE_MODAL_BUTTON).click()

    def click_save_modal_button(self):
        self.visibility_of_element_located(self.SAVE_MODAL_BUTTON).click()
        self.check_spinner_is_invisible()

    def select_dropdown_speed(self, value: str):
        self.visibility_of_element_located(self.SELECT_SPEED).click()
        self.visibility_of_element_located(("xpath", f'//span[text()=" {value}mph "]')).click()

    def select_dropdown_brake(self, value: str):
        self.visibility_of_element_located(self.SELECT_BRAKE).click()
        self.visibility_of_element_located(("xpath", f'//span[text()=" {value} "]')).click()



    def check_spinner_is_invisible(self):
        self.visibility_of_element_located(self.SPINNER)
        self.invisibility_of_element_located(self.SPINNER)
        print("spinner is invisible on asset tracker page")
