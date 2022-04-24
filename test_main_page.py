import pytest
from pages import MainPage

LINK = 'http://selenium1py.pythonanywhere.com/'
LOGIN_LINK_ID = '#login_link'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()
