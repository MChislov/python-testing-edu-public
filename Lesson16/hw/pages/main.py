from ..resources import common_resource, locators
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_main_page():
    driver = webdriver.Chrome()
    driver.get(common_resource.BASE_URL)
    driver.maximize_window()
    return driver

def open_monitors_list(driver):
    driver.find_element(By.XPATH, common_resource.dynamic_locator(locators.LINK_TEMPLATE, "Monitors")).click()
    time.sleep(3)

def close_page(driver):
    driver.close()
