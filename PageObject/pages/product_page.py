from PageObject.pages.base_page import BasePage
from PageObject.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_is_added(self):
        assert self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text == self.product_name(), 'Product with no proper name is added'

    def price_of_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text == self.book_price(), "The price of basket doesn't corresponds to the price of a product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def message_is_deleted(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) is False, 'Message disappears'
