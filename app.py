import requests
import os
import json

from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

def get_weather(city):
    apiKey = os.getenv("api_token")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"

    response = requests.get(url).json()

    weather = response["weather"][0]["main"]
    temp = round(response["main"]["temp"] - 273)

    return weather, temp

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def submit():
    city = request.form['inputText']

    try:
        weather, temp = get_weather(city)
        return render_template("weather.html", city=city, weather=weather, temp=temp)
    except Exception as e:
        return render_template("except.html", error=str(e))

app.run(debug=True)