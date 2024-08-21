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
        print(f"{udid=}")


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


def get_wakefulness_status() -> str:
    # Выполнение команды adb и получение вывода
    adb_command = ['adb', '-s', udid, 'shell', 'dumpsys', 'power']
    result = subprocess.run(adb_command, stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if "mWakefulness=" in line:
            return line.split('=')[1].strip()
    return "Status not found"


def wake_up_device() -> None:
    if get_wakefulness_status() == "Dozing":
        subprocess.run(
            ['adb', '-s', udid, 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    else:
        print("Devise is Active")


if __name__ == '__main__':
    get_udid()
    wake_up_device()
