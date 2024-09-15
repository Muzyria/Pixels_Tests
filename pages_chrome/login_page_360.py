import time

from pages_chrome import PageChrome
from credentials import LOGIN_360, PASSWORD_360
from .config import LinksBetaSyncWise360



class LoginPageSyncWise360(PageChrome):
    PAGE_URL = LinksBetaSyncWise360.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@aria-label='submit']")

    PROFILE_ICON = ("xpath", '//button[@aria-label="profile-icon"]')
    LOGOUT_BUTTON = ("xpath", '//li[text()=" Log out "]')

    LOGIN_SUCCESSFUL = ("xpath", '//h2[text()="Login Successful"]')

    SPINNER = ("xpath", "//div[@class='loader']")

    def __init__(self) -> None:
        super().__init__()

    def enter_login(self, login: str = LOGIN_360) -> 'LoginPageSyncWise360':
        self.element_to_be_clickable(self.USERNAME_FIELD).send_keys(login)
        return self

    def enter_password(self, password: str = PASSWORD_360) -> 'LoginPageSyncWise360':
        self.element_to_be_clickable(self.PASSWORD_FIELD).send_keys(password)
        return self

    def click_login_button(self) -> None:
        self.element_to_be_clickable(self.BUTTON_LOGIN).click()
        self.check_spinner_is_invisible()

    def check_spinner_is_invisible(self):
        self.invisibility_of_element_located(self.LOGIN_SUCCESSFUL)
        self.invisibility_of_element_located(self.SPINNER)
        print("successful is invisible and spinner is invisible 360")

    def click_logout_button(self):
        self.visibility_of_element_located(self.PROFILE_ICON).click()
        time.sleep(1)
        self.visibility_of_element_located(self.LOGOUT_BUTTON).click()

