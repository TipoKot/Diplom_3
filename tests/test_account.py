import allure
from pages.main_page import MainPageStellarBurgers
from pages.login_page import Login
from pages.profile_page import ProfilePage
from data import BASE_URL, test_user

class TestAccount():
    # переход по клику на «Личный кабинет»
    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_account(self, driver):
        main_page = MainPageStellarBurgers(driver)
        main_page.open()
        main_page.click_account_button()

        # проверяем, что URL содержит /account
        assert f"{BASE_URL}/login" in driver.current_url, "Не удалось перейти в раздел 'Личный кабинет'"
        
    # переход в раздел «История заказов»
    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver):
        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])

        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_page.go_to_order_history()
        assert f"{BASE_URL}/account/order-history" in driver.current_url, "Не удалось перейти в раздел 'История заказов'"

    # выход из аккаунта.
    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        login_page = Login(driver)
        login_page.open()
        login_page.login(test_user["email"], test_user["password"])

        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_page.logout()
        assert f"{BASE_URL}/login" in driver.current_url, "Не удалось выйти из аккаунта"