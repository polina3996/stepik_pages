from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import math
import time

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:  # базовая страница=1 класс, от кот наследуются остальные классы - КЛАСС ДЛЯ НАСТРОЙКИ ОКРУЖЕНИЯ, ПОЛУЧЕНИЯ ССЫЛКИ И ОБРАБОТК ИСКЛЮЧ
    def __init__(self, browser, url, timeout=10):  # вспомог методы для работы с драйвером
        self.browser = browser  # !!!экземпляр браузера передаем
        self.url = url  # ссылка
        self.browser.implicitly_wait(timeout)  # команду для неявного ожидания со значением по умолчанию в 10

    def open(self):  # открытие стр в браузере
        self.browser.get(self.url)

    def is_element_present(self, how,
                           what):  # в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
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

    # 1. Элемент потенциально может появиться на странице (но вообще-то не должен). Например, мы открываем страницу
    # товара, и ожидаем, что там нет сообщения об успешном добавлении в корзину. Мы проверяем, что элемента нет, но при
    # позитивном сценарии, когда мы добавляем товар в корзину, сообщение тоже появляется не сразу. Если при негативной
    # проверке мы не добавим ожидание, а сразу выдадим результат: "True, элемента действительно нет, все хорошо",
    # мы рискуем нарваться на ложно-зеленый тест. То есть, можем пропустить баг.
    # Абстрактный метод, который проверяет, что элемент НЕ появляется на странице в течение заданного времени
    # (явное ожидание!):
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))  # ждет появления
        except TimeoutException:
            return True  # НЕ появился(время вышло)
        return False  # все-таки появился(основной результат)

    # 2. Элемент присутствует на странице и должен исчезнуть со временем или в результате действий пользователя.
    # Это может быть, например, удаление товара из корзины, или исчезновение лоадера с загрузкой.
    # Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с
    # функцией until_not, в зависимости от того, какой результат мы ожидаем:
    def is_disappeared(self, how, what, timeout=4):  # ждем исчезновения элемента(сначала он присутствует)
        try:
            WebDriverWait(self.browser, timeout, 1, ignored_exceptions=[TimeoutException]).until_not(
                EC.presence_of_element_located((how, what)))  # ждет, пока не исчезнет
        except TimeoutException:
            return False  # все еще присутстсвует, а время вышло
        return True  # исчез

# Поэтому на каждый негативный тест обязательно должен приходиться положительный тест. В одном тесте проверяем, что
# элемента нет, в соседнем тесте, что элемент есть. Тогда мы сможем отслеживать актуальность селектора и не пропустим
# такой баг.
