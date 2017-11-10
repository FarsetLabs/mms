Feature: Basic Django Behaviour
  In order to verify that Django and Behave are working
  As a developer
  I want to try to access the "It's working" page

  Scenario: Accessing the Root URL
    When I access the root URL
    Then the response will not be empty
