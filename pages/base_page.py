from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators

EXCEPTION_LOGIN_LINK = "Login link is not presented"
EXCEPTION_BASKET_LINK = "Basket link is not presented"
EXCEPTION_AUTHORIZED_USER = "User icon is not presented, probably unauthorised user"


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        """Performing open the page"""
        self.browser.get(url=self.url)

    def is_element_present(self, how, what) -> bool:
        """Checking that element is present"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        """Checking that element doesn't present."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4) -> bool:
        """Wait while element is disappeared.
        If it doesn't happen after 'timeout' time,
        will be sent False"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self) -> None:
        """Performing a click for go to the login page"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        """Performing a click for go to the basket page"""
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_authorized_user(self):
        """Checking the authorized user"""
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
            EXCEPTION_AUTHORIZED_USER

    def should_be_login_link(self):
        """Check that the login link is present"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
            EXCEPTION_LOGIN_LINK

    def should_be_basket_link(self):
        """Checking that the login link is present"""
        assert self.is_element_present(*BasePageLocators.BASKET_LINK),\
            EXCEPTION_BASKET_LINK
