from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from data import BASE_URL

class MainPageStellarBurgers(BasePage):
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    BUILD_BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    BULKA_1 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a")
    BULKA_1_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class, 'counter')]")
    INGREDIENT_POPUP = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    INGREDIENT_POPUP_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    BURGER_CONSTRUCTOR_BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_POPUP = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    ORDER_POPUP_ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

    @allure.step("Открываем главную страницу")
    def open(self):
        self.open_url(f"{BASE_URL}/")

    @allure.step("Кликаем по кнопке 'Личный кабинет'")
    def click_account_button(self):
        self.click_element(self.ACCOUNT_BUTTON)

    @allure.step("Кликаем по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(self.CONSTRUCTOR_BUTTON)

    @allure.step("Кликаем по кнопке 'Лента заказов'")
    def click_feed_button(self):
        self.click_element(self.FEED_BUTTON)

    @allure.step("Кликаем по булке")
    def click_bulka_1(self):
        self.click_element(self.BULKA_1)
        self.wait_until_visible(self.INGREDIENT_POPUP)

    @allure.step("Закрываем всплывающее окно с деталями ингредиента")
    def close_ingredient_popup(self):
        self.click_element(self.INGREDIENT_POPUP_CLOSE_BUTTON)

    @allure.step("Добавляем ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient_locator):
        self.wait_until_visible(ingredient_locator)
        source = self.find(*ingredient_locator)
        target = self.find(*self.BURGER_CONSTRUCTOR_BASKET)
        self.drag_and_drop_element(source, target)

    @allure.step("Добавляем ингредиент Булка 1 в заказ")
    def add_bulka_1_to_order(self):
        self.add_ingredient_to_order(self.BULKA_1)

    @allure.step("Оформляем заказ")
    def click_submit_order(self):
        self.click_element(self.SUBMIT_ORDER_BUTTON)

    @allure.step("Получаем ID заказа из всплывающего окна")
    def get_order_id_from_popup(self):
        return self.wait_for_text_not_to_be(self.ORDER_POPUP_ORDER_ID, "9999")
    
    @allure.step("Ожидаем, что всплывающее окно с деталями заказа будет видимо")
    def wait_until_order_popup_visible(self):
        self.wait_until_visible(self.ORDER_POPUP)
        return True
