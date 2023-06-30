import pytest

from pages.PageObject.product_page import ProductPage


# link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

# ЛОГИКА ТЕСТОВ ДЛЯ СТРАНИЦЫ ПРОДУКТА

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    book_name = page.product_name()
    book_price = page.book_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.product_is_added() == book_name  # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    assert page.price_of_basket() == book_price  # Стоимость корзины совпадает с ценой товара.
