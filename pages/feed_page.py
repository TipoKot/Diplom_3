import allure
from data import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Feed(BasePage):
    ORDER_CARD = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    ORDER_POPUP = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4")
    ORDER_COUNTER = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")
    TODAY_ORDER_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROGRESS = (By.XPATH, "//p[text()='В работе']")

    @allure.step("Открываем страницу Ленты заказов")
    def open(self):
        self.driver.get(f"{BASE_URL}/feed")

    @allure.step("Кликаем по карточке заказа")
    def click_order_card(self):
        self.click_element(self.ORDER_CARD)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ORDER_POPUP)
        )

    @allure.step("Ищем заказ по ID")
    def find_order_by_id(self, order_id):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ORDER_CARD)
        )
        orders = self.driver.find_elements(*self.ORDER_CARD)
        for order in orders:
            if order_id in order.text:
                return order
        return None
    
    @allure.step("Получаем значение счётчика выполненных заказов")
    def get_counter_value(self) -> int:
        counter_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ORDER_COUNTER)
        )
        text = counter_elem.text
        return int(text)
    
    @allure.step("Получаем значение счётчика выполненных заказов за сегодня")
    def get_today_counter_value(self) -> int:
        today_counter_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TODAY_ORDER_COUNTER)
        )
        text = today_counter_elem.text
        return int(text)
    
    @allure.step("Проверяем, что заказ в работе")
    def is_order_in_progress(self, order_id):
        orders = self.driver.find_elements(*self.ORDER_IN_PROGRESS)
        for order in orders:
            if order_id in order.text:
                return True
        return False