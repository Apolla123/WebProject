# испортируем библиотеку для работы с падежами
import pymorphy2


# преобразование из иминительного падежа в падежный
def get_city(city):
    # вызываем класс pymorphy2.MorphAnalyzer()
    morph = pymorphy2.MorphAnalyzer()

    # Проводим морфологический анализ слова
    parsed_city = morph.parse(city)[0]

    # Словоизменяем слово в предложный падеж
    city_in_loct = parsed_city.inflect({"loct"})

    # выводим это слово
    return city_in_loct.word.capitalize()


# преобразование из любого падежа в иминительного
def make_city(city):
    # вызываем класс pymorphy2.MorphAnalyzer()
    morph = pymorphy2.MorphAnalyzer()

    # Проводим морфологический анализ слова
    parsed_city = morph.parse(city)[0]

    # Словоизменяем слово в иминительный падеж
    city_in_nomn = parsed_city.inflect({"nomn"})

    # выводим это слово
    return city_in_nomn.word.capitalize()
