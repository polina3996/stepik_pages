from PageObject.pages.base_page import BasePage
from PageObject.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_has_no_inner(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_INNER), 'Basket is not empty'

    def basket_has_text(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_TEXT), 'There is no text that basket is empty'
