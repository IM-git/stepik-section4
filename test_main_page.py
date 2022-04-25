import pytest
from pages import MainPage
from pages import LoginPage

LINK = 'http://selenium1py.pythonanywhere.com/'
# LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer'
LOGIN_LINK_ID = '#login_link'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    login_page = LoginPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page.should_be_login_page()
