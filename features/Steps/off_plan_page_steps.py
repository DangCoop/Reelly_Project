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

@then('Open filter menu')
def open_filter_menu(context):
    context.app.off_plan_page.open_filter()


@then('Use filter by price range from {price1} to {price2} AED')
def filter_products_by_price_range(context, price1, price2):
    context.app.off_plan_page.filter_by_price(price1, price2)


@then('Apply Filter')
def click_apply_filter(context):
    context.app.off_plan_page.apply_filter()


@then('Checking that the price in all cards is inside the range (1200000 - 2000000)')
def verify_price_inside_range_in_all_cards(context):
    context.app.off_plan_page.verify_price_range()


@then('Verify each product contains a visible title and picture')
def verify_projects_title_and_picture(context):
    context.app.off_plan_page.check_title_and_img()


@then('Click on Sale status Filter')
def click_sale_status_filter(context):
    context.app.off_plan_page.open_sales_status_filter()

@then('Filter by sale status of "Out of Stocks"')
def filter_out_out_stocks(context):
    context.app.off_plan_page.select_out_off_stock_status()

@then('Verify each product contains the "Out of Stocks" tag')
def verify_product_contains_out_stocks(context):
    context.app.off_plan_page.check_out_off_stock_status()

@then('Click on the first project')
def click_first_product(context):
    context.app.off_plan_page.go_to_first_project()

@then('Verify the visualization options are {option1},{option2},{option3}')
def verify_visualization_options(context, option1, option2, option3):
    context.app.off_plan_page.check_visualization_options(option1, option2, option3)


@then('Verify the visualization options are clickable')
def verify_visualization_options_clickable(context):
    context.app.off_plan_page.check_visualization_options_clickable()
