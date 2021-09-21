from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage): 
    def go_to_login_page(self):
       #login_link = browser.find_element_by_css_selector("#login_link") меняем эту строку на 
       login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
       #time.sleep(10)
       login_link.click()