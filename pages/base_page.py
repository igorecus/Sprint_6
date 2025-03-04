import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_timeout = 10

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.wait_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=None):
        timeout = timeout if timeout else self.wait_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.wait_for_element_clickable(locator).click()

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание определенного URL")
    def wait_for_url(self, url, timeout=None):
        timeout = timeout if timeout else self.wait_timeout
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Ожидание открытия определенного количества окон")
    def wait_for_windows_count(self, count, timeout=None):
        timeout = timeout if timeout else self.wait_timeout
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

    @allure.step("Ожидание, что URL содержит определенную строку")
    def wait_for_url_contains(self, url_part, timeout=None):
        timeout = timeout if timeout else self.wait_timeout
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))