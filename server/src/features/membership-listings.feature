Feature: Basic Member Listings Behaviour
  In order to verify that members can be managed
  As an administrator
  I want to interact with member records

  Background: Pre-existing Members
    Given a user list
      | username     | first_name      | last_name     |
      | a.lee        | Ash             | Lee           |
      | k.pat        | Kim             | Pat           |
    And a member list
      | user:user       | first_joined_date    |
      | 0               | 2010-01-08 12:03:12Z |
      | 1               | 2012-02-04 19:13:25Z |

  Scenario: Listing members
    Given I am an administrator
    When I request a list of members
    Then I should get a successful response
    And the response should contain:
      """
      [
        {
        "first_joined_date": "2010-01-08T12:03:12Z"
        }
      ]
      """
