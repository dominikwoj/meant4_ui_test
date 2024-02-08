@allure.label.epic=Login

Feature: Log in to the app
  I want to check if I can log in to the web application

  @allure.label.author:dominik_wojnowski
  Scenario Outline: Log in the app
    Given User opens <website> website
    When User clicks on Sign in link
    Then Authentication page is loaded
    When Users types an alredy registered section as Registered user
    And User clicks on Sign in button
    Then My account page is loaded

    Examples:
      | website                       |
      | https://automationpractice.pl |
