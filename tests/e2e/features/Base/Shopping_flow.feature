@allure.label.epic=Shopping

Feature: Shopping in the app
  I want to check if I can shopping in the app

  @allure.label.author:dominik_wojnowski
  Scenario Outline: Shopping flow
    Given User opens <website> website
    When User clicks on Sign in link
    Then Authentication page is loaded
    When Users types an alredy registered section as Registered user
    And User clicks on Sign in button
    Then My account page is loaded
    When User types Blouse to the search bar
    And Clicks search product button
    Then Product listing is visible
    And Product listing contains at least one item
    When Selects first product item
    Then Product page is open
    When User selects White color of the product
    Then Product is available
    When User adds the product to cart
    Then Order page is open
    When User continues order on Summary section
    And User continues order on Address section
    And User agrees to the terms and proceeds
    And Selects Pay by bank wire
    And Confirms order
    Then Successfully order complete

    Examples:
      | website                       |
      | https://automationpractice.pl |
