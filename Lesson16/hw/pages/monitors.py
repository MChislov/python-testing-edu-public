import time

from ..resources import common_resource, locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_costly_monitor_to_card(driver):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, locators.FIRST_PRODUCT_CARD)))
    index, price, title = _card_details(driver)
    driver.find_element(By.XPATH, common_resource.dynamic_locator(locators.PRODUCT_CARD_SELECT_TEMPLATE, str(index))).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(
        (By.XPATH, common_resource.dynamic_locator(locators.LINK_TEMPLATE, "Add to cart"))))
    driver.find_element(By.XPATH, common_resource.dynamic_locator(locators.LINK_TEMPLATE, "Add to cart")).click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    return price, title

def _card_details(driver):
    cards_len = len(driver.find_elements(By.XPATH, locators.PRODUCT_CARD_COMMON))
    prices_dict = {}
    for card_index in range(1, cards_len + 1):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, common_resource.dynamic_locator(locators.PRODUCT_CARD_TEMPLATE, str(card_index)))))
        price = driver.find_element(By.XPATH, common_resource.dynamic_locator(locators.PRODUCT_CARD_TEMPLATE, str(card_index))).text
        prices_dict[card_index] = price[1:]
    max_price = max(prices_dict.values())
    max_price_card_index = [k for k, v in prices_dict.items() if v == max_price][0]
    max_price_product_title = driver.find_element(By.XPATH, common_resource.dynamic_locator(locators.PRODUCT_CARD_TITLE_TEMPLATE, str(card_index))).text
    return max_price_card_index, max_price, max_price_product_title