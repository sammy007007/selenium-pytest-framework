from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    

    def wait_for_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))
