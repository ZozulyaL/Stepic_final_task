from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_baskket_page(self):
        self.should_be_login_url()
            
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "'basket' not in current url"
        
        
    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def guest_can_see_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)