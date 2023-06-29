from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class BasePage:  # базовая страница=1 класс, от кот наследуются остальные классы - КЛАСС ДЛЯ НАСТРОЙКИ ОКРУЖЕНИЯ, ПОЛУЧЕНИЯ ССЫЛКИ И ОБРАБОТК ИСКЛЮЧ
    def __init__(self, browser, url, timeout=10):  # вспомог методы для работы с драйвером
        self.browser = browser  # !!!экземпляр браузера передаем
        self.url = url  # ссылка
        self.browser.implicitly_wait(timeout)  # команду для неявного ожидания со значением по умолчанию в 10

    def open(self):  # открытие стр в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what):  # в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):  # получение проверочного кода,высчитывание ответа, вписывание ответа в алерт
        alert = self.browser.switch_to.alert  # переключение на алерт
        x = alert.text.split(" ")[2]  # число из алерт(3 элемент-число)
        answer = str(math.log(abs((12 * math.sin(float(x))))))  # вычисление ответа по формуле
        alert.send_keys(answer)  # вписываем ответ в алерт
        alert.accept()  # окей
        try:
            time.sleep(2)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
