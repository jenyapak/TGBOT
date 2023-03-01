import requests

API_OPENWEATHERMAP_TOKEN = "7bdc32d40763cf37f33636bd11a8286c"

city = input('Your city is: ')
try:
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_OPENWEATHERMAP_TOKEN}&units=metric&lang=ru')
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

    print(
        f" City: {city}\n Current temp: {temp}\n Weather: {des}\n Humidity: {humidity}\n Wind speed: {wind}\n Country code: {country}\n Sunset: {sunset}\n Sunrise: {sunrise}"
    )

except Exception as ex:
    print(ex)


