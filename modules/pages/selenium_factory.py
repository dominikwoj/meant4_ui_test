from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def _chrome_driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--lang=en-US")
    return webdriver.Chrome(options=options, service=None)


class DriverFactory:
    Drivers = {
        'chrome': _chrome_driver,
    }

    @classmethod
    def create_driver(cls, driver_type):
        if driver_type not in cls.Drivers:
            raise ValueError
        return cls.Drivers[driver_type]()
