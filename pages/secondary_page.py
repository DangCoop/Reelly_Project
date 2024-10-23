from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class SecondaryPage(Page):

    def go_to_final_page(self):

        # Find the total number of pages (assuming it is displayed somewhere on the page)
        total_pages_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='totalPageProperties']")
        total_pages = int(total_pages_element.text)  # Assuming it gives a number like "10"

        while True:
            # Get the current page number from the page (assuming it's displayed)
            current_page_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='currentPageProperties']")
            current_page_number = int(current_page_element.text)

            # Ensure we are on the correct page
            assert current_page_number <= total_pages, f"Current page {current_page_number} exceeds total pages {total_pages}"

            # Check if the current page is the last page, regardless of the "Next" button's state
            if current_page_number == total_pages:
                print(f"Reached the last page: {current_page_number}.")
                break  # Exit the loop when the last page (99) is reached

            # Check if we are on the last page (either current page == total pages or Next button is disabled)
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")

                # Add optional enhancement to log a warning if the Next button is still enabled on the last page
                if next_button.is_enabled() and current_page_number == total_pages:
                    print(f"Warning: Next button is still enabled on the last page ({current_page_number}).")
                    break

                # Click the Next button if it's enabled and not on the last page
                if next_button.is_enabled():
                    next_button.click()
                    sleep(4)
                else:
                    raise Exception(
                        f"Next button is incorrectly disabled before reaching the last page at page {current_page_number}, but there are {total_pages} pages.")

            except Exception as e:
                raise Exception(f"Error encountered during pagination: {e}")

        # Option 1: Simple way to check the pagination option - but it's not working (create a bug report AIC-234)
        # next_button = self.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")
        # while next_button.is_enabled():
        #     next_button.click()
        #     # Re-check for the next button in case of dynamic loading
        #     next_button = self.driver.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")

    def back_to_first_page(self):
        # Find the total number of pages (assuming it is displayed somewhere on the page)
        total_pages_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='totalPageProperties']")
        total_pages = int(total_pages_element.text)  # Assuming it gives a number like "10"

        # Ensure we are starting from page 99
        if total_pages != 99:
            raise Exception(f"Expected to start from page 99, but found {total_pages} pages.")

        while True:
            # Get the current page number from the page (assuming it's displayed)
            current_page_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='currentPageProperties']")
            current_page_number = int(current_page_element.text)

            # Ensure we are on a valid page (current page should not be less than 1)
            assert current_page_number >= 1, f"Current page {current_page_number} is invalid (less than 1)"

            # Check if the current page is the first page, regardless of the "Previous" button's state
            if current_page_number == 1:
                print(f"Reached the first page: {current_page_number}.")
                break  # Exit the loop when the first page (1) is reached

            # Check if we are on the first page (either current page == 1 or Previous button is disabled)
            try:
                prev_button = self.driver.find_element(By.CSS_SELECTOR, "[wized='previousPageMLS']")

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
