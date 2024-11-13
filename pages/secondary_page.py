from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SecondaryPage(Page):
    FILTERS_BUTTON = (By.CSS_SELECTOR, ".filter-button")
    WANT_TO_SELL_OPTION = (By.CSS_SELECTOR, "[wized='ListingTypeSell']")
    WANT_TO_BUY_OPTION = (By.CSS_SELECTOR, "[wized='ListingTypeBuy']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    LISTING_CARDS =(By.CSS_SELECTOR, ".listing-card")
    SALE_TAG = (By.CSS_SELECTOR, ".for-sale-block")
    BUY_TAG = (By.CSS_SELECTOR, ".for-sale-block")
    PRICE1_FIELD = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    PRICE2_FIELD = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    AED_PRICE = (By.CSS_SELECTOR, "div.number-price-text")


    def go_to_final_page(self):

        # # Find the total number of pages (assuming it is displayed somewhere on the page)
        # total_pages_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='totalPageProperties']")
        # total_pages = int(total_pages_element.text)  # Assuming it gives a number like "10"
        #
        # while True:
        #     # Get the current page number from the page (assuming it's displayed)
        #     current_page_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='currentPageProperties']")
        #     current_page_number = int(current_page_element.text)
        #
        #     # Ensure we are on the correct page
        #     #assert current_page_number <= total_pages, f"Current page {current_page_number} exceeds total pages {total_pages}"
        #
        #     # Check if the current page is the last page, regardless of the "Next" button's state
        #     if current_page_number == total_pages:
        #         print(f"Reached the last page: {current_page_number}.")
        #         break  # Exit the loop when the last page (99) is reached
        #
        #     # Check if we are on the last page (either current page == total pages or Next button is disabled)
        #     try:
        #         next_button = self.driver.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")
        #
        #         # Add optional enhancement to log a warning if the Next button is still enabled on the last page
        #         if next_button.is_enabled() and current_page_number == total_pages:
        #             print(f"Warning: Next button is still enabled on the last page ({current_page_number}).")
        #             break
        #
        #         # Click the Next button if it's enabled and not on the last page
        #         if next_button.is_enabled():
        #             next_button.click()
        #             sleep(4)
        #         else:
        #             raise Exception(
        #                 f"Next button is incorrectly disabled before reaching the last page at page {current_page_number}, but there are {total_pages} pages.")
        #
        #     except Exception as e:
        #         raise Exception(f"Error encountered during pagination: {e}")

        #Option 1: Simple way to check the pagination option - but it's not working (create a bug report AIC-234)
        # next_button = self.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")
        # while next_button.is_enabled():
        #     next_button.click()
        #     # Re-check for the next button in case of dynamic loading
        #     next_button = self.driver.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")
    # Option 3 Rakhib
        try:
            # Retrieve the total number of pages from the web page
            total_pages_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='totalPageProperties']")
            total_pages = int(total_pages_element.text)  # Example: If the element text is "10"

            # Continuously navigate through pages until reaching the last one
            while True:
                # 1. Retrieve the current page number from the page
                current_page_element = self.driver.find_element(By.CSS_SELECTOR, "[wized='currentPageProperties']")
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
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__button.w-inline-block"))
                )

                # 5. Check if the "Next" button is enabled, allowing further navigation
                if next_button.is_enabled():
                    next_button.click()  # Click to go to the next page

                    # 6. Wait until the current page number updates, confirming that the next page has loaded
                    self.wait.until(
                        EC.text_to_be_present_in_element(
                            (By.CSS_SELECTOR, "[wized='currentPageProperties']"),
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

    def click_filters_button(self):
        self.click(*self.FILTERS_BUTTON)

    def choose_want_to_sell_option(self):
        self.click(*self.WANT_TO_SELL_OPTION)
        #sleep(8)

    def choose_want_to_buy_option(self):
        self.click(*self.WANT_TO_BUY_OPTION)

    def click_apply_filter_button(self):
        self.click(*self.APPLY_FILTER_BUTTON)
        #sleep(8)

    # Option 1: Verifying without iteration.
    # def verify_sell_filter_works(self):
    #
    #     #all_cards = self.driver.find_elements(*self.LISTING_CARDS)
    #     all_cards = self.wait.until(
    #         EC.visibility_of_all_elements_located(self.LISTING_CARDS)
    #     )
    #
    #     for card in all_cards:
    #         tag = card.find_element(*self.SALE_TAG).text
    #         assert tag, 'Card tag is not shown'
    #         print(tag)

    # Option 2: Verifying with iteration.
    def verify_sell_filter_works(self):
        # Start from page 1
        page_count = 1

        while True:
            print(f"Checking page {page_count}...")

            # Wait until all listing cards are visible on the current page
            all_cards = self.wait.until(
                EC.visibility_of_all_elements_located(self.LISTING_CARDS)
            )

            # Verify each card has the "for sale" tag
            for card in all_cards:
                tag = card.find_element(*self.SALE_TAG).text
                assert tag, 'Card tag is not shown'
                print(tag)

            # Check if the "Next" button is present and clickable
            try:
                next_button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__button.w-inline-block"))
                )

                # Check if the "Next" button is enabled; if not, we are on the last page
                if not next_button.is_enabled():
                    print("Reached the last page; no more pages to navigate.")
                    # Exit the loop if the "Next" button is disabled
                    break

                # Click the "Next" button to go to the next page
                next_button.click()
                page_count += 1

                # Wait for the page number or content to update (optional)
                self.wait.until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[wized='currentPageProperties']"), str(page_count))
                )

            except:
                print("No more pages available or 'Next' button is not clickable.")
                # Exit the loop if there are no more pages
                break

    def verify_buy_filter_works(self):

        # Start from page 1
        page_count = 1

        while True:
            print(f"Checking page {page_count}...")

            # Wait until all listing cards are visible on the current page
            all_cards = self.wait.until(
                EC.visibility_of_all_elements_located(self.LISTING_CARDS)
            )

            # Verify each card has the "for sale" tag
            for card in all_cards:
                tag = card.find_element(*self.BUY_TAG).text
                assert tag, 'Card tag is not shown'
                print(tag)

            # Check if the "Next" button is present and clickable
            try:
                next_button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__button.w-inline-block"))
                )

                # Check if the "Next" button is enabled; if not, we are on the last page
                if not next_button.is_enabled():
                    print("Reached the last page; no more pages to navigate.")
                    # Exit the loop if the "Next" button is disabled
                    break

                # Click the "Next" button to go to the next page
                next_button.click()
                page_count += 1

                # Wait for the page number or content to update (optional)
                self.wait.until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[wized='currentPageProperties']"),
                                                     str(page_count))
                )
            except:
                print("No more pages available or 'Next' button is not clickable.")
                # Exit the loop if there are no more pages
                break

    def fiter_by_price (self, price1, price2):
        self.input_text(price1,*self. PRICE1_FIELD)
        self.input_text(price2,*self.PRICE2_FIELD)
        #sleep(6)

    def verify_price_filter_works(self):
        page_count = 1

        while True:
            print(f"Checking page {page_count}...")

            # Wait until all listing cards are visible on the current page
            all_cards = self.wait.until(
                EC.visibility_of_all_elements_located(self.AED_PRICE)
            )

            for card in all_cards:
                aed_price_text = card.text.replace("AED", "").replace(",", "").strip()
                if aed_price_text.isdigit():
                    aed_price = int(aed_price_text)
                    assert 1200000 <= aed_price <= 2000000, f"Product price {aed_price} is out of range"
                    print(aed_price)
                else:
                    raise ValueError(f"Price text '{aed_price_text}' is not a valid number")

            # Check if the "Next" button is present and clickable
            try:
                next_button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__button.w-inline-block"))
                )

                # Check if the "Next" button is enabled; if not, we are on the last page
                if not next_button.is_enabled():
                    print("Reached the last page; no more pages to navigate.")
                    # Exit the loop if the "Next" button is disabled
                    break

                # Click the "Next" button to go to the next page
                next_button.click()
                page_count += 1

                # Wait for the page number or content to update (optional)
                self.wait.until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[wized='currentPageProperties']"),
                                                     str(page_count))
                )
            except:
                print("No more pages available or 'Next' button is not clickable.")
                # Exit the loop if there are no more pages
                break