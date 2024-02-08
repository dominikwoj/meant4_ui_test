from modules.locators.product_page_locators import ProductPageLocators
from modules.pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self) -> bool:
        self._actions.wait_for_element_to_be_displayed(ProductPageLocators.preview_product_page_id)
        return self._actions.is_element_displayed(ProductPageLocators.preview_product_page_id)

    def select_color(self, color):
        self._actions.click_element(ProductPageLocators.color_pick_item(color))

    def product_is_available(self):
        return self._actions.wait_for_element_to_be_displayed(ProductPageLocators.in_stock_label)

    def add_to_cart(self):
        self._actions.wait_for_element_to_be_displayed(ProductPageLocators.add_to_cart_button)
        self._actions.wait_for_element_clickable(ProductPageLocators.add_to_cart_button)
        self._actions.click_element(ProductPageLocators.add_to_cart_button)

    def proceed_to_checkout(self):
        self._actions.wait_for_element_clickable(ProductPageLocators.proceed_to_checkout_button)
        self._actions.click_element(ProductPageLocators.proceed_to_checkout_button)
