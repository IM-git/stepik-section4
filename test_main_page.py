import pytest
from pages import MainPage
from pages import LoginPage

LINK = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser) -> None:
    page = MainPage(browser=browser, url=LINK)
    login_page = LoginPage(browser=browser, url=LINK)   # use browser.current_url without LINK
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page.should_be_login_page()
