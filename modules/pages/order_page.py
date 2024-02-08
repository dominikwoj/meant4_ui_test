from assertpy import assert_that
from modules.locators.order_page_locators import OrderPageLocators
from modules.pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self) -> bool:
        return self._actions.is_element_displayed(OrderPageLocators.order_page_id)

    def click_procced_on_summary(self) -> None:
        current_step = 'Summary'
        assert_that(self._actions.wait_for_element_to_be_displayed(OrderPageLocators.current_step_label).text,
                    f'Current step is not {current_step}').contains(current_step)
        self._actions.wait_for_element_clickable(OrderPageLocators.procced_to_checkout_on_summary_section)
        self._actions.click_element(OrderPageLocators.procced_to_checkout_on_summary_section)

    def click_procced_on_address(self) -> None:
        current_step = 'Address'
        assert_that(self._actions.wait_for_element_to_be_displayed(OrderPageLocators.current_step_label).text,
                    f'Current step is not {current_step}').contains(current_step)
        self._actions.wait_for_element_clickable(OrderPageLocators.procced_to_checkout_on_address_section)
        self._actions.click_element(OrderPageLocators.procced_to_checkout_on_address_section)

    def agree_terms_and_procced_on_shipping(self) -> None:
        current_step = 'Shipping'
        assert_that(self._actions.wait_for_element_to_be_displayed(OrderPageLocators.current_step_label).text,
                    f'Current step is not {current_step}').contains(current_step)
        self._actions.wait_for_element_to_be_displayed(OrderPageLocators.agree_terms_label)
        self._actions.click_element(OrderPageLocators.agree_terms_label)
        self._actions.wait_for_element_clickable(OrderPageLocators.procced_to_checkout_on_shipping_section)
        self._actions.click_element(OrderPageLocators.procced_to_checkout_on_shipping_section)

    def pay_by_bank_wire(self) -> None:
        self._actions.wait_for_element_to_be_displayed(OrderPageLocators.pay_by_bank_wire)
        self._actions.click_element(OrderPageLocators.pay_by_bank_wire)

    def confirm_order(self) -> None:
        current_step = 'Payment'
        assert_that(self._actions.wait_for_element_to_be_displayed(OrderPageLocators.current_step_label).text,
                    f'Current step is not {current_step}').contains(current_step)
        self._actions.wait_for_element_clickable(OrderPageLocators.procced_to_checkout_on_payment_section)
        self._actions.click_element(OrderPageLocators.procced_to_checkout_on_payment_section)

    def successfully_order_complete(self) -> None:
        message_element = self._actions.wait_for_element_to_be_displayed(
            OrderPageLocators.successfully_order_complete_message)
        assert_that(message_element.text, 'The order completion successfully message is incorrect.').contains(
            'Your order on My Shop is complete.')
