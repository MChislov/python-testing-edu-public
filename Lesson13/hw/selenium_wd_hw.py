from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
assert "Swag Labs" in driver.title
username_element = driver.find_element(By.NAME, "user-name")
username_element.clear()
username_element.send_keys("standard_user")
password_element = driver.find_element(By.ID, "password")
password_element.clear()
password_element.send_keys("secret_sauce")
login_button_elem = driver.find_element(By.XPATH, "//*[@type='submit']")
login_button_elem.click()
assert "Epic sadface: Username and password do not match any user in this service" not in driver.page_source
driver.close()