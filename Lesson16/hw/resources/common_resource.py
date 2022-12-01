# urls
BASE_URL = "https://www.demoblaze.com"

# Credentials

VALID_USERNAME = "mc1"
VALID_PASSWORD = "mc1pass"


# useful_keywords
def dynamic_locator(locator: str, replace_string: str):
    locator = locator.replace("%d", replace_string)
    return locator
