# Created by dang at 10/15/24
Feature: Testing a settings page for a specific number of UI elements
       # Description: The user navigates to the settings page and verifies that
       # there are exactly 12 options and that a specific button (“connect the company”) is available.

  Scenario: User can go to settings and see the right number of UI elements
    Given Open Sign In page
    When Enter email "**********" and "*********"
    And Click Continue Button
    And Click on settings option
    Then Verify correct URL opens for settings
    And Verify there are 12 options for the settings
    And Verify “connect the company” button is available
