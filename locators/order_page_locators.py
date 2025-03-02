from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Поля на первой странице заказа
    FIRST_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_STATION = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_STATION_SOKOLNIKI = [By.XPATH, "//button[@value='4']"]
    METRO_STATION_KRASNOSELSKAYA = [By.XPATH, "//button[@value='5']"]
    PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[contains(text(), 'Далее')]"]

    # Поля на второй странице заказа
    DELIVERY_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    CALENDAR = [By.XPATH, "//div[@class='react-datepicker__month-container']"]
    RENTAL_PERIOD = [By.XPATH, "//div[contains(text(), '* Срок аренды')]"]
    RENTAL_DAYS = [By.XPATH, "//div[contains(text(), 'семеро суток')]"]
    SCOOTER_COLOR = [By.XPATH, "//input[@id='black']"]
    COMMENT_FOR_THE_COURIER = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    # Кнопка "Заказать"
    ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"]

    # Элементы всплывающего окна
    ORDER_WINDOW = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    YES_BUTTON = [By.XPATH, "//button[text()='Да']"]
    SUCCESSFUL_ORDER = [By.XPATH, "//div[text()='Заказ оформлен']"]
    BUTTON_WATCH_STATUS = [By.XPATH, "//button[text()='Посмотреть статус']"]

    # URL формы заказа
    ORDER_FORM_URL = 'https://qa-scooter.praktikum-services.ru/order'

    # Локатор кнопки закрытия баннера cookie
    COOKIE_CLOSE_BUTTON = [By.XPATH, "//button[contains(text(), 'да все привыкли')]"]
