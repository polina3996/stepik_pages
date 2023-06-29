from pages.PageObject.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage): #наследуется от базового класса - КЛАСС ДЛЯ КЛИКАНИЙ И МЕЛКИХ ФРОНТЕНД ДЕЙСТВИЙ
    def should_be_login_link(self): #проверка наличия ссылки на лог-ин(вызов метода из баз класса, чтобы обработать исключение и сделать осмысленный вывод)
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" #берем из класса локаторов его атрибут(кортеж, распаковывается)
    def go_to_login_page(self): #переход на логин-стр
        self.is_element_present(*MainPageLocators.LOGIN_LINK).click() #берем из класса локаторов его атрибут(кортеж, распаковывается)


#Это хорошая практика: писать сначала красные тесты и только потом делать их зелеными.