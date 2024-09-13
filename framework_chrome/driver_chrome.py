from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DriverChrome:
    chrome_instance: webdriver.Chrome = None

    @classmethod
    def start(cls, options: webdriver.ChromeOptions) -> None:
        print("__start_chrome__")
        cls.chrome_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    @classmethod
    def finish(cls) -> None:
        print("__finish_chrome__")
        cls.chrome_instance.quit()
        cls.chrome_instance = None
