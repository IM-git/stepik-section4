from pages import ProductPage
from pages import LoginPage
from pages import BasketPage

import time

import pytest

LINK_PRODUCT = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
LINK_REGISTER_PAGE = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
PASSWORD = '_vladimir_'


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = f'im{str(time.time())}@gg.com'
        login_page = LoginPage(browser=browser, url=LINK_REGISTER_PAGE)
        login_page.open()
        login_page.register_new_user(email=email, password=PASSWORD)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser) -> None:
        """Test should to fail."""
        product_page = ProductPage(browser=browser, url=LINK_PRODUCT)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser) -> None:
        """Test a product webpage."""
        product_page = ProductPage(browser=browser, url=LINK_PRODUCT)
        product_page.open()
        product_page.should_not_be_success_message()
        product_page.click_add_to_basket_button()
        product_page.should_be_message_product_added_in_basket()
        product_page.should_be_message_cost_basket()


class TestProductPage:

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser) -> None:
        """Testing that guest can to add product to the basket."""
        product_page = ProductPage(browser=browser, url=LINK_PRODUCT)
        product_page.open()
        product_page.should_not_be_success_message()
        product_page.click_add_to_basket_button()
        product_page.should_be_message_product_added_in_basket()
        product_page.should_be_message_cost_basket()

    def test_guest_cant_see_success_message(self, browser) -> None:
        """Testing that after open product page
        guest can't see the success message"""
        product_page = ProductPage(browser=browser, url=LINK_PRODUCT)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser) -> None:
        """Test should to fail.
        Can't see success message after
        adding product to the basket."""
        product_page = ProductPage(browser=browser, url=LINK_PRODUCT)
        product_page.open()
        product_page.click_add_to_basket_button()
        product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser) -> None:
        """Test should to fail.
        The message should to disappeared after
        adding product to the basket."""
        product_page = ProductPage(browser=browser, url=LINK_PRODUCT)
        product_page.open()
        product_page.click_add_to_basket_button()
        product_page.should_is_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser) -> None:
        """Check that login link on the product page is seen."""
        page = ProductPage(browser=browser, url=LINK_PRODUCT)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser) -> None:
        """Check that can to go to the login link from product page."""
        page = ProductPage(browser=browser, url=LINK_PRODUCT)
        login_page = LoginPage(browser=browser, url=LINK_PRODUCT)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser) -> None:
        """Check that can't see product in basket page,
        when open basket page from product page"""
        page = ProductPage(browser=browser, url=LINK_PRODUCT)
        basket_page = BasketPage(browser=browser, url=LINK_PRODUCT)
        page.open()
        page.go_to_basket_page()
        basket_page.should_not_be_product_in_basket_page()
        basket_page.should_be_basket_empty()
