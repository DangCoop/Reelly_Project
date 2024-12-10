def paginate(self, direction="next", max_pages=None, next_button_selector=None, prev_button_selector=None,
             page_number_selector=None):
    """
    A universal pagination function for navigating through pages.

    :param direction: "next" for navigating forward, "prev" for navigating backward.
    :param max_pages: Maximum number of pages to navigate (optional).
    :param next_button_selector: Locator tuple for the "Next" button.
    :param prev_button_selector: Locator tuple for the "Previous" button.
    :param page_number_selector: Locator tuple for the current page number.
    """
    assert direction in ["next", "prev"], "Direction must be either 'next' or 'prev'."

    page_count = 0

    while True:
        # Optional: Stop if a max page count is provided
        if max_pages and page_count >= max_pages:
            print(f"Pagination stopped after {page_count} pages.")
            break

        # Wait for the current page number to be visible
        current_page_element = self.wait.until(
            EC.visibility_of_element_located(page_number_selector)
        )
        current_page_number = int(current_page_element.text)
        print(f"Currently on page {current_page_number}")

        # Determine which button to click (Next or Previous)
        button_selector = next_button_selector if direction == "next" else prev_button_selector
        try:
            button = self.wait.until(EC.element_to_be_clickable(button_selector))
            if not button.is_enabled():
                print(f"Pagination stopped. Reached the end in direction: {direction}.")
                break

            # Click the button to navigate
            button.click()
            page_count += 1

            # Optional: Wait for the page number to update
            self.wait.until(
                EC.text_to_be_present_in_element(page_number_selector,
                                                 str(current_page_number + (1 if direction == "next" else -1)))
            )
            sleep(2)  # Add delay if necessary for dynamic loading
        except Exception as e:
            print(f"Pagination failed: {e}")
            break

#Example for Navigating to the Final Page:

from selenium.webdriver.common.by import By
from base_page import BasePage

class OffPlanPage(BasePage):
    NEXT_BUTTON = (By.CSS_SELECTOR, ".pagination__button.next")
    PREV_BUTTON = (By.CSS_SELECTOR, ".pagination__button.prev")
    PAGE_NUMBER = (By.CSS_SELECTOR, ".current-page")

    def navigate_to_final_page(self):
        self.paginate(
            direction="next",
            next_button_selector=self.NEXT_BUTTON,
            page_number_selector=self.PAGE_NUMBER
        )


#Example for Navigating Back to the First Page:
class OffPlanPage(BasePage):
    NEXT_BUTTON = (By.CSS_SELECTOR, ".pagination__button.next")
    PREV_BUTTON = (By.CSS_SELECTOR, ".pagination__button.prev")
    PAGE_NUMBER = (By.CSS_SELECTOR, ".current-page")

    def navigate_to_first_page(self):
        self.paginate(
            direction="prev",
            prev_button_selector=self.PREV_BUTTON,
            page_number_selector=self.PAGE_NUMBER
        )

