from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class ProductPage(BasePage) :
    URL ="https://adnabu-store-assignment1.myshopify.com/products/the-complete-snowboard?_pos=1&_sid=5e7408530&_ss=r"
    add_to_cart_button = (By.XPATH,"//button[@name='add']")
    my_cart_count = (By.XPATH,"//input[@class='quantity__input']")
    your_cart_logo = (By.XPATH,"//h2[text()='Your cart']")


    def load(self):
        self.open_url(self.URL)
    
    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)
        self.wait_for_text(self.your_cart_logo,"Your cart")
    

    def get_cart_count(self):
         return self.get_text(self.my_cart_count).get_attribute("value")

    