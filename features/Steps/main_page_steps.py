from behave import given, when, then
from time import sleep


@when('Click on settings option')
def settings(context):
    context.app.main_page.click_settings_button()
    sleep(6)