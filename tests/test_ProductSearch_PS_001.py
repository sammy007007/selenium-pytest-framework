from pages.homepage import HomePage
from pages.productpage import ProductPage



def test_search_product(driver):
    home = HomePage(driver)

    home.load()
    home.search_product("snowboard")
    actual_text = home.get_first_product().text
    print(actual_text)
    assert "snowboard".lower() in actual_text.lower()


   