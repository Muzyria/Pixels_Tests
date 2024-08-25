from pages_chrome import PageChrome
from credentials import LOGIN_CONTROL, PASSWORD_CONTROL
from .config import LinksControl


class LoginPageControl(PageChrome):
    PAGE_URL = LinksControl.LOGIN_PAGE
    MAIN_PAGE = LinksControl.MAIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@id='btn-submit']")
    BUTTON_LOGOUT = ("xpath", '//div[@id="logout"]')

    def __init__(self) -> None:
        super().__init__()

    def enter_login(self, login: str = LOGIN_CONTROL) -> 'LoginPageControl':
        self.element_to_be_clickable(self.USERNAME_FIELD).send_keys(login)
        return self

    def enter_password(self, password: str = PASSWORD_CONTROL) -> 'LoginPageControl':
        self.element_to_be_clickable(self.PASSWORD_FIELD).send_keys(password)
        return self

    def click_login_button(self) -> None:
        self.element_to_be_clickable(self.BUTTON_LOGIN).click()

    def click_logout_button(self) -> None:
        self.element_to_be_clickable(self.BUTTON_LOGOUT).click()
