from pages.base_page import BasePage
from pages .main_page import MainPage
from pages.login_page import LoginPage
import time
import pytest

#def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    #page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


#def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    #page = MainPage(browser, link)
    #page.open()
    #page.should_be_login_link()
    
def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
#этот тест в классе теперь    
#def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com"
    #page = MainPage(browser, link)
    #page.open()
    #page.go_to_login_page()
    #login_page = LoginPage(browser, browser.current_url)
    #time.sleep(30)
    #login_page.should_be_login_page()
    
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.guest_cant_see_product_in_basket()
    page.guest_can_see_empty_basket()
    
    
#Давайте например объединим в группу два теста в файле test_main_page.py и пометим его меткой login_guest:

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
         # реализация теста
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        time.sleep(30)
        login_page.should_be_login_page()
        
    def test_guest_should_see_login_link(self, browser):
         # реализация теста
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

#Попробуйте запустить тесты в этом файле с меткой (нужно добавить "-m login_guest"). Вы увидите, что запустились оба теста, хотя метка всего одна. 