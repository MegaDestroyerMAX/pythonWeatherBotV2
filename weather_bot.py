import requests
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("qq")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        date = r.json()

        city = date["name"]
        cur_weather = date["main"]["temp"]
        humidity = date["main"]["pressure"]
        wind = date["wind"]["speed"]

        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_weather}\nВлажность {humidity} мм рт. ст.\nВетер: {wind} м/c")

    except:
        await message.reply("Проверьте название города!")


if __name__ == '__main__':
    executor.start_polling(dp)