class BasePage:  #базовая страница=1 класс, от кот наследуются остальные классы
    def __init__(self, browser, url): #вспомог методы для работы с драйвером
        self.browser = browser #!!!экземпляр браузера передаем
        self.url = url  #ссылка

    def open(self):  #открытие стр в браузере
        self.browser.get(self.url)
