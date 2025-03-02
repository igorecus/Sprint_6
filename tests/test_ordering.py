import allure
import pytest
from pages.order_page import OrderPage
from data.order_page_data import test_cases
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Заказ самоката")
class TestOrdering:
    @allure.step("Тест процесса заказа")
    @pytest.mark.parametrize("entry_point, data_set", test_cases,
                             ids=["Order via TOP button", "Order via BOTTOM button"])
    def test_order_flow(self, driver, entry_point, data_set):
        # Открываем главную страницу
        driver.get("https://qa-scooter.praktikum-services.ru/")

        # Пытаемся закрыть баннер cookie, если он отображается
        try:
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(OrderPageLocators.COOKIE_CLOSE_BUTTON)
            ).click()
        except Exception:
            pass

        # Выбираем точку входа: верхняя или нижняя кнопка "Заказать"
        if entry_point == "top":
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')]"))
            ).click()
        else:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]"))
            ).click()

        # Работа с формой заказа
        order_page = OrderPage(driver)
        order_page.wait_for_page_load()
        order_page.fill_order_form(data_set)
        order_page.submit_order()

        # Проверяем, что появляется окно с надписью, начинающейся с "Заказ оформлен"
        success = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESSFUL_ORDER)
        )
        actual_text = success.text.strip()
        assert actual_text.startswith("Заказ оформлен"), \
            f"Заголовок успешного заказа не соответствует ожидаемому. Фактический текст: '{actual_text}'"
