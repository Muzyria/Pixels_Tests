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
    options.new_command_timeout = 300  # Время ожидания между командами в секундах
    return options


# def reset_app(package: str) -> None:
#     subprocess.run(
#         ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
#         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
#     )

def get_current_activity() -> str | None:
    """return name activity"""
    result = subprocess.run(["adb", "-s", udid, "shell", "dumpsys", "activity", "activities"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    # Поиск строки с информацией о текущей активности
    for line in result.stdout.splitlines():
        if "mResumedActivity" in line:
            # Извлечение полного имени активности
            activity_info = line.split()[-2]  # Предпоследний элемент строки
            # Преобразование активности в правильный формат
            activity_name = activity_info.replace('{', '').replace('}', '').split('/')[1]
            return activity_name
    return None  # Возвращает None, если активность не найдена


def wait_for_the_device_to_boot():
    """Wait for application will be booted"""
    while True:
        result = subprocess.run(["adb", "-s", udid, "shell", "pidof", "com.l1inc.yamatrack3d"], capture_output=True, text=True)
        if result.stdout.strip():  # Если приложение запущено
            print(f"Приложение com.l1inc.yamatrack3d запущено.")
            # time.sleep(5)
            return True
        print("Ожидание запуска приложения...")
        time.sleep(5)  # Проверяем каждые 5 секунд


def get_wakefulness_status() -> str:
    """Check status of sleep. return status from [Dozing, Awake, Asleep]"""
    adb_command = ['adb', '-s', udid, 'shell', 'dumpsys', 'power']
    result = subprocess.run(adb_command, stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if "mWakefulness=" in line:
            result = line.split('=')[1].strip()
            print(result)
            return result
    return "Status not found"


def wake_up_device() -> None:
    """Wake up Device from sleep"""
    if get_wakefulness_status() in ("Dozing", "Asleep"):
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
    while not get_wakefulness_status() in ("Dozing", "Asleep"):
        print("Ожидание, пока устройство заснет...")
        time.sleep(5)  # Период ожидания перед следующей проверкой
    print("Device in Cart Burn Sleep Mode")


def cart_of_hole_sleep_mode() -> None:
    """Put device in off hole sleep"""
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'am', 'broadcast', '-a', 'com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep'],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    # time.sleep(20)  # Период ожидания
    print("Device in Off Hole Sleep Mode")


def device_reboot() -> None:
    """Reboot device"""
    subprocess.run(['adb', '-s', udid, 'reboot'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def touch_screen_by_coordinate(x: str | int, y: str | int) -> None:
    subprocess.run(['adb', '-s', udid, 'shell', 'input', 'tap', f"{x} {y}"])


def swipe_screen_down_to_up(x1=500, y1=700, x2=500, y2=100, speed=250) -> None:
    """exemple x1=100, y1=500, x2=200, y2=500, speed=250"""
    subprocess.run(['adb', '-s', udid, 'shell', 'input', 'swipe', f"{x1} {y1} {x2} {y2} {speed}"])


def swipe_screen_up_to_down(x1=500, y1=100, x2=500, y2=700, speed=250) -> None:
    """exemple x1=100, y1=500, x2=200, y2=500, speed=250"""
    subprocess.run(['adb', '-s', udid, 'shell', 'input', 'swipe', f"{x1} {y1} {x2} {y2} {speed}"])

# connect --------------------------------------------------------------------------------------------------------------


def is_wifi_connected():
    # Выполнение команды adb shell ip addr show wlan0
    result = subprocess.run(["adb", '-s', udid, "shell", "ip", "addr", "show", "wlan0"], capture_output=True, text=True)
    # Проверка подключения Wi-Fi
    if "inet " in result.stdout:
        print("Устройство подключено к Wi-Fi")
        return True
    else:
        print("Устройство не подключено к Wi-Fi")
        return False


def is_cellular_connected():
    # Выполнение команды adb shell ip addr show rmnet_data0
    result = subprocess.run(["adb", '-s', udid, "shell", "ip", "addr", "show", "rmnet_data0"], capture_output=True,
                            text=True)
    if "inet " in result.stdout:
        print("Устройство подключено к сотовому интернету")
        return True
    else:
        print("Устройство не подключено к сотовому интернету")
        return False

# ----------------------------------------------------------------------------------------------------------------------

    # @staticmethod
    # def device_read_ip_address():
    #     """Получение IP адрес девайса при подключении по USB"""
    #     os.system(fr'adb shell ip addr show wlan0')  # читаем IP девайса
    #     result = subprocess.run(["adb", "shell", "ip", "addr", "show", "wlan0"], capture_output=True, text=True)
    #     output_lines = result.stdout.splitlines()
    #
    #     # Регулярное выражение для извлечения IP-адреса
    #     pattern = r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    #     ip_address = re.search(pattern, [item for item in output_lines if 'inet ' in item][0]).group(0).split()[1]
    #     print(ip_address)
    #     return ip_address
    #
    # def adb_get_state(self):
    #     output = os.system('adb get-state')
    #     # print(f'{output}')
    #     return output
    #
    # def device_disconnect(self):
    #     os.system(f'adb disconnect {self.ip_device}')
    #
    # def device_connect(self):
    #     os.system(f'adb connect {self.ip_device}')
    #
    # def device_reboot(self):
    #     os.system(f'adb -s {self.ip_device} reboot')
    #
    # def check_devices_active(self):
    #     """Проверяем, есть ли подключенные устройства в выводе в консоль"""
    #     output = subprocess.check_output(['adb', 'devices'])
    #     if self.ip_device in str(output) and "offline" not in str(output):
    #         print('Устройство Android подключено и активно.')
    #
    #     else:
    #         print(f'Устройство Android {self.ip_device} будет подключено By TCP/IP')
    #         self.device_disconnect()
    #         time.sleep(2)
    #         self.device_connect()
    #
    # def device_send_key(self, key=26):
    #     os.system(f'adb -s {self.ip_device} shell input keyevent {key}')
    #
    # def touch_screen(self, x=700, y=500):
    #     os.system(f'adb -s {self.ip_device} shell input tap {x} {y}')
    #
    # def device_send_coordinate(self, location):
    #     os.system(rf'adb -s {self.ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')  # "50.012356,36.243361"
    #
    # def device_in_cart_barn(self):
    #     os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep')
    #
    # def device_in_off_hole(self):
    #     os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep')
    #
    # def device_close_yamatack(self):
    #     os.system(f'adb -s {self.ip_device} shell am force-stop com.l1inc.yamatrack3d')
    #
    # def device_close_all(self):
    #     os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_HOME')
    #
    # def device_kill_app(self):
    #     os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_APP_SWITCH')
    #     os.system(f'adb -s {self.ip_device} shell input keyevent DEL')
    #
    # def device_get_system_volume_speaker(self):
    #     """Get value system volume speaker"""
    #     os.system(f'adb -s {self.ip_device} shell settings get system volume_alarm_speaker')
    #
    # """SETTINGS PAGES"""
    # def device_open_settings_main_page(self):
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SETTINGS')
    #
    # def device_open_wifi_settings(self):
    #     """Open pages Settings WI-FI"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIFI_SETTINGS')
    #
    # def device_open_wireless_settings(self):
    #     """Open pages Settings WireLess"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIRELESS_SETTINGS')
    #
    # def device_open_sounds_settings(self):
    #     """Open pages Settings Sounds"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SOUND_SETTINGS')
    #
    # def device_open_location_settings(self):
    #     """Open pages Settings Location"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.LOCATION_SOURCE_SETTINGS')
    #
    # def open_date_settings(self):
    #     """Open pages Settings Date"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DATE_SETTINGS')
    #
    # def open_device_info_settings(self):
    #     """Open pages Settings Device Info"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DEVICE_INFO_SETTINGS')
    #
    # def open_device_developer_options_settings(self):
    #     """Open pages Settings Developer Options"""
    #     os.system(f'adb -s {self.ip_device} shell am start -a android.settings.APPLICATION_DEVELOPMENT_SETTINGS')


if __name__ == '__main__':
    get_udid()
    device_reboot()
