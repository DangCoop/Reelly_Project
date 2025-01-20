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
    # Description: User logs in, navigates to the Off Plan page, filters products by price range,
    # and verifies that all displayed products fall within the specified range.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on Off Plan option
    Then Verify the right page opens
    And Open filter menu
    And Use filter by price range from "1200000" to "2000000" AED
    And Apply Filter
    And Checking that the price in all cards is inside the range (1200000 - 2000000)

  Scenario: User can see titles and pictures on each product inside the Off Plan page
    # Description: This scenario verifies that each product on the Off Plan page
    # contains a visible title and picture.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on Off Plan option
    Then Verify the right page opens
    And Verify each product contains a visible title and picture

  Scenario: User can filter products by sale status of "Out of Stocks"
    #This scenario ensures that users can successfully apply a filter
    # by sale status "Out of Stocks" on the Off Plan page. And only products marked with
    # the "Out of Stocks" tag are displayed on the page.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on Off Plan option
    Then Verify the right page opens
    And Click on Sale status Filter
    And Filter by sale status of "Out of Stocks"
    And Verify each product contains the "Out of Stocks" tag

  Scenario:  User can open product detail and see three options of visualization
    #This scenario validates the visualization options for a product on the Off Plan page.
    # It ensures that the first product in the list displays the expected visualization options ("architecture", "interior", and "lobby")
    # and verifies that these options are visible and clickable.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on Off Plan option
    Then Click on the first project
    And Verify the visualization options are Architecture,Interior,Lobby
    And Verify the visualization options are clickable
