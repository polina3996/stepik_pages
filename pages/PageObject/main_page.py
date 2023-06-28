from pages.PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage): #наследуется от базового класса - КЛАСС ДЛЯ КЛИКАНИЙ И МЕЛКИХ ФРОНТЕНД ДЕЙСТВИЙ
    def should_be_login_link(self): #проверка наличия ссылки на лог-ин(вызов метода из баз класса, чтобы обработать исключение и сделать осмысленный вывод)
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
    def go_to_login_page(self): #переход на логин-стр
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link") #поиск кнопки перехода на логин
        login_link.click() #кликаем


#Это хорошая практика: писать сначала красные тесты и только потом делать их зелеными.