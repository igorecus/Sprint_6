import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.title('Проверка текста ответов в аккордеоне')
class TestMainPage:
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    @allure.description('Проверка, что при клике на вопрос отображается правильный текст ответа')
    def test_text(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)
        # Закрываем баннер cookie, если он есть
        try:
            main_page.close_cookie_banner()
        except Exception:
            pass
        # Ожидаем появления вопроса и скроллим к нему
        main_page.wait_for_element_appearance(question_locator)
        # Кликаем по вопросу
        main_page.click_on_element(question_locator)
        # Ожидаем появления ответа и получаем его текст
        main_page.wait_and_find_element(answer_locator)
        answer_text = main_page.get_element_text(answer_locator)
        assert answer_text == expected_text, f"Ожидаемый текст '{expected_text}', но получен '{answer_text}'"
