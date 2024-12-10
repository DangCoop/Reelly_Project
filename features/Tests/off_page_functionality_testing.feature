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

  Scenario: Users can filter the off plan products by Unit price range
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on Off Plan option
    Then Verify the right page opens
    And Open filter menu
    And Use filter by price range from "1200000" to "2000000" AED
    And Apply Filter
    And Checking that the price in all cards is inside the range (1200000 - 2000000)
