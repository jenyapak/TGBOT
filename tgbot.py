import requests

from aiogram import Bot, Dispatcher, executor, types

import config
API_TOKEN = config.API_TOKEN
API_OPENWEATHERMAP_TOKEN = config.API_OPENWEATHERMAP_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_function(message: types.Message):
    await message.reply("Put the city!: ")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_OPENWEATHERMAP_TOKEN}&units=metric&lang=ru')
        data = response.json()

        """ with open('file_weather.txt', 'w') as f:
            f.write(str(data)) """          #we download all data and now we will take the values through the keys!!!!

        city = data['name']    #take values!
        des = data['weather'][0]['description']
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]

        from datetime import datetime  #переводим во временные парамметры
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]) #.strtime("%H:%M")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(
            f" City: {city}\n Current temp: {temp}\n Weather: {des}\n Humidity: {humidity}\n Wind speed: {wind}\n Country code: {country}\n Sunset: {sunset}\n Sunrise: {sunrise}"
        )

    except Exception as ex:
        await message.reply("Add correct city name!: ")


if __name__== "__main__":   # name- name of the file, main - shows that the file is main!
    executor.start_polling(dp)
