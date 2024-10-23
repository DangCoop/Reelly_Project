# Created by dang at 10/21/24
Feature: Testing a secondary deals page pagination functionality
  # Description:  The user can navigates to the Secondary deals page and
  # go through the pagination from star till the end and back

  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open Sign In page
    When Enter email "***********" and "**********"
    And Click Continue Button
    And Click on the Secondary deals option
    Then Verify correct URL opens for secondary
    And Click the pagination button until reaching the final page
    And Click the pagination button until reaching the first page
