from pages_android import Page


class IntroPage(Page):

    def __init__(self) -> None:
        super().__init__()

        self.login_button_id = 'authHelloLogin'

    def click_login_button(self) -> None:
        login_button = self.find_element_by_id(self.login_button_id)
        login_button.click()
