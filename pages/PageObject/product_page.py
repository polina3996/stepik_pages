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

    def should_not_be_success_message(self):  # появляется сообщение об успешном добавлении в корзину
        # true - не появился, а время вышло; false д.быть - появился(увидим сообщение ассерт)
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_is_deleted(self):  # сообщение исчезает из корзины
        # true д.быть
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Message is still there'
