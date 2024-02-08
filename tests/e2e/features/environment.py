from behave import fixture, use_fixture
from modules.pages.selenium_factory import DriverFactory


@fixture
def selenium_browser_chrome(context):
    context.driver = DriverFactory.create_driver('chrome')
    context.driver.set_page_load_timeout(30)
    yield context.driver
    context.driver.close()
    context.driver.quit()


def before_all(context):
    context.selenium_browser = selenium_browser_chrome
    use_fixture(context.selenium_browser, context)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
