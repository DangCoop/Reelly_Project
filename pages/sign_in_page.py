from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASS_INPUT_FIELD = (By.CSS_SELECTOR, "#field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".login-button.w-button")

    def open_page(self):
        self.driver.get('https://soft.reelly.io/')

    def enter_email_and_pass(self, email, password):
        self.input_text(email, *self.EMAIL_INPUT_FIELD)
        self.input_text(password, *self.PASS_INPUT_FIELD)

    def click_cont_button(self):
        self.click(*self.CONTINUE_BUTTON)