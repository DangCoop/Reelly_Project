from behave import given, when, then
from time import sleep


@then('Click the pagination button until reaching the final page')
def pagination_up_function(context):
    context.app.secondary_page.go_to_final_page()


@then('Click the pagination button until reaching the first page')
def pagination_down_function(context):
    context.app.secondary_page.back_to_first_page()


@then('Click on Filters Button')
def filters_button(context):
    context.app.secondary_page.click_filters_button()


@then('Filter the products by want to sell option')
def choose_sell_filter(context):
    context.app.secondary_page.choose_want_to_sell_option()

@then('Filter the products by want to buy option')
def choose_buy_filter(context):
    context.app.secondary_page.choose_want_to_buy_option()


@then('Click on Apply filter Button')
def apply_filter_button(context):
    context.app.secondary_page.click_apply_filter_button()


@then('Verify all cards have "for sale" tag')
def verify_for_sale_tag_available(context):
    context.app.secondary_page.verify_sell_filter_works()


@then('Verify all cards have "Want to buy" tag')
def verify_want_to_buy_tag_available(context):
    context.app.secondary_page.verify_buy_filter_works()