from behave import given, when, then


@then('Verify the right page opens')
def open_off_page(context):
    context.app.off_plan_page.verify_off_plan_page_enter()


@then('Use the pagination button until reaching the final page')
def click_the_pagination_button_next(context):
    context.app.off_plan_page.go_to_last_page()


@then('Use the pagination button until reaching the first page')
def click_the_pagination_button_previous(context):
    context.app.off_plan_page.go_to_first_page()