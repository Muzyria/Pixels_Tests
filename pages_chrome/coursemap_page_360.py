from pages_chrome import PageChrome


class CourseMapSyncWise360(PageChrome):

    SETTINGS_ICON = ("xpath", '//button[@aria-label="settings-icon"]')
    # ------------------------------------------------------------------------------------------------------------------
    BUTTON_MENU_ICON = ("xpath", '//button[@aria-label="menu-icon"]')
    BUTTON_MENU_ICON_DEVICE_SETUP = ("xpath", '//div[@class="gridMenuDrop active"]//div[@routerlink="/device-setup"]')

    # ------------------------------------------------------------------------------------------------------------------
    BUTTON_ASSETS = ("xpath", '//button[@aria-label="assets"]')
    SPINNER = ("xpath", "//div[@class='loader']")
    # app_asset_details_____________________________________________________________________
    TAB_ASSET_DETAILS = ("xpath", '//li[@mattooltip="Asset Details"]')
    DEVICE_INFO_OS_VERSION = ("xpath", '//div[text()=" Os version "]/strong')
    DEVICE_INFO_APK_VERSION = ("xpath", '//div[text()=" Apk version "]/strong')
    DEVICE_INFO_GPS_VERSION = ("xpath", '//div[text()=" Gps Firmware Version "]/strong')
    DEVICE_INFO_CABLE_VERSION = ("xpath", '//div[text()=" Cable Firmware Version "]/strong')

    def __init__(self) -> None:
        super().__init__()

    def click_settings_icon(self) -> None:
        self.presence_of_element_located(self.SETTINGS_ICON).click()
        self.check_spinner_is_invisible()

    def click_button_menu_icon(self):
        self.presence_of_element_located(self.BUTTON_MENU_ICON).click()
        return self

    def click_button_menu_icon_device_setup(self) -> None:
        self.presence_of_element_located(self.BUTTON_MENU_ICON_DEVICE_SETUP).click()
        self.check_spinner_is_invisible()


    def click_assets_button(self) -> None:
        self.presence_of_element_located(self.BUTTON_ASSETS).click()
        self.check_spinner_is_invisible()

    def check_spinner_is_invisible(self):
        self.invisibility_of_element_located(self.SPINNER)
        print("spinner is invisible 360")

    # app_asset_details_______________________________________________________________________
    def click_tab_asset_details(self) -> None:
        self.visibility_of_element_located(self.TAB_ASSET_DETAILS).click()

    def get_device_info_os_version(self) -> str:
        return self.visibility_of_element_located(self.DEVICE_INFO_OS_VERSION).text

    def get_device_info_apk_version(self) -> str:
        return self.visibility_of_element_located(self.DEVICE_INFO_APK_VERSION).text

    def get_device_info_gps_version(self) -> str:
        return self.visibility_of_element_located(self.DEVICE_INFO_GPS_VERSION).text

    def get_device_info_cable_version(self) -> str:
        return self.visibility_of_element_located(self.DEVICE_INFO_CABLE_VERSION).text
