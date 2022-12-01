import pytest
import pages.main as main


def test_01_login():
    main.login_valid_credentials()


def test_02_add_monitor_to_cart():
    pass
