from pages_android import Page


class UUUpdateFirmwarePage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ".activities.SettingsUpdatesActivity_"

    BUTTON_UPDATE_NOW = ("id", "com.l1inc.yamatrack_util_2:id/buttonUpdateNow")

    UPDATE_MESSAGE_TEXT = ("id", "com.l1inc.yamatrack_util_2:id/textViewUpdatedMessage")
    UPDATE_STATUS_TEXT = ("id", "com.l1inc.yamatrack_util_2:id/textViewStatusText")

    UPDATE_DETAILED_MESSAGE_TEXT = ("id", "com.l1inc.yamatrack_util_2:id/textViewUpdateDetailedMessage")

    def press_button_update_now(self) -> "UUUpdateFirmwarePage":
        self.element_to_be_clickable(self.BUTTON_UPDATE_NOW).click()
        return self

    def get_text_update_message(self) -> str:
        """
        YOUR DEVICE IS UPDATED
        """
        return self.visibility_of_element_located(self.UPDATE_MESSAGE_TEXT).text

    def get_text_update_detailed_message(self) -> str:
        """
        SELECT UPDATE NOW
        """
        return self.visibility_of_element_located(self.UPDATE_MESSAGE_TEXT).text

    def get_text_update_status(self) -> str:
        """
        1: NO UPDATES AVAILABLE
        2: UPDATE AVAILABLE
        """
        return self.visibility_of_element_located(self.UPDATE_STATUS_TEXT).text

