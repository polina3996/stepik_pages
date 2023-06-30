from pages.PageObject.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage # 1 способ: импорт страницы с логином

class MainPage(BasePage): #наследуется от базового класса - КЛАСС ДЛЯ КЛИКАНИЙ И МЕЛКИХ ФРОНТЕНД ДЕЙСТВИЙ
    #заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)