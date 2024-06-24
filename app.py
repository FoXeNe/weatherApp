import requests
import os
import json

from flask import Flask, render_template, request
from dotenv import load_dotenv

try:
    app = Flask(__name__)

    load_dotenv()

    def get_weather(a):
        # водим апи ключ
        apiKey = os.getenv("api_token")
        # принимает переменную и кладет ее в city
        city = a

        # делаем запрос по этому юрл
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"

        # ответ с юрл
        response = requests.get(url).json()
        pretty_response = json.dumps(response, indent=4)
        print(pretty_response) 

        # беру первый элемент из weather в response
        weather = response["weather"][0]["main"]

        # беру инфомацию из response и перевожу ее из кельвина в цельсия отнимая 273
        temp = round(response["main"]["temp"] - 273)

        return weather, temp


    @app.route('/')
    def index():
        # выводит index.html пользователю
        return render_template("index.html")

    @app.route('/', methods=['POST'])
    def submit():
        # принимает текст который ввел пользователь из index.html
        city = request.form['inputText']
        weather, temp = get_weather(city)
        # вывожу weather.html задавая переменные которые находятся в weather.html
        return render_template("weather.html", city = city, weather = weather, temp = temp)


    app.run(debug= True)
except:
    pass

