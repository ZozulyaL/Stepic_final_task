from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
#from pages.basket_page import BasketPage
import time
import math
import pytest

@pytest.mark.parametrize('promo', [ "?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail) , "?promo=offer8", "?promo=offer9",  ])
#@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{promo}"
    link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    #time.sleep(1)
    #page.guest_can_see_product_name()
    #time.sleep(2)
    #page.product_price_is_correct()


