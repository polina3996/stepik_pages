import pytest

from pages.PageObject.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link2 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


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


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.should_not_be_success_message() is False, "Success message is not presented"  # проверка, что нет сообщения об успешном доб в корзину ПОСЛЕ ДОБАВЛЕНИЯ


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.should_not_be_success_message() is True, 'Success message appears without any success'  # проверка, что нет сообщения об успешном доб в корзину БЕЗ добавления


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_is_deleted()  # проверка, что сообщение исчезает после добавления в корзину


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()
