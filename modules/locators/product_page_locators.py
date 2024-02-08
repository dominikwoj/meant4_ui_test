from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class ProductPageLocators:
    preview_product_page_id: By = (By.XPATH, "//body[@id='product']")
    in_stock_label: By = (By.ID, "availability_statut")
    add_to_cart_button: By = (By.ID, "add_to_cart")
    proceed_to_checkout_button: By = (By.XPATH, "//div[@id='layer_cart']//div[@class='clearfix']//a")

    @staticmethod
    def color_pick_item(color):
        return (By.XPATH, f"//ul[@id='color_to_pick_list']//a[@title='{color}']")
