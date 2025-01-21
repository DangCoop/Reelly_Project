from behave import given, when, then


@then('Verify the "Market" page opens')
def open_market_page_verification(context):
    context.app.market_page.verify_market_page()


@then('Navigate to the final page using pagination')
def navigate_to_final_page(context):
    context.app.market_page.go_to_final_page()


@then('Navigate back to the first page using pagination')
def navigate_to_previous_page(context):
    context.app.market_page.go_to_first_page()