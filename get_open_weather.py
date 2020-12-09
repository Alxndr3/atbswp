#!/usr/bin/env python3
# get_open_wether.py - Prints the weather for a location from a commanda line.


import json
from os import environ
import pprint
import requests
import sys


APPID = environ.get("OPEN_WEATHER_ID")

# Compute location from comand line arguments.
if len(sys.argv) < 2:
    print('Usage: get_open_weather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
# URL for day weather
# url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APPID}'

# URL for 5 day / 3 hour
url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&APPID={APPID}'

response = requests.get(url)
response.raise_for_status()

# Uncoment to see the raw JSON text.
# print(response.text)

# Load JSON data into a Python variable 
weather_data = json.loads(response.text)

# Print weather descriptions.
# c = weather_data['name']
# m = weather_data['main']
#pprint.pprint(c)

w = weather_data['list'] # pprint.pprint(w[0])
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], end='\n\n')
print('Temperature:')
print(round(int(w[0]['main']['temp']) - 273.15, 2), end='\n\n')
print('Feels like:')
print(round(int(w[0]['main']['feels_like']) - 273.15, 2), end='\n\n')

print('Tomorrow')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'], end='\n\n')
print('Temperature:')
print(round(int(w[1]['main']['temp']) - 273.15, 2), end='\n\n')
print('Feels like:')
print(round(int(w[1]['main']['feels_like']) - 273.15, 2), end='\n\n')


print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'], end='\n\n')
print('Temperature:')
print(round(int(w[2]['main']['temp']) - 273.15, 2), end='\n\n')
print('Feels like:')
print(round(int(w[2]['main']['feels_like']) - 273.15, 2), end='\n\n')
