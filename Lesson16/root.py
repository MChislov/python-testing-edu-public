from hw.tests import TC_01_login
from hw.tests import TC_02_add_monitor_to_cart
from hw.tests import FX_login


def test_01():
    TC_01_login()

def test_02(FX_login):
    TC_02_add_monitor_to_cart(FX_login)