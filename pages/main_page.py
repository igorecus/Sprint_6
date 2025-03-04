import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Инициализация и переход на главную страницу')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(MainPageLocators.BASE_URL)

    @allure.step("Прокрутка страницы, ожидание элемента и скролл к нему")
    def wait_for_element_appearance(self, locator):
        """Прокручивает страницу до конца, затем ожидает появления элемента и скроллит его в видимую область."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step("Получение текста элемента")
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Закрыть баннер cookie')
    def close_cookie_banner(self):
        self.click(MainPageLocators.COOKIE_CLOSE_BUTTON)

    @allure.step('Нажать на кнопку "Заказать" в футере')
    def click_order_button_1(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать на кнопку "Заказать" над разделом "Вопросы о важном"')
    def click_order_button_2(self):
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SAMOKAT_LOGO)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)