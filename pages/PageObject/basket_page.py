from pages.PageObject.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_has_no_inner(self):# пустая или есть товары
        return self.is_not_element_present(*BasketPageLocators.BASKET_INNER)

    def basket_has_text(self):  #есть ли текст что пустая
        return self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
