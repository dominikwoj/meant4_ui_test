from modules.locators.main_page_locators import MainPageLocators
from modules.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in_button(self):
        self._actions.wait_for_element_clickable(MainPageLocators.sign_in_button)
        self._actions.click_element(MainPageLocators.sign_in_button)
