# Created by dang at 10/21/24
Feature: Testing a Secondary Deals Page functionality


  Scenario: User can open the Secondary deals Page and go through the Pagination
    # Description:  The user can navigates to the Secondary deals page and
    # go through the pagination from star till the end and back
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on the Secondary deals option
    Then Verify correct URL opens for secondary
    And Click the pagination button until reaching the final page
    And Click the pagination button until reaching the first page


  Scenario: User can open the Secondary deals Page and Apply Filter "want to sell"
    # Description: The user can navigates to the Secondary deals page and
    # filter the products by "want to sell" label.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on the Secondary deals option
    Then Verify correct URL opens for secondary
    And Click on Filters Button
    And Filter the products by want to sell option
    And Click on Apply filter Button
    And Verify all cards have "for sale" tag


  Scenario: User can open the Secondary deals Page and Apply Filter "want to buy"
    # Description: The user can navigates to the Secondary deals page and
    # filter the products by "want to buy" label.
    Given Open Sign In page
    When Enter email "antonov.resu@gmail.com" and "Internship2024!"
    And Click Continue Button
    And Click on the Secondary deals option
    Then Verify correct URL opens for secondary
    And Click on Filters Button
    And Filter the products by want to buy option
    And Click on Apply filter Button
    And Verify all cards have "Want to buy" tag