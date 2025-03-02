import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class MainPage:
    @allure.step('Инициализация и переход на главную страницу')
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(MainPageLocators.BASE_URL)

    @allure.step("Прокрутка страницы, ожидание элемента и скролл к нему")
    def wait_for_element_appearance(self, locator):
        """Прокручивает страницу до конца, затем ожидает появления элемента и скроллит его в видимую область."""
        # Прокручиваем страницу до конца, чтобы загрузились все элементы
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    @allure.step("Ожидание элемента и его поиск")
    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step('Закрыть баннер cookie')
    def close_cookie_banner(self):
        self.driver.find_element(*MainPageLocators.COOKIE_CLOSE_BUTTON).click()

    # Методы, необходимые для тестов в test_order_and_navigation.py:

    @allure.step('Нажать на кнопку "Заказать" в футере')
    def click_order_button_1(self):
        self.driver.find_element(*MainPageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку "Заказать" над разделом "Вопросы о важном"')
    def click_order_button_2(self):
        self.driver.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.SAMOKAT_LOGO).click()

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()
