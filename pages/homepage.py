from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class HomePage(BasePage):

    URL = "https://sauce-demo.myshopify.com/"

    # Locators
    search_icon = (By.ID, "search-submit")
    search_input = (By.ID, "search-field")
    first_product = (By.XPATH,"//a[@id='product-1']//h3")


    def load(self):
        self.open_url(self.URL)

    def search_product(self, product_name):
        self.type(self.search_input, product_name)
        self.find(self.search_icon).submit()
    
    def get_first_product(self):
        return self.get_text(self.first_product) 
