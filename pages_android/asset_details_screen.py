from pages_android import Page
from android_utils import touch_screen_by_coordinate, swipe_screen_down_to_up


class AssetDetailsPage(Page):
    def __init__(self):
        super().__init__()

    # ASSETS_APK_VERSION = ("xpath", '(//android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewValue"])[1]')
    # ASSETS_OS_VERSION = ("xpath", '(//android.widget.TextView[@resource-id="com.l1inc.yamatrack3d:id/textViewValue"])[2]')
    ASSETS_APK_VERSION = ("xpath", "//android.widget.TextView[@text='APPLICATION VERSION (APK)']/following-sibling::android.widget.TextView")
    ASSETS_OS_VERSION = ("xpath", "//android.widget.TextView[@text='OS VERSION']/following-sibling::android.widget.TextView")
    ASSETS_CABLE_VERSION = ("xpath", "//android.widget.TextView[@text='CABLE FIRMWARE']/following-sibling::android.widget.TextView")
    ASSETS_GPS_VERSION = ("xpath", "//android.widget.TextView[@text='GPS FIRMWARE']/following-sibling::android.widget.TextView")

    CANCEL_BUTTON = ('id', 'com.l1inc.yamatrack3d:id/imageButtonCancel')

    def get_apk_version(self):
        swipe_screen_down_to_up()
        apk_version = self.visibility_of_element_located(self.ASSETS_APK_VERSION).text
        print(f'{apk_version=}')
        return apk_version

    def get_os_version(self):
        swipe_screen_down_to_up()
        os_version = self.visibility_of_element_located(self.ASSETS_OS_VERSION).text
        print(f'{os_version=}')
        return os_version

    def get_cable_version(self):
        swipe_screen_down_to_up()
        cable_version = self.visibility_of_element_located(self.ASSETS_CABLE_VERSION).text
        print(f'{cable_version=}')
        return cable_version

    def get_gps_version(self):
        swipe_screen_down_to_up()
        gps_version = self.visibility_of_element_located(self.ASSETS_GPS_VERSION).text
        print(f'{gps_version=}')
        return gps_version

    def press_button_cancel(self):
        self.visibility_of_element_located(self.CANCEL_BUTTON).click()
