import pytest
from pages.PageObject.basket_page import BasketPage
from pages.PageObject.product_page import ProductPage
from pages.PageObject.login_page import LoginPage
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'


# ЛОГИКА ТЕСТОВ ДЛЯ СТРАНИЦЫ ПРОДУКТА

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                       marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):  # , link):
    page = ProductPage(browser, link)
    page.open()
    book_name = page.product_name()
    book_price = page.book_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.product_is_added() == book_name  # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    assert page.price_of_basket() == book_price  # Стоимость корзины совпадает с ценой товара.


@pytest.mark.success_message
class TestSeeingSuccessMessage:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        assert page.should_not_be_success_message() is False, "Success message is not presented"  # проверка, что есть сообщение об успешном доб в корзину ПОСЛЕ ДОБАВЛЕНИЯ

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        assert page.should_not_be_success_message() is True, 'Success message appears without any success'  # проверка, что нет сообщения об успешном доб в корзину БЕЗ добавления

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.message_is_deleted()  # проверка, что сообщение исчезает после добавления в корзину


@pytest.mark.login_guest
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.basket_has_no_inner(), 'Basket is not empty'
    assert basket_page.basket_has_text(), 'There is no text that basket is empty'


class TestUserAddToBasketFromProductPage:  # для зарегистрированных
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser): #перед каждым тестом этого класса - регистрация
        self.login_page = LoginPage(browser, login_link)
        self.login_page.open()
        self.login_page.register_new_user(str(time.time()) + "@fakemail.org", "hehfdsdf123")
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        assert page.should_not_be_success_message() is True, 'Success message appears without any success'

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        book_name = page.product_name()
        book_price = page.book_price()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        assert page.product_is_added() == book_name  # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        assert page.price_of_basket() == book_price  # Стоимость корзины совпадает с ценой товара.

# общие функции -сетап и тирдаун -  для разных тестов выносятся отдельно(в фикстуру), запуск автоматически перед каждым тестом
# @pytest.mark.login
# создавать новый товар в нашем интернет-магазине перед тестом и удалять по завершении теста. К сожалению, наш интернет-
# магазин пока не имеет возможности создавать объекты по API, но в идеальном мире мы бы написали вот такой тест-класс
# class TestLoginFromProductPage:
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self): #функция, которая выполнится перед запуском каждого теста из класса, обычно туда входит подготовка данных. манипулировать браузером в сетапе и уж тем более что-то там проверять — это плохая практика, лучше так не делать без особой необходимости. Здесь этот пример исключительно в учебных целях, чтобы вы попробовали писать сетапы для тестов. В реальной жизни мы реализовали бы все эти манипуляции с помощью API или напрямую через базу данных.
#         self.product = ProductFactory(title="Best book created by robot")
#         # создаем продукта по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
