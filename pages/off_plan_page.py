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
    PRICE1_FIELD = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    PRICE2_FIELD = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    FILTER_BUTTON = (By.CSS_SELECTOR, ".filter-button.w-inline-block")
    #MOBILE_VER_FILTER_BUTTON = (By.CSS_SELECTOR, "div.filter-button")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, ".button-filter.w-button")
    PROJECTS_LISTING = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    PROJECT_NAME = (By.CSS_SELECTOR, ".project-name")
    PROJECT_IMAGE = (By.CSS_SELECTOR, ".project-image")

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

    def open_filter(self):
        self.click(*self.FILTER_BUTTON)
        # Change Locator for Mobile Version
        #self.click(*self.MOBILE_VER_FILTER_BUTTON)

    def filter_by_price(self, price1, price2):
        self.input_text(price1, *self.PRICE1_FIELD)
        self.input_text(price2, *self.PRICE2_FIELD)

    def apply_filter(self):
        self.click(*self.APPLY_FILTER_BUTTON)

    def verify_price_range(self):
        total_pages_element = self.driver.find_element(*self.TOTAL_PAGE_SELECTOR)
        sleep(3)
        total_pages = int(total_pages_element.text)  # Example: If the element text is "10"
        print(f'Total pages: {total_pages}')

        for current_page in range(1, total_pages + 1):
            print(f"Processing page {current_page}")

            # Wait for the data to load
            self.wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.price-value"))
            )

            # Process the data on the page
            projects = self.find_elements(By.CSS_SELECTOR, "div.price-value")
            for project in projects:
                price_text = project.text.replace("AED", "").replace(",", "").strip()
                if price_text.isdigit():
                    price = int(price_text)
                    assert 1200000 <= price <= 2000000, f"Product price {price} is out of range"
                else:
                    raise ValueError(f"Price text '{price_text}' is not a valid number")

            # If not the last page, navigate to the next page
            if current_page < total_pages:
                next_button = self.find_element(*self.NEXT_PAGE_BUTTON)
                # Scroll element into view for Mobile Version
                self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                # Add sleep for mobile version
                sleep(10)
                next_button.click()
                # Ensure the next page has loaded completely
                self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.price-value"))
                )

    def check_title_and_img(self):
        # To see All Listings:
        self.driver.execute_script("window.scrollBy(0, 2000)", "")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 2000)", "")


        #all_projects = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[wized='projectsListing']"))
        #                )

        all_projects = self.driver.find_elements(*self.PROJECTS_LISTING)
        print(f"Number of projects found: {len(all_projects)}")

        for project in all_projects:
            title = project.find_element(*self.PROJECT_NAME).text
            assert title, 'Product name not shown'
            print(title)
            project_img = project.find_element(*self.PROJECT_IMAGE).get_attribute('src')
            assert project_img, 'Product image not shown'








