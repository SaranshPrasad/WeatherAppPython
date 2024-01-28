from flask import Flask, render_template, request
import datetime
import requests

day = datetime.datetime.now().strftime("%A")
date = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%b")





app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    global day, date, month
    if request.method == "POST":
        query = request.form.get("city_name").capitalize()
        apiKey = "65723339ad21eb46a9128715d989e842"
        unit = "metric"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={apiKey}&units={unit}"
        response = requests.get(url).json()
        feels_like = round(response['main']['feels_like'])
        icon = response["weather"][0]['icon']
        weather = response["weather"][0]['main']
        max_temp = round(response['main']['temp_max'])
        min_temp = round(response['main']['temp_min'])
        return render_template("index.html", day=day, month=month, date=date, city=query, temp=feels_like, weather=weather, icon=icon, max_temp=max_temp, min_temp=min_temp)


    return render_template("index.html", day=day, month=month, date=date)






