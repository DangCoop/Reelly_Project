from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class OffPlanPage(Page):
    TOTAL_PAGE_SELECTOR = (By.CSS_SELECTOR, "div[wized='totalPageProperties']")
    CURRENT_PAGE_SELECTOR = (By.CSS_SELECTOR, "[wized='currentPageProperties']")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, ".pagination__button.w-inline-block")
    PREV_PAGE_BUTTON = (By.CSS_SELECTOR, "[wized='previousPageProperties']")

    def verify_off_plan_page_enter(self):
        expected_text = 'Total projects'
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text
        assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

    def go_to_last_page(self):
        try:
            # Retrieve the total number of pages from the web page
            total_pages_element = self.driver.find_element(*self.TOTAL_PAGE_SELECTOR)
            sleep(3)
            total_pages = int(total_pages_element.text)  # Example: If the element text is "10"
            print(f'Total pages: {total_pages}')

            # Continuously navigate through pages until reaching the last one
            while True:
                # 1. Retrieve the current page number from the page
                current_page_element = self.driver.find_element(*self.CURRENT_PAGE_SELECTOR)
                current_page_number = int(current_page_element.text)

                # 2. Ensure the current page number does not exceed the total number of pages
                if current_page_number > total_pages:
                    raise Exception(
                        f"Current page {current_page_number} exceeds the total number of pages: {total_pages}")

                # 3. If we are already on the last page, exit the loop
                if current_page_number == total_pages:
                    print(f"Reached the last page: {current_page_number}.")
                    break

                # 4. Locate the "Next" button and ensure it is clickable
                next_button = self.wait.until(
                    EC.element_to_be_clickable((self.NEXT_PAGE_BUTTON))
                )

                # 5. Check if the "Next" button is enabled, allowing further navigation
                if next_button.is_enabled():
                    next_button.click()  # Click to go to the next page

                    # 6. Wait until the current page number updates, confirming that the next page has loaded
                    self.wait.until(
                        EC.text_to_be_present_in_element(
                            (self.CURRENT_PAGE_SELECTOR),
                            str(current_page_number + 1)
                        )
                    )
                else:
                    # Raise an exception if the "Next" button is disabled prematurely
                    raise Exception(
                        f"The 'Next' button is disabled at page {current_page_number}, but there are {total_pages} pages."
                    )
        except Exception as e:
            # Provide detailed error context if an issue arises during pagination
            raise Exception(f"An error occurred during pagination: {e}")

    def go_to_first_page(self):

            total_pages_element = self.driver.find_element(*self.TOTAL_PAGE_SELECTOR)
            sleep(5)
            total_pages = int(total_pages_element.text)  # Assuming it gives a number like "10"

            # Ensure we are starting from page 99
            if total_pages != 56:
                raise Exception(f"Expected to start from page 99, but found {total_pages} pages.")

            while True:
                # Get the current page number from the page (assuming it's displayed)
                current_page_element = self.driver.find_element(*self.CURRENT_PAGE_SELECTOR)
                current_page_number = int(current_page_element.text)

                # Ensure we are on a valid page (current page should not be less than 1)
                assert current_page_number >= 1, f"Current page {current_page_number} is invalid (less than 1)"

                # Check if the current page is the first page, regardless of the "Previous" button's state
                if current_page_number == 1:
                    print(f"Reached the first page: {current_page_number}.")
                    break  # Exit the loop when the first page (1) is reached

                # Check if we are on the first page (either current page == 1 or Previous button is disabled)
                try:
                    prev_button = self.driver.find_element(*self.PREV_PAGE_BUTTON)

                    # Add optional enhancement to log a warning if the Previous button is still enabled on the first page
                    if prev_button.is_enabled() and current_page_number == 1:
                        print(f"Warning: Previous button is still enabled on the first page ({current_page_number}).")
                        break

                    # Click the Previous button if it's enabled and not on the first page
                    if prev_button.is_enabled():
                        prev_button.click()
                        sleep(4)  # Wait for the page to load (adjust the sleep time if necessary)
                    else:
                        raise Exception(
                            f"Previous button is incorrectly disabled before reaching the first page at page {current_page_number}, but there are {total_pages} pages.")

                except Exception as e:
                    raise Exception(f"Error encountered during pagination: {e}")