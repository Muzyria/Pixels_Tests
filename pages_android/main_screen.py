from pages_android import Page


class MainPage(Page):
    def __init__(self):
        super().__init__()

        self.menu_button_id = "buttonMenu"


    def press_button(self, id_button) -> None:
        self.find_element_by_id(id_button).click()

    def press_menu_button(self) -> "MainPage":
        # self.press_button(self.menu_button_id)
        self.find_element_by_id(self.menu_button_id).click()
        return self

    def press_settings_slide_bar_button(self) -> None:
        self.press_button(self.settings_slide_bar_button_id)

    def get_info_button(self):
        my_dict = {}

        button = self.find_element_by_id(self.devices_button_id)
        button_text = button.get_attribute("text")
        bounds = button.get_attribute("bounds")
        print(button_text)
        print(bounds)



