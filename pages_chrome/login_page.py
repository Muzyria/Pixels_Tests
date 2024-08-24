from pages_chrome import PageChrome
from credentials import LOGIN_360, PASSWORD_360
from .config import LinksBetaSyncWise360


class LoginPageSyncWise360(PageChrome):
    PAGE_URL = LinksBetaSyncWise360.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@aria-label='submit']")

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
