import allure
from data import BASE_URL
from pages.base_page import BasePage
from pages.main_page import MainPageStellarBurgers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(BasePage):
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")

    @allure.step("Открываем страницу логина")
    def open(self):
        self.open_url(f"{BASE_URL}/login")

    @allure.step("Заполняем поле email")
    def fill_email(self, email):
        self.fill_input(self.EMAIL_INPUT, email)

    @allure.step("Заполняем поле пароля")
    def fill_password(self, password):
        self.fill_input(self.PASSWORD_INPUT, password)

    @allure.step("Кликаем по кнопке 'Войти'")
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Авторируемся")
    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()

    @allure.step("Кликаем по кнопке 'Восстановить пароль'")
    def click_restore_password_button(self):
        self.click_element(self.RESTORE_PASSWORD_BUTTON)
