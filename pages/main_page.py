from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "a[href*='/settings'].menu-button-block")

    def click_settings_button(self):
        self.click(*self.SETTINGS_BUTTON)