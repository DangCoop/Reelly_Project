from behave.model import Step
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Sign In page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_page()
    sleep(3)


@when('Enter email {email} and {password}')
def enter_credentials(context, email, password):
    context.app.sign_in_page.enter_email_and_pass(email, password)
    sleep(2)


@when('Click Continue Button')
def click_continue_button(context):
    context.app.sign_in_page.click_cont_button()
    sleep(10)
