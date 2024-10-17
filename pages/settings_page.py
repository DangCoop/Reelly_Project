from pages.base_page import Page
from selenium.webdriver.common.by import By


class SettingsPage(Page):


    def verify_url(self, expected_url="https://soft.reelly.io/settings"):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected url {expected_url} did not match actual {actual_url}'

    def verify_numbers_of_settings(self, number):
        number = int(number)
        options = self.driver.find_elements(By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
        assert len(options) == number, f'Expected {number} cells, but got {len(options)}'
        print(options)

    def verify_button_availability(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "[target='_blank'].button-link-menu")
        assert button.is_displayed(), "The 'connect the company' button is not available"



