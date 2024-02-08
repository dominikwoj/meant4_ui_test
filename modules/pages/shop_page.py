from modules.locators.shop_page_locators import ShopPageLocators
from modules.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class ShopPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def type_text_to_search_bar(self, text) -> None:
        self._actions.send_keys(ShopPageLocators.search_bar, text)

    def click_search_button(self) -> None:
        self._actions.click_element(ShopPageLocators.search_button)

    def check_if_product_listing_is_visible(self) -> bool:
        return self._actions.is_element_displayed(ShopPageLocators.product_listing)

    def product_items(self) -> WebElement:
        return self._actions.wait_for_elements_to_be_displayed(ShopPageLocators.product_items)

    def select_item(self, product_index) -> None:
        self._actions.mouse_hover(
            self._actions.wait_for_elements_to_be_displayed(ShopPageLocators.product_link)[product_index])
        self._actions.click_element(
            self._actions.wait_for_element_to_be_displayed(ShopPageLocators.view_product_button))
