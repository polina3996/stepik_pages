from pages.PageObject.basket_page import BasketPage
from pages.PageObject.main_page import MainPage
from pages.PageObject.login_page import LoginPage
import pytest

# ОСНОВНАЯ ЛОГИКА ТЕСТОВ ДЛЯ ГЛАВНОЙ СТР
link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        # login_page = page.go_to_login_page()  # 1 способ:выполняем метод страницы — переходим на страницу логина и сохраняем возвращаемый объект стр в переменную
        page.go_to_login_page()  # 2 способ:
        login_page = LoginPage(browser, browser.current_url)  # 2 способ:Инициализируем LoginPage в теле теста
        login_page.should_be_login_page()  # 1 и 2 способ:проверка, что стр есть


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.basket_has_no_inner(), 'Basket is not empty'
    assert basket_page.basket_has_text(), 'There is no text that basket is empty'
