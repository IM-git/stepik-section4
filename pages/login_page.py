from .base_page import BasePage
from .locators import LoginPageLocators

LOGIN_PAGE_LINK = '/accounts/login/'
EXCEPTION_REGISTER_FORM = "Register form doesn't displayed"
EXCEPTION_LOGIN_FORM = "Login form doesn't displayed"


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert LOGIN_PAGE_LINK in current_url,\
            f"Part of the link doesn't match." \
            f"Expected the part link {LOGIN_PAGE_LINK}" \
            f"is contained in {current_url}"

    def should_be_login_form(self):
        login_form = self.is_element_present(
            *LoginPageLocators.LOGIN_FORM)
        assert login_form is True, EXCEPTION_LOGIN_FORM

    def should_be_register_form(self):
        register_form = self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM)
        assert register_form is True, EXCEPTION_REGISTER_FORM
