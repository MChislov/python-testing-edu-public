import pytest
from .pages import *

@pytest.fixture
def FX_login():
    driver = open_main_page()
    login_valid_credentials(driver)
    return driver


def TC_01_login():
    driver = open_main_page()
    login_valid_credentials(driver)
    close_page(driver)


def TC_02_add_monitor_to_cart(driver):
    open_monitors_list(driver)
    price, title = add_costly_monitor_to_card(driver)
    check_monitor_is_in_cart(driver, price, title)
    close_page(driver)
