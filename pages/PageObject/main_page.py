from pages.PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage): #наследуется от базового класса
    def go_to_login_page(self): #переход на логин-стр
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link") #поиск кнопки перехода на логин
        login_link.click() #кликаем