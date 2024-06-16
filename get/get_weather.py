# испортируем библиотеку для работы с запросами
import requests


# функция для получения температуры
def get_weather(city):
    # формируем запрос
    url = ('https://api.openweathermap.org/data/2.5/weather?q='
           +city+'&units=metric&lang=ru&appid=08e34e35ab68be2b75939da620c9b612')

    # отправляем запрос на сервер и сразу получаем результат
    weather_data = requests.get(url).json()

    # получаем данные о температуре
    temperature = round(weather_data['main']['temp'])

    # и о том, как она ощущается
    temperature_feel_like = round(weather_data['main']['feels_like'])

    # выводим значения
    return str(temperature), str(temperature_feel_like)
