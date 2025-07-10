import allure
from pages.feed_page import Feed
from pages.login_page import Login
from pages.profile_page import ProfilePage
from pages.main_page import MainPageStellarBurgers
from selenium.webdriver.support import expected_conditions as EC
from data import test_user

class TestOrderFeed:
    # если кликнуть на заказ, откроется всплывающее окно с деталями,
    @allure.title("Проверка открытия попапа с деталями заказа")
    def test_order_feed(self, driver):
        
        feed_page = Feed(driver)
        feed_page.open()
        feed_page.click_order_card()
        assert EC.visibility_of_element_located(feed_page.ORDER_POPUP), "Всплывающее окно с деталями заказа не открылось"

    # заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
    @allure.title("Проверка наличия заказа пользователя в ленте заказов")
    def test_order_in_feed(self, driver):
        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user['email'], test_user['password'])

        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_page.go_to_order_history()
        order_id = profile_page.get_first_order_id()

        feed_page = Feed(driver)
        feed_page.open()
        assert feed_page.find_order_by_id(order_id), f"Заказ с ID {order_id} не найден в ленте заказов"

    # при создании нового заказа счётчик Выполнено за всё время увеличивается,
    @allure.title("Проверка увеличения счетчика выполненных заказов")
    def test_completed_orders_counter(self, driver):
        feed_page = Feed(driver)
        feed_page.open()
        initial_counter = feed_page.get_counter_value()

        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user['email'], test_user['password'])

        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.add_ingredient_to_order(main_page.BULKA_1)
        main_page.click_submit_order()

        feed_page = Feed(driver)
        feed_page.open()
        after_counter = feed_page.get_counter_value()
        assert after_counter > initial_counter, f"Ожидалось, что счётчик увеличится. Было: {before}, стало: {after}"

    # при создании нового заказа счётчик Выполнено за сегодня увеличивается,
    @allure.title("Проверка увеличения счетчика выполненных заказов за сегодня")
    def test_today_completed_orders_counter(self, driver):
        feed_page = Feed(driver)
        feed_page.open()
        initial_today_counter = feed_page.get_today_counter_value()

        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user['email'], test_user['password'])

        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.add_ingredient_to_order(main_page.BULKA_1)
        main_page.click_submit_order()

        feed_page = Feed(driver)
        feed_page.open()
        after_today_counter = feed_page.get_today_counter_value()
        assert after_today_counter > initial_today_counter, f"Ожидалось, что счётчик выполненных заказов за сегодня увеличится. Было: {initial_today_counter}, стало: {after_today_counter}"


    # после оформления заказа его номер появляется в разделе В работе.
    @allure.title("Проверка наличия заказа в разделе 'В работе'")
    def test_order_in_progress(self, driver):
        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user['email'], test_user['password'])

        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.add_ingredient_to_order(main_page.BULKA_1)
        main_page.click_submit_order()
        order_id = main_page.get_order_id_from_popup()

        feed_page = Feed(driver)
        feed_page.open()
        assert feed_page.find_order_by_id(order_id), f"Заказ с ID {order_id} не найден в разделе 'В работе'"

