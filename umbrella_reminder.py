#!/usr/bin/env python3
# umbrela_reminder.py - Sends an SMS message if it's going to rain.


from os import environ
import json
import pprint
import requests
import text_myself


APPID = environ.get("OPEN_WEATHER_ID")

location = 'curitiba'

# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&APPID={APPID}'

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable 
weather_data = json.loads(response.text)

w = weather_data['list']

message = f"""Don\'t forget your umbrela.
        the weather for today:
        {w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description']}'
        'Temperature:'
        {round(int(w[0]['main']['temp']) - 273.15, 2)}'
        'Feels like:'
        {round(int(w[0]['main']['feels_like']) - 273.15, 2)}"""

print(message)
if str(w[0]['weather'][0]['main']).lower() == "rain":
    text_myself.text_myself(message)

