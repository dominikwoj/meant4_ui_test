from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class AuthenticationPageLocators:
    authentication_section: By = (By.XPATH, "//*[text()='Authentication']")
    email_create_input: By = (By.XPATH, "//input[@id='email_create']")
    create_account_button: By = (By.XPATH, "//button[@id='SubmitCreate']")
    email_input: By = (By.ID, "email")
    password_input: By = (By.ID, "passwd")
    sign_in_button: By = (By.ID, "SubmitLogin")
