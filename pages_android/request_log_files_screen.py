from pages_android import Page


class RequestLofFilesPage(Page):
    def __init__(self):
        super().__init__()

    REQUEST_LOGS_BUTTON = ("id", "com.l1inc.yamatrack3d:id/buttonRequestLogs")
    TEXT_VIEW_STATUS = ("id", "com.l1inc.yamatrack3d:id/textViewStatusText")

    TEXT_VIEW_UPDATED_MESSAGE = ("id", "com.l1inc.yamatrack3d:id/textViewUpdatedMessage")

    CANCEL_BUTTON = ('id', 'com.l1inc.yamatrack3d:id/imageButtonCancel')

    def press_request_logs_button(self) -> None:
        self.presence_of_element_located(self.REQUEST_LOGS_BUTTON).click()

    def get_text_view_status(self) -> str:
        """
        1 NO DATA
        2 ZIPPING FILES IN PROGRESS
        3 DOWNLOADING FILES IN PROGRESS
        """
        return self.visibility_of_element_located(self.TEXT_VIEW_STATUS).text

    def get_text_view_updated_message(self) -> str:
        return self.visibility_of_element_located(self.TEXT_VIEW_UPDATED_MESSAGE).text

    def press_button_cancel(self):
        self.visibility_of_element_located(self.CANCEL_BUTTON).click()
