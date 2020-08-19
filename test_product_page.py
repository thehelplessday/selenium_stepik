from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser,link):

    page = ProductPage(browser, link, 10)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.add_to_cart_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 10)
    page.open()
    page.add_product_to_cart()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, 10)
    page.open()
    page.go_to_login_page()