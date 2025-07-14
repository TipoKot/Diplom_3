import allure
from data import BASE_URL, test_user
from pages.main_page import MainPageStellarBurgers
from pages.login_page import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMainFeatures:
    # переход по клику на «Конструктор»,
    @allure.feature("Клик по кнопке «Конструктор»")
    def test_click_constructor_button(self, driver):
        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.click_feed_button()  # сначала кликаем на Ленту заказов, чтобы убедиться, что мы на главной странице
        main_page.click_constructor_button()

        # проверяем, что URL содержит /constructor
        assert f"{BASE_URL}" in main_page.get_current_url, "Не удалось перейти в раздел 'Конструктор'"

    # переход по клику на «Лента заказов»
    @allure.feature("Клик по кнопке «Лента заказов»")
    def test_click_feed_button(self, driver):
        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.click_feed_button()

        # проверяем, что URL содержит /feed
        assert f"{BASE_URL}/feed" in main_page.get_current_url, "Не удалось перейти в раздел 'Лента заказов'"

    # если кликнуть на ингредиент, появится всплывающее окно с деталями
    @allure.feature("Клик по ингредиенту")
    def test_click_ingredient(self, driver):
        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.click_bulka_1()  # кликаем на булку
        assert EC.visibility_of_element_located(main_page.INGREDIENT_POPUP), "Всплывающее окно с деталями ингредиента не появилось"
    
    # всплывающее окно закрывается кликом по крестику
    @allure.feature("Закрытие всплывающего окна")
    def test_close_ingredient_popup(self, driver):
        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.click_bulka_1()
        main_page.close_ingredient_popup()
        assert EC.invisibility_of_element_located(main_page.INGREDIENT_POPUP), "Всплывающее окно с деталями ингредиента не закрылось"

    # при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
    @allure.feature("Добавление ингредиента в заказ")
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.add_ingredient_to_order(main_page.BULKA_1)

        counter = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(main_page.BULKA_1_COUNTER)
        )
        assert counter.text == "2", f"Ожидалось значение каунтера '2', но получили '{counter.text}'"

    # залогиненный пользователь может оформить заказ
    @allure.title("Оформление заказа залогиненным пользователем")
    def test_order_as_logged_in_user(self, driver):
        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])

        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.add_ingredient_to_order(main_page.BULKA_1)
        main_page.click_submit_order()

        assert EC.visibility_of_element_located(main_page.ORDER_POPUP), "Окно подтверждения заказа не появилось"