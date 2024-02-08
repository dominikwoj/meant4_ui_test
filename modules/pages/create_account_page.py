from modules.locators.create_account_page_locators import CreateAccountPageLocators
from modules.pages.base_page import BasePage
from modules.user_data.user_generator import UserGenerator


class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self) -> bool:
        return (self._actions.is_element_displayed(CreateAccountPageLocators.your_personal_information_section))

    def field_form(self, user_key: str) -> None:
        user = UserGenerator.get_user(user_key)
        print(f'info: password:{user.password}')
        self._actions.send_keys(CreateAccountPageLocators.customer_firstname_input, user.first_name)
        self._actions.send_keys(CreateAccountPageLocators.customer_lastname_input, user.last_name)
        self._actions.send_keys(CreateAccountPageLocators.password_input, user.password)

    def click_register_button(self) -> None:
        self._actions.click_element(CreateAccountPageLocators.register_button)
