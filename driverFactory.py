import time

from selenium.webdriver.chrome.webdriver import WebDriver

def get_driver():
    driver = WebDriver()
    driver.maximize_window()
    return driver


