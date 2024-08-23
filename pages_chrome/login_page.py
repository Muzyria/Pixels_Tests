from pages_chrome import PageChrome
from .config.links import Links_syncwise360
from credentials import LOGIN, PASSWORD


class LoginPageSyncwise360(PageChrome):
    PAGE_URL = Links_syncwise360.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@aria-label='submit']")

    SPINNER = ("xpath", "//div[@class='loader']")

    def __init__(self) -> None:
        super().__init__()

    def enter_login(self, login: str = LOGIN) -> "LoginPageSyncwise360":
        self.element_to_be_clickable(self.USERNAME_FIELD).send_keys(login)
        return self

    def enter_password(self, password: str = PASSWORD) -> "LoginPageSyncwise360":
        self.element_to_be_clickable(self.PASSWORD_FIELD).send_keys(password)
        return self

    def click_login_button(self):
        self.element_to_be_clickable(self.BUTTON_LOGIN).click()
