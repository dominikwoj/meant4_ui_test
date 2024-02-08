from modules.pages.selenium_actions import SeleniumActions
from retry import retry


class BasePage:

    def __init__(self, driver):
        self._actions = SeleniumActions(driver)

    @retry(AssertionError, tries=2, delay=2.0)
    def open_page(self, url):
        self._actions.driver.get(url)
