from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    #LOGIN_NAME = (By.NAME, "login-username")
    #LOGIN_PASSWORD = (By.NAME, "login-password")
    #LOGIN_SUBMIT = (By.NAME, "login-submit")
    #REGISTRATION_EMAIL = (By.NAME, "registration-email")
    #REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    #REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    #REGISTRATION_SUBMIT = (By.NAME, "registration-submit")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")