from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "a[href*='/settings'].menu-button-block")
    SECONDARY_BUTTON = (By.CSS_SELECTOR, "#w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b")

    def click_settings_button(self):
        self.click(*self.SETTINGS_BUTTON)

    def click_secondary_deals_button(self):
        self.click(*self.SECONDARY_BUTTON)
