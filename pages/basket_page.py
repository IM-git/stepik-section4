from .base_page import BasePage
from .locators import BasketPageLocators

EXCEPTION_MESSAGE_NOT_PRESENT = "Basket product form is presented, but should not be"
EXCEPTION_BASKET_EMPTY = "Not found 'Basket empty' message"


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        """Check the message should not be presented."""
        assert self.is_element_present(
            *BasketPageLocators.TEXT_BASKET_EMPTY),\
            EXCEPTION_BASKET_EMPTY

    def should_not_be_product_in_basket_page(self):
        """Check the message should not be presented."""
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCT_FORM), \
            EXCEPTION_MESSAGE_NOT_PRESENT
