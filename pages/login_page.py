from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Screen."""

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self):
        self.navigate_to(Config.BASE_URL)
        return self

    def enter_username(self, username: str):
        self.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        self.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Helper flow to perform complete login in one step."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
