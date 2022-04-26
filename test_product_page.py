from pages import ProductPage
from pages import LoginPage
import pytest

LINK_STEP_2 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
LINK_STEP_3 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
LINK_STEP_4 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
LINK_STEP_8 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


def test_guest_can_add_product_to_basket(browser) -> None:
    """Test a product webpage."""
    product_page = ProductPage(browser=browser, url=LINK_STEP_8)
    product_page.open()
    product_page.should_not_be_success_message()
    product_page.click_add_to_basket_button()
    product_page.should_be_message_product_added_in_basket()
    product_page.should_be_message_cost_basket()


def test_guest_cant_see_success_message(browser) -> None:
    """Test should to fail."""
    product_page = ProductPage(browser=browser, url=LINK_STEP_8)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser) -> None:
    """Test should to fail.
    Can't see success message after
    adding product to the basket."""
    product_page = ProductPage(browser=browser, url=LINK_STEP_8)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser) -> None:
    """Test should to fail.
    The message should to disappeared after
    adding product to the basket."""
    product_page = ProductPage(browser=browser, url=LINK_STEP_8)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.should_is_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser) -> None:
    """Check that login link on the product page is seen."""
    page = ProductPage(browser=browser, url=LINK_STEP_8)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser) -> None:
    """Check that can to go to the login link from product page."""
    page = ProductPage(browser=browser, url=LINK_STEP_8)
    login_page = LoginPage(browser=browser, url=LINK_STEP_8)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page.should_be_login_page()
