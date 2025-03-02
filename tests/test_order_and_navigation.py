import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from conftest import driver

@allure.title('Проверка кнопок заказа и навигации по логотипам')
class TestOrderAndNavigation:

    @allure.description('Проверяем, что при клике на верхнюю кнопку "Заказать" открывается форма заказа самоката')
    def test_top_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_1()
        WebDriverWait(driver, 5).until(EC.url_to_be(MainPageLocators.ORDER_FORM_URL))
        assert driver.current_url == MainPageLocators.ORDER_FORM_URL, (
            f"Ожидался URL формы заказа: {MainPageLocators.ORDER_FORM_URL}, получен: {driver.current_url}"
        )

    @allure.description('Проверяем, что при клике на нижнюю кнопку "Заказать" открывается форма заказа самоката')
    def test_bottom_order_button(self, driver):
        main_page = MainPage(driver)
        # Закрываем баннер cookie перед кликом
        main_page.close_cookie_banner()
        main_page.click_order_button_2()
        WebDriverWait(driver, 5).until(EC.url_to_be(MainPageLocators.ORDER_FORM_URL))
        assert driver.current_url == MainPageLocators.ORDER_FORM_URL, (
            f"Ожидался URL формы заказа: {MainPageLocators.ORDER_FORM_URL}, получен: {driver.current_url}"
        )

    @allure.description('Проверяем, что при клике на логотип "Самокат" происходит переход на главную страницу Самоката')
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        driver.get(MainPageLocators.ORDER_FORM_URL)
        main_page.click_scooter_logo()
        WebDriverWait(driver, 5).until(EC.url_to_be(MainPageLocators.BASE_URL))
        assert driver.current_url == MainPageLocators.BASE_URL, (
            f"Ожидался URL главной страницы: {MainPageLocators.BASE_URL}, получен: {driver.current_url}"
        )

    @allure.description('Проверяем, что при клике на логотип "Яндекс" открывается главная страница Дзена в новом окне')
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        new_window = [handle for handle in driver.window_handles if handle != original_window][0]
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 5).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url, (
            f"Ожидался URL страницы Дзена, содержащий 'dzen.ru', получен: {driver.current_url}"
        )
        driver.close()
        driver.switch_to.window(original_window)
