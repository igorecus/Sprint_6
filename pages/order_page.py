import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_timeout = 10

    def wait_for_element(self, locator, timeout=None):
        if timeout is None:
            timeout = self.wait_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        WebDriverWait(self.driver, self.wait_timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def set_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def close_cookie_if_present(self):
        """Закрывает баннер cookie, если он отображается."""
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(OrderPageLocators.COOKIE_CLOSE_BUTTON)
            ).click()
        except TimeoutException:
            pass

    @allure.step("Ожидание загрузки страницы заказа")
    def wait_for_page_load(self):
        self.wait_for_element(OrderPageLocators.FIRST_NAME)

    @allure.step("Заполнение персональных данных (первая страница заказа)")
    def fill_personal_info(self, first_name, last_name, address, metro_station, phone):
        self.close_cookie_if_present()

        self.wait_for_element(OrderPageLocators.FIRST_NAME)
        self.set_text(OrderPageLocators.FIRST_NAME, first_name)
        self.set_text(OrderPageLocators.LAST_NAME, last_name)
        self.set_text(OrderPageLocators.ADDRESS, address)

        # Открываем выпадающий список станций
        self.click(OrderPageLocators.METRO_STATION)
        self.set_text(OrderPageLocators.METRO_STATION, metro_station)
        if metro_station.strip().lower() == "сокольники":
            self.click(OrderPageLocators.METRO_STATION_SOKOLNIKI)
        elif metro_station.strip().lower() == "красносельская":
            self.click(OrderPageLocators.METRO_STATION_KRASNOSELSKAYA)
        else:
            dynamic_locator = (
                OrderPageLocators.METRO_STATION[0],
                f"//button[normalize-space(text())='{metro_station}']"
            )
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(dynamic_locator)
            )
            self.click(dynamic_locator)

        self.set_text(OrderPageLocators.PHONE, phone)
        self.close_cookie_if_present()
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение данных заказа (вторая страница)")
    def fill_order_info(self, delivery_date, comment):
        self.close_cookie_if_present()

        self.wait_for_element(OrderPageLocators.DELIVERY_DATE)
        self.set_text(OrderPageLocators.DELIVERY_DATE, delivery_date)
        # Отправляем клавишу ENTER для закрытия календаря
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE).send_keys(Keys.ENTER)
        # Ждем, пока календарь (элемент с классом react-datepicker__current-month) исчезнет
        from selenium.webdriver.common.by import By
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker__current-month"))
        )

        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.click(OrderPageLocators.RENTAL_DAYS)
        self.click(OrderPageLocators.SCOOTER_COLOR)
        self.set_text(OrderPageLocators.COMMENT_FOR_THE_COURIER, comment)
        self.close_cookie_if_present()
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Заполнение формы заказа")
    def fill_order_form(self, data_set: dict):
        self.fill_personal_info(
            data_set["first_name"],
            data_set["last_name"],
            data_set["address"],
            data_set["metro_station"],
            data_set["phone"]
        )
        self.fill_order_info(
            data_set["delivery_date"],
            data_set["comment"]
        )

    @allure.step("Подтверждение заказа")
    def submit_order(self):
        self.wait_for_element(OrderPageLocators.ORDER_WINDOW)
        self.click(OrderPageLocators.YES_BUTTON)
        self.wait_for_element(OrderPageLocators.SUCCESSFUL_ORDER)
        status_text = self.wait_for_element(OrderPageLocators.BUTTON_WATCH_STATUS).text
        return status_text
