from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
import time


class MainPage(BasePage): 
    def go_to_login_page(self):
       #login_link = browser.find_element_by_css_selector("#login_link") меняем эту строку на 
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click()
       
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK),"Login link is not presented"