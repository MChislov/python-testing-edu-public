from robot.libraries.BuiltIn import BuiltIn

def get_max_price_card_details():
        sl = None
        try:
            sl = BuiltIn().get_library_instance('SeleniumLibrary')
        except RuntimeError:
            print("SeleniumLibrary is not in use")
        if sl:
            driver = None
            try:
                driver = sl._current_browser()
            except RuntimeError:
                print("No browser open, skipping screenshot")
            if driver:
                index, price, max_price_product_title = _card_details(sl)
                return index, price, max_price_product_title

def _card_details(sl):
    cards_len = sl.get_element_count("//div[@class='card h-100']//*[@class='card-block']/h5")
    prices_dict = {}
    for card_index in range(1, cards_len+1):
        sl.wait_until_element_is_visible("//*[@class='card h-100']/../../div[" + str(card_index) + "]//h5")
        price = sl.get_text("//*[@class='card h-100']/../../div[" + str(card_index) + "]//h5")
        prices_dict[card_index] = price[1:]
    max_price = max(prices_dict.values())
    max_price_card_index = [k for k, v in prices_dict.items() if v == max_price][0]
    max_price_product_title = sl.get_text("//*[@class='card h-100']/../../div[" + str(max_price_card_index) + "]//h4[@class='card-title']/a")
    return max_price_card_index, max_price, max_price_product_title

