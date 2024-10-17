from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@then('Verify correct URL opens for settings')
def correct_url_opens(context):
    context.app.settings_page.verify_url()


@then('Verify there are {number} options for the settings')
def verify_number_of_options(context, number):
    context.app.settings_page.verify_numbers_of_settings(number)



@then('Verify “connect the company” button is available')
def verify_connect_company_button(context):
    context.app.settings_page.verify_button_availability()

