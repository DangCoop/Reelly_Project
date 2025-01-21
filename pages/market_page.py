from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class MarketPage(Page):
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, ".pagination__button.w-inline-block")
    PREVIOUS_PAGE_BUTTON = (By.CSS_SELECTOR, "div.pagination__button")
    TOTAL_PAGE_COUNT = (By.CSS_SELECTOR, "[wized='totalPageMarket']")
    CURRENT_PAGE_COUNT = (By.CSS_SELECTOR, "[wized='currentPageMarket']")

    def verify_market_page(self):
        expected_url = "https://soft.reelly.io/market-companies"
        current_url = self.driver.current_url
        assert expected_url == current_url, f"Expected URL '{expected_url}', but got '{current_url}'"

    def go_to_final_page(self):
        while True:
            try:
                # Retrieve the total number of pages
                total_pages_element = self.driver.find_element(*self.TOTAL_PAGE_COUNT)
                total_pages = int(total_pages_element.text)

                # Retrieve the current page number
                current_page_element = self.driver.find_element(*self.CURRENT_PAGE_COUNT)
                current_page = int(current_page_element.text)

                print(f"Current page: {current_page}, Total pages: {total_pages}")

                # Stop if we have reached the last page
                if current_page == total_pages:
                    print(f"Reached the last page: {current_page}.")
                    break

                # Locate the Next button
                next_button = self.wait.until(
                    EC.element_to_be_clickable(self.NEXT_PAGE_BUTTON)
                )

                # Check if the Next button is interactable
                if next_button.is_enabled():
                    next_button.click()
                    print(f"Clicked Next button to go to page {current_page + 1}.")

                    # Wait for the page number to update
                    self.wait.until(
                        EC.text_to_be_present_in_element(self.CURRENT_PAGE_COUNT, str(current_page + 1))
                    )
                else:
                    print(
                        f"Warning: Next button is still enabled but no more pages to navigate (current page: {current_page}).")
                    break

            except Exception as e:
                print(f"Pagination error: {e}")
                break

    def go_to_first_page(self):
        while True:
            try:
                # Retrieve the current page number
                current_page_element = self.driver.find_element(*self.CURRENT_PAGE_COUNT)
                current_page = int(current_page_element.text)

                print(f"Current page: {current_page}")

                # Stop if we have reached the first page
                if current_page == 1:
                    print("Reached the first page.")
                    break

                # Locate the Previous button
                prev_button = self.wait.until(
                    EC.element_to_be_clickable(self.PREVIOUS_PAGE_BUTTON)
                )

                # Check if the Previous button is interactable
                if prev_button.is_enabled():
                    prev_button.click()
                    print(f"Clicked Previous button to go to page {current_page - 1}.")

                    # Wait for the page number to update
                    self.wait.until(
                        EC.text_to_be_present_in_element(self.CURRENT_PAGE_COUNT, str(current_page - 1))
                    )
                else:
                    print(
                        f"Warning: Previous button is still enabled but no more pages to navigate (current page: {current_page}).")
                    break

            except Exception as e:
                print(f"Pagination error while navigating back: {e}")
                break





