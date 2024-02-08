from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class CreateAccountPageLocators:
    your_personal_information_section: By = (By.XPATH, "//form[@id='account-creation_form']")
    customer_firstname_input: By = (By.ID, "customer_firstname")
    customer_lastname_input: By = (By.ID, "customer_lastname")
    password_input: By = (By.ID, "passwd")
    register_button: By = (By.ID, "submitAccount")
