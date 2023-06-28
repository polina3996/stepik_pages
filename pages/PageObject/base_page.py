from selenium.common.exceptions import NoSuchElementException

class BasePage:  #базовая страница=1 класс, от кот наследуются остальные классы - КЛАСС ДЛЯ НАСТРОЙКИ ОКРУЖЕНИЯ, ПОЛУЧЕНИЯ ССЫЛКИ И ОБРАБОТК ИСКЛЮЧ
    def __init__(self, browser, url, timeout=10): #вспомог методы для работы с драйвером
        self.browser = browser #!!!экземпляр браузера передаем
        self.url = url  #ссылка
        self.browser.implicitly_wait(timeout) #команду для неявного ожидания со значением по умолчанию в 10

    def open(self):  #открытие стр в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what): #в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True