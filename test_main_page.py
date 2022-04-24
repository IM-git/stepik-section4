import pytest

LINK = 'http://selenium1py.pythonanywhere.com/'
LOGIN_LINK_ID = '#login_link'


def test_guest_can_go_to_login_page(browser):
    browser.get(LINK)
    login_link = browser.find_element_by_css_selector(LOGIN_LINK_ID)
    login_link.click()
