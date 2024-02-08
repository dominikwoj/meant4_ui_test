from modules.locators.authentication_page_locators import AuthenticationPageLocators
from modules.pages.base_page import BasePage
from modules.user_data.user_generator import UserGenerator


class AuthenticationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self) -> bool:
        return (self._actions.is_element_displayed(AuthenticationPageLocators.authentication_section) and
                self._actions.is_element_displayed(AuthenticationPageLocators.email_create_input) and
                self._actions.is_element_displayed(AuthenticationPageLocators.create_account_button))

    def type_email_to_create_account(self) -> None:
        email = UserGenerator.generate_email_address()
        print(f'info: email:{email}')
        self._actions.send_keys(AuthenticationPageLocators.email_create_input, email)

    def click_create_account_button(self):
        self._actions.click_element(AuthenticationPageLocators.create_account_button)

    def field_form(self, user_key: str) -> None:
        user = UserGenerator.get_user(user_key)
        print(f"info: user_key:{user_key}| user:{user}")
        self._actions.send_keys(AuthenticationPageLocators.email_input, user.email)
        self._actions.send_keys(AuthenticationPageLocators.password_input, user.password)

    def click_sign_in_button(self):
        self._actions.click_element(AuthenticationPageLocators.sign_in_button)
