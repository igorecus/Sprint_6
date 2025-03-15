import allure
import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data.order_page_data import test_cases
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators


@allure.feature("Заказ самоката")
class TestOrdering:
    @allure.step("Тест процесса заказа через верхнюю кнопку")
    @pytest.mark.parametrize("data_set", [test_cases[0][1]], ids=["Order via TOP button"])
    def test_order_flow_top_button(self, driver, data_set):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_order_button_1()

        order_page = OrderPage(driver)
        order_page.wait_for_page_load()
        order_page.fill_order_form(data_set)
        order_page.submit_order()

        success = order_page.wait_for_element(OrderPageLocators.SUCCESSFUL_ORDER)
        actual_text = success.text.strip()
        assert actual_text.startswith("Заказ оформлен"), \
            f"Заголовок успешного заказа не соответствует ожидаемому. Фактический текст: '{actual_text}'"

    @allure.step("Тест процесса заказа через нижнюю кнопку")
    @pytest.mark.parametrize("data_set", [test_cases[1][1]], ids=["Order via BOTTOM button"])
    def test_order_flow_bottom_button(self, driver, data_set):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_order_button_2()

        order_page = OrderPage(driver)
        order_page.wait_for_page_load()
        order_page.fill_order_form(data_set)
        order_page.submit_order()

        success = order_page.wait_for_element(OrderPageLocators.SUCCESSFUL_ORDER)
        actual_text = success.text.strip()
        assert actual_text.startswith("Заказ оформлен"), \
            f"Заголовок успешного заказа не соответствует ожидаемому. Фактический текст: '{actual_text}'"