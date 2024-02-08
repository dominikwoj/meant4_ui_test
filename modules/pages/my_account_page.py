from modules.locators.my_account_page_locators import MyAccountLocators
from modules.pages.base_page import BasePage


class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self) -> bool:
        return self._actions.is_element_displayed(MyAccountLocators.my_account_section)

    def registered_successfully(self) -> bool:
        return self._actions.is_element_displayed(MyAccountLocators.allert_success)
