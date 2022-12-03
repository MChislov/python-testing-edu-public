# main_page
BUTTON_LOGIN = "//*[@id='login2']"
WELCOME_TEXT: str = "//*[text()='Welcome %d']"
LINK_TEMPLATE: str = "//*[text()='%d']"
PRODUCT_CARD_COMMON = "//div[@class='card h-100']//*[@class='card-block']/h5"
PRODUCT_CARD_TEMPLATE = "//*[@class='card h-100']/../../div['%d']//h5"
PRODUCT_CARD_TITLE_TEMPLATE = "//*[@class='card h-100']/../../div['%d']//h4[@class='card-title']/a"
PRODUCT_CARD_SELECT_TEMPLATE = "//*[@class='card h-100']/../../div['%d']"

# login_page
LOGIN_FIELD = "//*[@id='loginusername']"
PASSWORD_FIELD = "//*[@id='loginpassword']"
BUTTON_SUBMIT_LOGIN = "//button[text()='Log in']"

# monitors_page
FIRST_PRODUCT_CARD = "//*[@class='card h-100']/../../div[1]//h5"

# cart_page
PRODUCT_IN_CART_CARD_DETAILS_TEMPLATE = "//*[@class='table-responsive']//tr[@class='success']/td[text()='%d']"