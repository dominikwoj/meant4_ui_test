from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class MyAccountLocators:
    my_account_section: By = (By.XPATH, "//div[@id='center_column']//*[text()='My account']")
    allert_success: By = (By.XPATH, "//p[@class='alert alert-success']")
