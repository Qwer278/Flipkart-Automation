from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.service import Service
s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)


@pytest.fixture()
def initiate_driver():
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
