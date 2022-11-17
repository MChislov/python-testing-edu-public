from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
assert "Swag Labs" in driver.title
add_username = driver.find_element(By.NAME, "user-name").send_keys("standard_user")
add_password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
click_login_button = driver.find_element(By.XPATH, "//*[@type='submit']").click()
assert "Epic sadface: Username and password do not match any user in this service" not in driver.page_source
assert "Sauce Labs Backpack" in driver.page_source
driver.close()