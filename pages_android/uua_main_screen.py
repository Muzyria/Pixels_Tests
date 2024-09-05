from pages_android import Page


class UUAMainPage(Page):
    def __init__(self):
        super().__init__()

    NAME_ACTIVITY = ".activities.SettingsUpdatesListActivity_"
    NAME_INSTALL_ACTIVITY = ".PackageInstallerActivity"

    BUTTON_CANCEL = ("id", "com.android.packageinstaller:id/cancel_button")

    BUTTON_UPDATE_FIRMWARE = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack_util_2:id/textViewName" and @text="UPDATE FIRMWARE"]')
    BUTTON_UPDATE_CABLE = ("xpath", '//android.widget.TextView[@resource-id="com.l1inc.yamatrack_util_2:id/textViewName" and @text="UPDATE CABLE"]')

    def wait_install_activity(self):
        assert self.wait_activity(self.NAME_INSTALL_ACTIVITY, 120), "INSTALL_ACTIVITY_IS_NOT_LOADED"
        print("__INSTALL_ACTIVITY_IS_LOADED__")

    def wait_update_list_activity(self):
        assert self.wait_activity(self.NAME_ACTIVITY, 120), "UPDATE_LIST_ACTIVITY_IS_NOT_LOADED"
        print("__UPDATE_LIST_ACTIVITY_IS_LOADED__")

    def press_button_cancel(self) -> "UUAMainPage":
        self.element_to_be_clickable(self.BUTTON_CANCEL).click()
        return self

    def press_button_update_firmware(self) -> "UUAMainPage":
        self.element_to_be_clickable(self.BUTTON_UPDATE_FIRMWARE).click()
        return self
