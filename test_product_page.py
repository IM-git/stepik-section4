from pages import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    """Test a product webpage.
    Test steps:
        - Open page.
        - Click 'Add to basket' button.
        - Compare name of the books.
        - Compare cost of the books.
        """
    product_page = ProductPage(browser=browser, url=LINK)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_product_added_in_basket()
    product_page.should_be_message_cost_basket()
