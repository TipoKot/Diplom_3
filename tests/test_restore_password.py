import pytest
import allure
import random
from pages.login_page import Login
from pages.forgot_password_page import ForgotPassword
from data import BASE_URL

class TestRestorePassword:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_restore_password(self, driver):
        login_page = Login(driver)
        login_page.open()

        login_page.wait_for_overlay_to_disappear()
        login_page.click_restore_password_button()
        assert f"{BASE_URL}/forgot-password" in login_page.get_current_url, "Не удалось перейти на страницу восстановления пароля"

    # ввод почты и клик по кнопке «Восстановить»
    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_restore_password_submit(self, driver):
        forgot_password_page = ForgotPassword(driver)
        forgot_password_page.open()

        email = f"user{random.randint(1000, 9999)}@example.com"
        forgot_password_page.fill_email(email)

        forgot_password_page.click_restore_button()

        # ждем перехода на страницу сброса пароля
        forgot_password_page.wait_for_page_to_load()
        assert f"{BASE_URL}/reset-password" in forgot_password_page.get_current_url, "Не удалось перейти на страницу сброса пароля"

    # клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_toggle_password_visibility(self, driver):
        forgot_password_page = ForgotPassword(driver)
        forgot_password_page.open()

        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_page_to_load()

        forgot_password_page.click_toggle_password_visibility()
        # проверяем, что появилась обводка
        assert forgot_password_page.is_password_field_highlighted(), "Поле ввода пароля не подсветилось после клика"