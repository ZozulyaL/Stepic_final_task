from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import math

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()


    def guest_can_see_product_name(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is no the same"

    def product_price_is_correct(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_STORE)
        assert product_prise_in_store.text == product_price_in_basket.text, "Price is wrong"

    
    def check_message_about_adding_to_basket(self):
        basket_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_on_product_page(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"    
            
            
            
    