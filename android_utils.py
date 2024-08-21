import subprocess
from appium.options.android import UiAutomator2Options


adb_output = subprocess.getoutput('adb devices')
udid = ""


def get_udid() -> None:
    """Get UDID"""
    if not adb_output or len(adb_output.splitlines()) == 1:
        raise EnvironmentError('No Android device found')
    else:
        global udid
        udid = adb_output.splitlines()[1].split()[0]


def get_driver_appium_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.no_reset = True
    options.udid = udid
    options.clear_device_logs_on_start = True
    options.auto_grant_permissions = True
    options.disable_window_animation = True
    return options


def reset_app(package: str) -> None:
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
