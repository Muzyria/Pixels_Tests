import subprocess
import time

from appium.options.android import UiAutomator2Options


adb_output = subprocess.getoutput('adb devices')
udid = ""


# def get_udid() -> None:
#     """Get UDID"""
#     if not adb_output or len(adb_output.splitlines()) == 1:
#         raise EnvironmentError('No Android device found')
#     else:
#         global udid
#         udid = adb_output.splitlines()[1].split()[0]
#         print(f"{udid=}")
def get_udid(device_ip: str = None) -> None:
    """Get UDID from usb or set IP address"""
    if not device_ip:
        if not adb_output or len(adb_output.splitlines()) == 1:
            raise EnvironmentError('No Android device found')
        else:
            global udid
            udid = adb_output.splitlines()[1].split()[0]
            print(f"{udid=}")
    else:
        udid = device_ip
        device_connect()


def device_connect() -> None:
    subprocess.run(['adb', 'connect', udid])


def get_driver_appium_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.no_reset = True
    options.udid = udid
    options.clear_device_logs_on_start = True
    options.auto_grant_permissions = True
    options.disable_window_animation = True
    return options


# def reset_app(package: str) -> None:
#     subprocess.run(
#         ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
#         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
#     )


def wait_for_the_device_to_boot():
    while True:
        result = subprocess.run(["adb", "-s", udid, "shell", "pidof", "com.l1inc.yamatrack3d"], capture_output=True, text=True)
        if result.stdout.strip():  # Если приложение запущено
            print(f"Приложение com.l1inc.yamatrack3d запущено.")
            time.sleep(30)
            return True
        print("Ожидание запуска приложения...")
        time.sleep(5)  # Проверяем каждые 5 секунд


def get_wakefulness_status() -> str:
    # Выполнение команды adb и получение вывода
    adb_command = ['adb', '-s', udid, 'shell', 'dumpsys', 'power']
    result = subprocess.run(adb_command, stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if "mWakefulness=" in line:
            result = line.split('=')[1].strip()
            print(result)
            return result
    return "Status not found"


def wake_up_device() -> None:
    if get_wakefulness_status() == "Dozing":
        subprocess.run(
            ['adb', '-s', udid, 'shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    else:
        print("Devise is Active")


# @_wait_for_the_device_to_boot
def cart_burn_sleep_mode() -> None:
    """Put device in cart bun sleep"""
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'am', 'broadcast', '-a', 'com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    # Ждем, пока устройство не заснет
    while not get_wakefulness_status() == "Dozing":
        print("Ожидание, пока устройство заснет...")
        time.sleep(5)  # Период ожидания перед следующей проверкой
    print("Device in Cart Burn Sleep Mode")


def cart_of_hole_sleep_mode() -> None:
    """Put device in off hole sleep"""
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'am', 'broadcast', '-a', 'com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    time.sleep(20)  # Период ожидания
    print("Device in Off Hole Sleep Mode")

def device_reboot() -> None:
    """Reboot device"""
    subprocess.run(['adb', '-s', udid, 'reboot'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def touch_screen_by_coordinate(x: str|int , y: str|int) -> None:
    subprocess.run(['adb', '-s', udid, 'shell', 'input', 'tap', f"{x} {y}"])


def swipe_screen_down_to_up(x1=500, y1=700, x2=500, y2=100, speed=250) -> None:
    """exemple x1=100, y1=500, x2=200, y2=500, speed=250"""
    subprocess.run(['adb', '-s', udid, 'shell', 'input', 'swipe', f"{x1} {y1} {x2} {y2} {speed}"])


def swipe_screen_up_to_down(x1=500, y1=100, x2=500, y2=700, speed=250) -> None:
    """exemple x1=100, y1=500, x2=200, y2=500, speed=250"""
    subprocess.run(['adb', '-s', udid, 'shell', 'input', 'swipe', f"{x1} {y1} {x2} {y2} {speed}"])


if __name__ == '__main__':
    get_udid()
    device_reboot()
