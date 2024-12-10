from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.secondary_page import SecondaryPage
from pages.off_plan_page import OffPlanPage


class Application:
    def __init__(self, driver):

        self.page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.off_plan_page = OffPlanPage(driver)