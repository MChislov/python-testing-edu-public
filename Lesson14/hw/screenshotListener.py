from robot.libraries.BuiltIn import BuiltIn

class screenshotListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def end_keyword(self, name, attrs):
        sl = None
        try:
            sl = BuiltIn().get_library_instance('SeleniumLibrary')
        except RuntimeError:
            print("SeleniumLibrary is not in use")
        if sl and 'screenshot' in attrs['tags']:
            driver = None
            try:
                driver = sl._current_browser()
            except RuntimeError:
                print("No browser open, skipping screenshot")
            if driver:
                sl.capture_page_screenshot()
