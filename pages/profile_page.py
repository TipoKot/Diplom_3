import allure
from data import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(BasePage):
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    FIRST_ORDER_CARD = (By.CSS_SELECTOR, "ul.OrderHistory_profileList__374GU li.OrderHistory_listItem__2x95r")

    @allure.step("Открываем страницу профиля")
    def open(self):
        self.driver.get(f"{BASE_URL}/account")

    @allure.step("Переходим в раздел 'История заказов'")
    def go_to_order_history(self):
        self.click_element(self.ORDER_HISTORY_BUTTON)

    @allure.step("Выходим из аккаунта")
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/login")
        )

    @allure.step("Находим и возвращаем ID заказа из ЛК")
    def get_first_order_id(self):
        first_card = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_ORDER_CARD)
        )

        order_id_element = first_card.find_element(By.CSS_SELECTOR, "p.text_type_digits-default")

        return order_id_element.text