from selenium.webdriver.common.by import By
from Locators.HomepageLocator import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.configdata import *
from conftest import *


class Util:
    def find(self, element):
        if element.startswith('//'):
            found_element = driver.find_element(by=By.XPATH, value=element)
        else:
            found_element = driver.find_element(by=By.CSS_SELECTOR, value=element)
        return found_element

    def click_on(self, element):
        self.find(element).click()

    def wait_for(self, element):
        if element.startswith('//'):
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, element)))
        else:
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))

    def move_to(self, element):
        action = ActionChains(driver)
        if element.startswith('//'):
            moving_element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, profile)))
            return action.move_to_element(moving_element)
        else:
            moving_element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, profile)))
            return action.move_to_element(moving_element)

    def switch_tab_to(self, num):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[num])

    def find_all(self, element):
        if element.startswith('//'):
            find_all_element = driver.find_elements(by=By.XPATH, value=element)
        else:
            find_all_element = driver.find_elements(by=By.CSS_SELECTOR, value=element)
        return find_all_element
