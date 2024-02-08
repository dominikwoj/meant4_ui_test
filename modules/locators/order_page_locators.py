from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class OrderPageLocators:
    order_page_id: By = (By.ID, "order")
    current_step_label: By = (By.XPATH, "//li[contains(@class,'step_current')]")
    procced_to_checkout_on_summary_section: By = (
        By.XPATH, "//p[@class='cart_navigation clearfix']//a[@title='Proceed to checkout']")
    procced_to_checkout_on_address_section: By = (
        By.XPATH, "//button[@type='submit' and @name='processAddress']")
    procced_to_checkout_on_shipping_section: By = (
        By.XPATH, "//button[@type='submit' and @name='processCarrier']")

    agree_terms_label: By = (By.XPATH, "//label[@for='cgv']")
    pay_by_bank_wire: By = (By.XPATH, "//a[@class='bankwire']")
    procced_to_checkout_on_payment_section: By = (
        By.XPATH, "//p[@id='cart_navigation']//button[@type='submit']")
    successfully_order_complete_message: By = (By.XPATH, "//p[@class='alert alert-success']")
