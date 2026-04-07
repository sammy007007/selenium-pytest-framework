from pages.homepage import HomePage
from pages.productpage import ProductPage


def test_add_product_to_cart(driver):
    product =ProductPage(driver)
    product.load()
    product.add_product_to_cart()
    actual_text = product.get_cart_count()
    assert "1" in actual_text

   