from selenium.webdriver.common.by import By


class BasePageLocators:
    """Locators for main page."""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class BasketPageLocators:
    """Locators for basket page"""
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_PRODUCT_FORM = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_TOTALS = (By.CSS_SELECTOR, "#basket_totals")


class LoginPageLocators:
    """Locators for login page."""
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class MainPageLocators:
    """Locators for main page."""
    pass


class ProductPageLocators:
    """Locators for product page."""
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_OF_THE_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    COST_OF_THE_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    SUCCESS_MESSAGE_BOOK = (By.CSS_SELECTOR, '#messages div:nth-child(1)')
    NAME_OF_THE_BOOK_IN_ANSWER = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    COST_OF_THE_BOOK_IN_ANSWER = (By.CSS_SELECTOR, 'div.alert-info strong')
    COST_OF_THE_BOOK_IN_BASKET = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs')
