from selenium.webdriver.common.by import By
#Когда мы выносим селекторы в отдельную сущность, мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе.

class MainPageLocators:  #теперь каждый селектор — это пара: как искать и что искать(чтобы менять селектор в 1 месте только)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")