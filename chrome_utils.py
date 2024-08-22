from selenium import webdriver


def get_driver_chrome_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--window-size=1920,1080")
    return options


