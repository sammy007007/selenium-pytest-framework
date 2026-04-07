from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class ProductPage(BasePage) :
    URL ="https://sauce-demo.myshopify.com/products/striped-top?_pos=1&_sid=69495c96c&_ss=r"
    add_to_cart_button = (By.XPATH,"//input[@id='add']")
    my_cart_count = (By.XPATH,"//a[text()='My Cart ']/span/span")

    def load(self):
        self.open_url(self.URL)
    
    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)
        self.wait_for_text(self.my_cart_count,"(1)")
    

    def get_cart_count(self):
         return self.get_text(self.my_cart_count)

    