from pages.PageObject.main_page import MainPage
from login_page import LoginPage

#ОСНОВНАЯ ЛОГИКА ТЕСТОВ
link =  "http://selenium1py.pythonanywhere.com/"
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    #login_page = page.go_to_login_page()  # 1 способ:выполняем метод страницы — переходим на страницу логина и сохраняем возвращаемый объект стр в переменную
    page.go_to_login_page() #2 способ:
    login_page = LoginPage(browser, browser.current_url) #2 способ:Инициализируем LoginPage в теле теста
    login_page.should_be_login_page() #1 и 2 способ:проверка, что стр есть

