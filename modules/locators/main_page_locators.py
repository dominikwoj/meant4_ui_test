from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class MainPageLocators:
    sign_in_button: By = (By.XPATH, "//a[@class='login']")
    authentication_site: By = (By.XPATH, "//input[@id='email_create']")
    email_create_input: By = (By.XPATH, "//input[@id='email_create']")
