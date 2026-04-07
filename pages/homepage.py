from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class HomePage(BasePage):

    URL = "https://adnabu-store-assignment1.myshopify.com/"
    

    # Locators
    search_icon = (By.XPATH, "//summary[@aria-label='Search']")
    search_input = (By.XPATH, "//input[@id='Search-In-Modal']")
    first_product = (By.XPATH,"//h3[@class='card__heading h5']//a")


    def load(self):
        self.open_url(self.URL)

    def search_product(self, product_name):
        self.click(self.search_icon)
        self.type(self.search_input, product_name)
        
    
    def get_first_product(self):
        return self.get_text(self.first_product) 
