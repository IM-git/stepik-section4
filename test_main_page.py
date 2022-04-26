from pages import MainPage
from pages import LoginPage
from pages import BasketPage

LINK = 'http://selenium1py.pythonanywhere.com/'


class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser) -> None:
        """Check that can to go to the login page from main page"""
        page = MainPage(browser=browser, url=LINK)
        login_page = LoginPage(browser=browser, url=LINK)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser) -> None:
        """Check that can see the link to login page on main page"""
        page = MainPage(browser=browser, url=LINK)
        page.open()
        page.should_be_login_link()


class TestBasketFromMainPage:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser) -> None:
        """Check that can to go to the basket page from main page"""
        page = MainPage(browser=browser, url=LINK)
        basket_page = BasketPage(browser=browser, url=LINK)
        page.open()
        page.go_to_basket_page()
        basket_page.should_not_be_product_in_basket_page()
        basket_page.should_be_basket_empty()
