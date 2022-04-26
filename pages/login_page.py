from .base_page import BasePage
from .locators import LoginPageLocators

LOGIN_PAGE_LINK = '/accounts/login/'
EXCEPTION_REGISTER_FORM = "Register form doesn't displayed"
EXCEPTION_LOGIN_FORM = "Login form doesn't displayed"


class LoginPage(BasePage):
    """The login page"""

    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email: str, password: str) -> None:
        """Performs register new user"""
        email_input = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(
            *LoginPageLocators.REPEAT_REGISTER_PASSWORD_INPUT)
        repeat_password_input.clear()
        repeat_password_input.send_keys(password)
        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_url(self):
        """Check login url"""
        current_url = self.browser.current_url
        assert LOGIN_PAGE_LINK in current_url,\
            f"Part of the link doesn't match." \
            f"Expected the part link {LOGIN_PAGE_LINK}" \
            f"is contained in {current_url}"

    def should_be_login_form(self):
        """Check login form"""
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form is True, EXCEPTION_LOGIN_FORM

    def should_be_register_form(self):
        """Check register form"""
        register_form = self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM)
        assert register_form is True, EXCEPTION_REGISTER_FORM
