from .base_page import BasePage
from .locators import ProductPageLocators

EXCEPTION_BUTTON = "Add to basket button is not presented"
EXCEPTION_NAME = "The name of the books doesn't match."
EXCEPTION_COST = "The cost of the books doesn't match."
EXCEPTION_SUCCESS_MESSAGE_BOOK = "Success message is presented, but should not be"


class ProductPage(BasePage):
    """The product page."""

    def click_add_to_basket_button(self) -> None:
        """Performing a click to the 'Add to basket' button"""
        self.should_not_be_success_message()
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.should_be_add_basket_button()
        add_to_basket_button.click()

    def should_be_message_product_added_in_basket(self) -> None:
        """Two name of the books on a webpage are compared.
        The names are expected to be the same."""
        expected_name = self.get_name_book()
        got_name = self.get_answer_name_book()
        self.should_be_the_same_values(expected=expected_name,
                                       got=got_name,
                                       text=EXCEPTION_NAME)

    def should_be_message_cost_basket(self) -> None:
        """Two cost of the books on a webpage are compared.
        The costs are expected to be the same."""
        expected_cost = self.get_cost_book()
        got_cost_answer = self.get_answer_cost_book()
        got_cost_basket = self.get_answer_cost_book()
        self.should_be_the_same_values(expected=expected_cost,
                                       got=got_cost_answer,
                                       text=EXCEPTION_COST)
        self.should_be_the_same_values(expected=expected_cost,
                                       got=got_cost_basket,
                                       text=EXCEPTION_COST)

    def get_name_book(self) -> str:
        """Getting name of the book in the description."""
        name_book = self.browser.find_element(
            *ProductPageLocators.NAME_OF_THE_BOOK)
        return name_book.text

    def get_cost_book(self) -> str:
        """Getting cost of the book of description."""
        cost_book = self.browser.find_element(
            *ProductPageLocators.COST_OF_THE_BOOK)
        return cost_book.text

    def get_answer_name_book(self) -> str:
        """Getting name of the book of basket."""
        name_book = self.browser.find_element(
            *ProductPageLocators.NAME_OF_THE_BOOK_IN_ANSWER)
        return name_book.text

    def get_answer_cost_book(self) -> str:
        """Getting cost of the book of basket."""
        cost_book = self.browser.find_element(
            *ProductPageLocators.COST_OF_THE_BOOK_IN_ANSWER)
        return cost_book.text

    def get_basket_cost_book(self) -> str:
        """Getting cost of the book of basket."""
        cost_book = self.browser.find_element(
            *ProductPageLocators.COST_OF_THE_BOOK_IN_BASKET)
        return cost_book.text

    def should_be_add_basket_button(self):
        """Checking add to basket button present."""
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), EXCEPTION_BUTTON

    def should_not_be_success_message(self):
        """Check the message should not be presented."""
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_BOOK),\
            EXCEPTION_SUCCESS_MESSAGE_BOOK

    @staticmethod
    def should_be_the_same_values(expected: str,
                                  got: str,
                                  text: str = "The values doesn't match."):
        """Two values are compared."""
        assert expected == got, f"{text} Expected: {expected}, got: {got}"
