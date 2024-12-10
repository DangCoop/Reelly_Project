# Created by dang at 11/19/24
Feature: Testing a Off Plan Page Functionality


  Scenario: User can navigate the Off Plan page and test pagination
    # Description: User logs in to the platform, navigates to the Off Plan page,
    # and verifies pagination functionality by going to the last page and back to the first page.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on Off Plan option
    Then Verify the right page opens
    And Use the pagination button until reaching the final page
    And Use the pagination button until reaching the first page