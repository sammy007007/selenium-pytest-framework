from pages.homepage import HomePage
from pages.productpage import ProductPage



def test_search_product(driver):
    home = HomePage(driver)

    home.load()
    home.search_product("jacket")
    actual_text =home.get_first_product()
    print(actual_text)
    assert "jacket".lower() in actual_text.lower()


   