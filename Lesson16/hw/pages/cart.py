from ..resources import common_resource, locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_monitor_is_in_cart(driver, price, title):
    driver.find_element(By.XPATH, common_resource.dynamic_locator(locators.LINK_TEMPLATE, "Cart")).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, common_resource.dynamic_locator(locators.PRODUCT_IN_CART_CARD_DETAILS_TEMPLATE, price))))
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, common_resource.dynamic_locator(locators.PRODUCT_IN_CART_CARD_DETAILS_TEMPLATE, title))))