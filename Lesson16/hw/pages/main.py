from ..resources import common_resource, locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login_valid_credentials():
    driver = webdriver.Chrome()
    driver.get(common_resource.BASE_URL)
    WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, locators.LOGIN_FIELD))
    driver.find_element(By.XPATH, locators.LOGIN_FIELD).send_keys(common_resource.VALID_USERNAME)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(common_resource.VALID_PASSWORD)
    driver.find_element(By.XPATH, locators.WELCOME_TEXT).click()
    WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, common_resource.dynamic_locator(
        locators.WELCOME_TEXT, common_resource.VALID_USERNAME)))
    driver.close()

login_valid_credentials()
