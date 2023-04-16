import requests
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        date = req.json()

        city = date["name"]
        cur_weather = date["main"]["temp"]
        humidity = date["main"]["pressure"]
        wind = date["wind"]["speed"]

        print(f"Погода в городе: {city}\nТемпература: {cur_weather}\nВлажность {humidity}\nВетер: {wind}")

    except Exception as ex:
        print(ex)
        print("Проверьте название города!")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()