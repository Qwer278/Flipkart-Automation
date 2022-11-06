from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def initiate_driver():
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
