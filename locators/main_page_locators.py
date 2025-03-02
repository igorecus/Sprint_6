from selenium.webdriver.common.by import By

class MainPageLocators:
    # Стартовая страница тестового стенда
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    # Страница с формой заказа
    ORDER_FORM_URL = 'https://qa-scooter.praktikum-services.ru/order'
    # Страница Дзена
    DZEN_PAGE = 'https://dzen.ru/?yredirect=true'

    # Локаторы вопросов и ответов аккордеона
    QUESTION_1 = (By.XPATH, '(.//div[@class="accordion__button"])[1]')
    ANSWER_1 = (By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')

    QUESTION_2 = (By.XPATH, '(.//div[@class="accordion__button"])[2]')
    ANSWER_2 = (By.XPATH, './/p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]')

    QUESTION_3 = (By.XPATH, '(.//div[@class="accordion__button"])[3]')
    ANSWER_3 = (By.XPATH, './/p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]')

    QUESTION_4 = (By.XPATH, '(.//div[@class="accordion__button"])[4]')
    ANSWER_4 = (By.XPATH, './/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')

    QUESTION_5 = (By.XPATH, '(.//div[@class="accordion__button"])[5]')
    ANSWER_5 = (By.XPATH, './/p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')

    QUESTION_6 = (By.XPATH, '(.//div[@class="accordion__button"])[6]')
    ANSWER_6 = (By.XPATH, './/p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]')

    QUESTION_7 = (By.XPATH, '(.//div[@class="accordion__button"])[7]')
    ANSWER_7 = (By.XPATH, './/p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')

    QUESTION_8 = (By.XPATH, '(.//div[@class="accordion__button"])[8]')
    ANSWER_8 = (By.XPATH, './/p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]')

    # Другие локаторы
    TOP_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIE_CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")
