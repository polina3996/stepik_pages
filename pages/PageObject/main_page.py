from pages.PageObject.base_page import BasePage


class MainPage(BasePage): #наследуется от базового класса - КЛАСС ДЛЯ КЛИКАНИЙ И МЕЛКИХ ФРОНТЕНД ДЕЙСТВИЙ
    #заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)