# Created by dang at 1/20/25
Feature: Testing a Market Page Functionality


  Scenario: User can open the Market tab and navigate through pagination
    # Description: This feature tests the navigation to the Market tab and verifies
    # the pagination functionality to the final and first page.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on "Market" in the left-side menu
    Then Verify the "Market" page opens
    And Navigate to the final page using pagination
    And Navigate back to the first page using pagination