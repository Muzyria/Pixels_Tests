import os
import random
import time

import android_utils
from android_utils import *
import subprocess


def convert_time(time_str):
    # Если длина строки 3, добавляем ведущий ноль
    if len(time_str) == 3:
        time_str = '0' + time_str

    # Разбиваем строку на часы и минуты
    hours = time_str[:-2]  # все символы кроме последних двух
    minutes = time_str[-2:]  # последние два символа

    # Возвращаем результат в формате HH:MM
    return f"{hours}:{minutes}"


def log_message(message):
    with open("tests/test_logs/log_scheduler.txt", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

# def run_adb_logcat():
#     # Запуск команды adb logcat
#     process = subprocess.Popen('adb logcat -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, _ = process.communicate()
#     return output.decode('utf-8', errors='ignore')
#
#
#
# def check_for_message(message_to_find,  interval=30, timeout=600):
#     """
#     Проверка adb логов на наличие определённого сообщения.
#
#     :param message_to_find: Сообщение, которое необходимо найти.
#     :param interval: Интервал в секундах между выполнением команды adb logcat.
#     :param timeout: Время ожидания в секундах до прекращения поиска.
#     :return: True, если сообщение найдено, False - если тайм-аут истек.
#     """
#
#     start_time = time.time()
#     start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
#     print(f"Начало ожидания сообщения в {start_time_readable}, тайм-аут: {timeout} секунд")
#
#
#     last_adb_execution_time = 0  # Время последнего выполнения команды
#
#     while time.time() - start_time < timeout:
#         current_time = time.time()
#
#         # Выполняем adb logcat с интервалом
#         if current_time - last_adb_execution_time >= interval:
#             # self.adb_command.swipe_screen(100, 500, 200, 500, 250)
#             # self.adb_command.swipe_screen(200, 500, 100, 500, 250)
#             print("-----ADB COMMAND----------------------------------------------")
#             last_adb_execution_time = current_time
#             try:
#                 output = run_adb_logcat()
#                 if message_to_find in output:
#                     end_time = time.time()
#                     end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
#                     duration = int(end_time - start_time)
#                     print(
#                         f"Сообщение '{message_to_find}' найдено в {end_time_readable}, время ожидания: {duration} секунд")
#                     return True
#             except Exception as e:
#                 print(f"Ошибка при поиске сообщения в логе: {e}")
#
#         # Ждем 1 секунду перед повторной проверкой
#         time.sleep(1)
#
#     print(f"Сообщение '{message_to_find}' не найдено за {timeout} секунд.")
#     return False


if __name__ == '__main__':
    # get_udid()
    # android_utils.get_wakefulness_status()
    # android_utils.wake_up_device()
    # Пример использования
    check_for_message("CartCommand MATRIX_MODE = 2")
