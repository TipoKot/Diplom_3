import allure
from selenium.webdriver.common.by import By
from data import BASE_URL, browser_name
from pages.base_page import BasePage


class ForgotPassword(BasePage):
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    EMAIL_INPUT = (By.NAME, "name")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action")
    PASSWORD_INPUT_HIGHLIGHT = (By.CSS_SELECTOR, "div.input.input_status_active")

    @allure.step("Открываем страницу восстановления пароля")
    def open(self):
        self.driver.get(f"{BASE_URL}/forgot-password")

    @allure.step("Заполняем поле почты")
    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    @allure.step("Кликаем по кнопке 'Восстановить'")
    def click_restore_button(self):
        if browser_name == "Firefox":
            self.wait_for_overlay_to_disappear()
        else:
            self.click_element(self.RESTORE_BUTTON)

    @allure.step("Кликаем по кнопке показать/скрыть пароль")
    def click_toggle_password_visibility(self):
        self.click_element(self.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверяем, что поле с паролем подсвечено")
    def is_password_field_highlighted(self):
        field_container = self.find(self.PASSWORD_INPUT_HIGHLIGHT)
        return "input_status_active" in field_container.get_attribute("class")