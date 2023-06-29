from pages.PageObject.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


# ЛОГИКА ТЕСТОВ ДЛЯ СТРАНИЦЫ ПРОДУКТА

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    book_title = page.product_name()
    book_price = page.book_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.product_is_added() == book_title  #Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    assert page.price_of_basket() == book_price #Стоимость корзины совпадает с ценой товара.
