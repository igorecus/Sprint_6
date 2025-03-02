class OrderPageData:
    # Данные для набора 1
    FIRST_NAME_SET_1 = 'Иван'
    LAST_NAME_SET_1 = 'Петров'
    ADDRESS_SET_1 = 'г. Петербург, ул. Ленинградская, 10'
    STATION_METRO_SET_1 = 'Сокольники'
    PHONE_NUMBER_SET_1 = '+77778885566'
    DELIVERY_DATE_SET_1 = '10.02.2025'
    COMMENT_FOR_COURIER_SET_1 = 'Привет.'

    # Данные для набора 2
    FIRST_NAME_SET_2 = 'Игорь'
    LAST_NAME_SET_2 = 'Иванов'
    ADDRESS_SET_2 = 'г. Москва, ул. Московская, 15'
    STATION_METRO_SET_2 = 'Красносельская'
    PHONE_NUMBER_SET_2 = '81113332244'
    DELIVERY_DATE_SET_2 = '10.01.2025'
    COMMENT_FOR_COURIER_SET_2 = 'Hello!'

# Набор тестовых кейсов с параметрами: точка входа и данные для формы заказа.
test_cases = [
    ("top", {
         "first_name": OrderPageData.FIRST_NAME_SET_1,
         "last_name": OrderPageData.LAST_NAME_SET_1,
         "address": OrderPageData.ADDRESS_SET_1,
         "metro_station": OrderPageData.STATION_METRO_SET_1,
         "phone": OrderPageData.PHONE_NUMBER_SET_1,
         "delivery_date": OrderPageData.DELIVERY_DATE_SET_1,
         "comment": OrderPageData.COMMENT_FOR_COURIER_SET_1,
    }),
    ("bottom", {
         "first_name": OrderPageData.FIRST_NAME_SET_2,
         "last_name": OrderPageData.LAST_NAME_SET_2,
         "address": OrderPageData.ADDRESS_SET_2,
         "metro_station": OrderPageData.STATION_METRO_SET_2,
         "phone": OrderPageData.PHONE_NUMBER_SET_2,
         "delivery_date": OrderPageData.DELIVERY_DATE_SET_2,
         "comment": OrderPageData.COMMENT_FOR_COURIER_SET_2,
    })
]
