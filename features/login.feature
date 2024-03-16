Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM homepage
    And Enter username "student" and password "Password123"
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I launch Chrome browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page
    Examples:
      | username | password |
      | student | Password123 |
      | student123 | Password |
#      | studentxyz | Password123 |
#      | student | Passwordxyz |

