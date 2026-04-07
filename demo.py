from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


search_icon = (By.ID, "search-submit")
search_input = (By.ID, "search-field")



def navigate_to_home(driver):
    driver.get("https://sauce-demo.myshopify.com/")
    

        

def search_for_product(self, product_name):
        self.driver.find_element(*self.search_icon).click()
        search_field = self.driver.find_element(*self.search_input)
        search_field.send_keys(product_name)
        search_field.send_keys(Keys.ENTER)

