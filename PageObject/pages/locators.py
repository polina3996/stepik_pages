from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, '//span[@class="btn-group"]/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    REPEAT_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION = (By.XPATH, '(//button)[4]')


class ProductPageLocators:
    BOOK_NAME = (By.TAG_NAME, 'h1')
    BOOK_PRICE = (By.XPATH, '//p[@class="price_color"]')
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_BOOK = (By.XPATH, '(//div[@class ="alertinner "]/strong)[1]')
    BASKET_PRICE = (By.XPATH, '(//div[@class="alertinner "]/p/strong)[1]')
    SUCCESS_MESSAGE = (By.XPATH, '(//div[@class ="alertinner "])[1]')


class BasketPageLocators:
    BASKET_INNER = (By.ID, 'basket_formset')
    BASKET_TEXT = (By.XPATH, '//p')
