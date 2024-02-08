from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumActions:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.5,
                             ignored_exceptions=(ElementClickInterceptedException, NoSuchElementException)
                             ).until(ec.element_to_be_clickable(locator))

    def wait_for_element_to_be_displayed(self, locator, timeout=DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout).until(
            ec.visibility_of_element_located(locator))

    def wait_for_elements_to_be_displayed(self, locator, timeout=DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout).until(
            ec.visibility_of_all_elements_located(locator))

    def is_element_displayed(self, locator, timeout=DEFAULT_TIMEOUT) -> bool:
        try:
            self.wait_for_element_to_be_displayed(locator, timeout)
        except TimeoutException:
            return False
        else:
            return True

    def send_keys(self, locator, value) -> None:
        element = self.wait_for_element_clickable(locator)
        element.clear()
        element.send_keys(value)

    def click_element(self, locator, timeout=DEFAULT_TIMEOUT) -> None:
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def mouse_hover(self, element) -> None:
        return ActionChains(self.driver).move_to_element(element).perform()
