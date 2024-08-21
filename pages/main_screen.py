from pages import Page


class MainPage(Page):
    def __init__(self):
        super().__init__()

        self.menu_button_id = "menuDrawer"
        self.arm_button_id = "armButton"
        self.disarm_button_id = "disarmButton"
        self.night_mode_button_id = "nightModeButton"
        self.panic_button_id = "panicButton"

        self.devices_button_id = "devices"
        self.rooms_button_id = "rooms"
        self.notifications_button_id = "notifications"
        self.control_button_id = "control"

        self.settings_button_id = "buttonSettings"

        """slide bar menu"""
        self.settings_slide_bar_button_id = "settings"

    def press_button(self, id_button) -> None:
        self.find_element_by_id(id_button).click()

    def press_menu_button(self) -> "MainPage":
        self.press_button(self.menu_button_id)
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



