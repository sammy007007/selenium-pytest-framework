import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driverFactory import get_driver
def pytest_addoption(parser):
    parser.addoption("--store-pass", action="store")

@pytest.fixture(scope="function")
def driver(request):
    store_password = request.config.getoption("--store-pass")
    driver=get_driver()
    wait = WebDriverWait(driver, 10) 
    driver.get("https://adnabu-store-assignment1.myshopify.com/password")
    driver.set_page_load_timeout(15)
    driver.find_element(By.ID,"password").send_keys(store_password+ Keys.ENTER)
    wait.until(EC.invisibility_of_element_located((By.ID, "password"))) 

    yield driver
    driver.quit()