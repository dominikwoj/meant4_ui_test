from assertpy import assert_that
from behave import step
from modules.pages.authentication_page import AuthenticationPage
from modules.pages.create_account_page import CreateAccountPage
from modules.pages.main_page import MainPage
from modules.pages.my_account_page import MyAccountPage
from modules.pages.order_page import OrderPage
from modules.pages.product_page import ProductPage
from modules.pages.shop_page import ShopPage


@step("User Opens {param} website")
def step_impl(context, param):
    context.base_url = param
    page = MainPage(context.driver)
    page.open_page(context.base_url)


@step("User clicks on Sign in link")
def step_impl(context):
    main_page = MainPage(context.driver)
    main_page.click_sign_in_button()


@step("Authentication page is loaded")
def stem_impl(context):
    auth_page = AuthenticationPage(context.driver)
    assert_that(auth_page.is_page_loaded(), "Authentication page is not visible").is_true()


@step("Users types an random email to create an account section")
def step_impl(context):
    auth_page = AuthenticationPage(context.driver)
    auth_page.type_email_to_create_account()


@step("User clicks on Create an account button")
def step_impl(context):
    auth_page = AuthenticationPage(context.driver)
    auth_page.click_create_account_button()


@step("Create an account page is loaded")
def stem_impl(context):
    create_account_page = CreateAccountPage(context.driver)
    assert_that(create_account_page.is_page_loaded(), "Create an account page is not visible").is_true()


@step("User fields a register form as {param}")
def stem_impl(context, param):
    create_account_page = CreateAccountPage(context.driver)
    create_account_page.field_form(param)


@step("Clicks a register button")
def step_impl(context):
    create_account_page = CreateAccountPage(context.driver)
    create_account_page.click_register_button()


@step("Account registered successfully")
def stem_impl(context):
    my_account_page = MyAccountPage(context.driver)
    assert_that(my_account_page.is_page_loaded(), "My account page is not visible").is_true()
    assert_that(my_account_page.is_page_loaded(), "Incorrect registered account.").is_true()


@step("Users types an alredy registered section as {param}")
def stem_impl(context, param):
    auth_page = AuthenticationPage(context.driver)
    auth_page.field_form(param)


@step("User clicks on Sign in button")
def step_impl(context):
    auth_page = AuthenticationPage(context.driver)
    auth_page.click_sign_in_button()


@step("My account page is loaded")
def stem_impl(context):
    my_account_page = MyAccountPage(context.driver)
    assert_that(my_account_page.is_page_loaded(), "My account page is not visible").is_true()


@step("User types {param} to the search bar")
def stem_impl(context, param):
    shop_page = ShopPage(context.driver)
    shop_page.type_text_to_search_bar(param)


@step("Clicks search product button")
def stem_impl(context):
    shop_page = ShopPage(context.driver)
    shop_page.click_search_button()


@step("Product listing is visible")
def stem_impl(context):
    shop_page = ShopPage(context.driver)
    assert_that(shop_page.check_if_product_listing_is_visible(), "Product listing is not visible").is_true()


@step("Product listing contains at least one item")
def stem_impl(context):
    shop_page = ShopPage(context.driver)
    assert_that(len(shop_page.product_items())).is_greater_than_or_equal_to(1)


@step("Selects first product item")
def stem_impl(context):
    shop_page = ShopPage(context.driver)
    shop_page.select_item(0)


@step("Product page is open")
def stem_impl(context):
    product_page = ProductPage(context.driver)
    assert_that(product_page.is_page_loaded(), "Preview product page is not visible").is_true()


@step("User selects {param} color of the product")
def stem_impl(context, param):
    context.color = param
    product_page = ProductPage(context.driver)
    product_page.select_color(param)


@step("Product is available")
def stem_impl(context):
    product_page = ProductPage(context.driver)
    assert_that(product_page.product_is_available(), f"{context.color} product is not available").is_true()


@step("User adds the product to cart")
def stem_impl(context):
    product_page = ProductPage(context.driver)
    product_page.add_to_cart()
    product_page.proceed_to_checkout()


@step("Order page is open")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    assert_that(order_page.is_page_loaded(), "Order page is not open").is_true()


@step("User continues order on Summary section")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    order_page.click_procced_on_summary()


@step("User continues order on Address section")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    order_page.click_procced_on_address()


@step("User agrees to the terms and proceeds")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    order_page.agree_terms_and_procced_on_shipping()


@step("Selects Pay by bank wire")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    order_page.pay_by_bank_wire()


@step("Confirms order")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    order_page.confirm_order()


@step("Successfully order complete")
def stem_impl(context):
    order_page = OrderPage(context.driver)
    order_page.successfully_order_complete()
