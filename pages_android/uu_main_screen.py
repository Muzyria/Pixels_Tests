from pages_android import Page


class UUMainPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ".activities.SettingsUpdatesListActivity_"

    BUTTON_CANCEL = ("id", "com.android.packageinstaller:id/cancel_button")

    BUTTON_UPDATE_FIRMWARE = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack_util_2:id/textViewName" and @text="UPDATE FIRMWARE"]')
    BUTTON_UPDATE_CABLE = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack_util_2:id/textViewName" and @text="UPDATE CABLE"]')

    def press_button_cancel(self) -> "UUMainPage":
        self.element_to_be_clickable(self.BUTTON_CANCEL).click()
        return self

    def press_button_update_firmware(self) -> "UUMainPage":
        self.element_to_be_clickable(self.BUTTON_UPDATE_FIRMWARE).click()
        return self
