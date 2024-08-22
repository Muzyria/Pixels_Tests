import subprocess
import time

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


# def reset_app(package: str) -> None:
#     subprocess.run(
#         ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
#         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
#     )


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


def cart_burn_sleep_mode() -> None:
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'am', 'broadcast', '-a', 'com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    # Ждем, пока устройство не заснет
    while not get_wakefulness_status() == "Dozing":
        print("Ожидание, пока устройство заснет...")
        time.sleep(2)  # Период ожидания перед следующей проверкой
    print("Device in Cart Burn Sleep Mode")


def device_reboot():
    subprocess.run(['adb', '-s', udid, 'reboot'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



if __name__ == '__main__':
    get_udid()
    device_reboot()


