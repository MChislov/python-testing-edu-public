from ..resources import common_resource, locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_valid_credentials(driver):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, locators.BUTTON_LOGIN)))
    driver.find_element(By.XPATH, locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, locators.LOGIN_FIELD)))
    driver.find_element(By.XPATH, locators.LOGIN_FIELD).send_keys(common_resource.VALID_USERNAME)
    driver.find_element(By.XPATH, locators.PASSWORD_FIELD).send_keys(common_resource.VALID_PASSWORD)
    driver.find_element(By.XPATH, locators.BUTTON_SUBMIT_LOGIN).click()
    WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, common_resource.dynamic_locator(locators.WELCOME_TEXT, common_resource.VALID_USERNAME)))