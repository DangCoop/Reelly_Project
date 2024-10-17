from pages.base_page import Page
from selenium.webdriver.common.by import By


class SettingsPage(Page):
    NUMBER_OF_OPTIONS = (By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
    COMPANY_CONNECT_BTN = (By.CSS_SELECTOR, "[target='_blank'].button-link-menu")

    def verify_correct_url(self, expected_url_part):
        self.verify_partial_url(expected_url_part)

    def verify_numbers_of_settings(self, number):
        self.verify_number_of_elements(number, *self.NUMBER_OF_OPTIONS)
        # number = int(number)
        # options = self.driver.find_elements(By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
        # assert len(options) == number, f'Expected {number} cells, but got {len(options)}'
        # print(options)

    def verify_button_availability(self):
        self.verify_btn_accessibility(*self.COMPANY_CONNECT_BTN)
        # button = self.driver.find_element(By.CSS_SELECTOR, "[target='_blank'].button-link-menu")
        # assert button.is_displayed(), "The 'connect the company' button is not available"



