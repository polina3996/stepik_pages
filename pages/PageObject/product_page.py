from pages.PageObject.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def product_name(self):  # имя товара вначале
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def book_price(self):  # цена вначале
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def add_to_basket(self):  # метод добавления в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    # методы проверки
    def product_is_added(self):  # Сообщение о том, что товар добавлен в корзину.
        return self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text

    def price_of_basket(self):  # Сообщение со стоимостью корзины.
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
