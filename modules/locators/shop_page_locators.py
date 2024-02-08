from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class ShopPageLocators:
    search_bar: By = (By.ID, "search_query_top")
    search_button: By = (By.NAME, "submit_search")
    product_listing: By = (By.XPATH, "//h1[@class='page-heading  product-listing']")
    product_items: By = (By.XPATH, "//ul[contains(@class,'product_list')]/li")
    product_link: By = (By.XPATH, "//a[@class='product_img_link']/img")
    view_product_button: By = (By.XPATH, "//a[@class='button lnk_view btn btn-default']")
