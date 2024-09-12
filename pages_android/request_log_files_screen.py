import time

from pages_android import Page
import android_utils


class RequestLogFilesPage(Page):
    def __init__(self):
        super().__init__()

    REQUEST_LOGS_BUTTON = ("id", "com.l1inc.yamatrack3d:id/buttonRequestLogs")
    TEXT_VIEW_STATUS = ("id", "com.l1inc.yamatrack3d:id/textViewStatusText")

    LAYOUT_PROGRESSING_TEXT = ("xpath", '//android.widget.RelativeLayout[@resource-id="com.l1inc.yamatrack3d:id/relativeLayoutLogsProcessing"]//android.widget.TextView')
    TEXT_PROCESS_PERCENTAGE = ("id", "com.l1inc.yamatrack3d:id/textViewProcessPercentage")

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

    def get_text_layout_progressing(self) -> str:
        return self.visibility_of_element_located(self.LAYOUT_PROGRESSING_TEXT).text

    def get_text_process_percentage(self) -> str:
        return self.visibility_of_element_located(self.TEXT_PROCESS_PERCENTAGE).text

    def get_text_view_updated_message(self) -> str:
        return self.visibility_of_element_located(self.TEXT_VIEW_UPDATED_MESSAGE).text

    def wait_zipping_files(self):
        while self.get_text_view_status() == "ZIPPING FILES IN PROGRESS":
            android_utils.touch_screen_by_coordinate(200, 200)
            time.sleep(3)
            print(f"ZIPPING FILES IN PROGRESS")
        print("ZIPPING FILES IS COMPLETE")
        return True

    def wait_downloading_files(self):
        while self.get_text_view_status() == "DOWNLOADING FILES IN PROGRESS":
            android_utils.touch_screen_by_coordinate(200, 200)
            time.sleep(3)
            print(f"DOWNLOADING FILES IN PROGRESS")
        print("DOWNLOADING FILES IS COMPLETE")
        return True

    def press_button_cancel(self):
        self.visibility_of_element_located(self.CANCEL_BUTTON).click()
