@allure.label.epic=Register

Feature: Register an account
  I want check if I can to register an account

  @allure.label.author:dominik_wojnowski
  Scenario Outline: Register an random account
    Given User opens <website> website
    When User clicks on Sign in link
    Then Authentication page is loaded
    When Users types an random email to create an account section
    And User clicks on Create an account button
    Then Create an account page is loaded
    When User fields a register form as Common user
    And Clicks a register button
    Then Account registered successfully

    Examples:
      | website                       |
      | https://automationpractice.pl |
