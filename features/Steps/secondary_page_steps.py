from behave import given, when, then
from time import sleep


@then('Click the pagination button until reaching the final page')
def pagination_up_function(context):
    context.app.secondary_page.go_to_final_page()


@then('Click the pagination button until reaching the first page')
def pagination_down_function(context):
    context.app.secondary_page.back_to_first_page()