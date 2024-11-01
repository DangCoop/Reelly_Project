# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.google.com/')
#
# # populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Car')
#
# # wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify search results
# assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
#
# driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_final_page(self):
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
                raise Exception(f"Current page {current_page_number} exceeds the total number of pages: {total_pages}")

            # 3. If we are already on the last page, exit the loop
            if current_page_number == total_pages:
                print(f"Reached the last page: {current_page_number}.")
                break

            # 4. Locate the "Next" button and ensure it is clickable
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__button.w-inline-block"))
            )

            # 5. Check if the "Next" button is enabled, allowing further navigation
            if next_button.is_enabled():
                next_button.click()  # Click to go to the next page

                # 6. Wait until the current page number updates, confirming that the next page has loaded
                WebDriverWait(self.driver, 10).until(
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