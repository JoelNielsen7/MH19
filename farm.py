"""This class is used to represent one instance of a farm. Each farm can contain
many sensor objects that each have their own list of data points. In addition,
each farm has a list of past, current, and future global data pulled from a
weather API"""

import requests
from datapoint import DataPoint
from sensor import Sensor

class Farm:
    sensors = []
    water_coords = []
    global_past = []
    today = None
    future_forecast = []


#not sure if we actually need anything in the constructor
    def __init__(self, coords):
        self.coords = coords

#add a sensor to the list
    def add_sensor(self, sensor):
        self.sensors.append(sensor)

#add body of water point for wind direction
    def add_water(self, coords):
        self.water_coords.append(coords)

#pull a group of current and forecasted data and add them to the lists
    def pull_global(self):
        x=1

#Returns a list of forecasted datapoints for a given lat/long
def get_forecast(lat, lon):
    request_str = 'http://api.openweathermap.org/data/2.5/forecast?lat=' + str(lat) + '&lon=' + str(lon) + '&units=metric&APPID=7affa084c276e60ac6eaa71ec2e60737'
    result = requests.get(request_str).json()
    if str(result['cod']) != '200':
        print('bad response code: ' + result['cod'])
        return []

    datapoint_list = []
    for entry in result['list']:
        time = int(entry['dt'])
        temp = float(entry['main']['temp'])
        pressure = float(entry['main']['pressure'])
        humidity = int(entry['main']['humidity']) / 100
        wind_speed = float(entry['wind']['speed'])
        wind_dir = int(entry['wind']['deg'])
        clouds = int(entry['clouds']['all']) / 100

        datapoint_list.append(DataPoint(time, temp, pressure, humidity, wind_speed, wind_dir, clouds))

    return datapoint_list

#Returns current datapoint for a given lat/long
def get_weather(lat, lon):
    request_str = 'http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&units=metric&APPID=7affa084c276e60ac6eaa71ec2e60737'
    result = requests.get(request_str).json()
    if str(result['cod']) != '200':
        print('bad response code: ' + result['cod'])
        return []

    time = int(result['dt'])
    temp = float(result['main']['temp'])
    pressure = float(result['main']['pressure'])
    humidity = int(result['main']['humidity']) / 100
    wind_speed = float(result['wind']['speed'])
    wind_dir = int(result['wind']['deg'])
    clouds = int(result['clouds']['all']) / 100

    return DataPoint(time, temp, pressure, humidity, wind_speed, wind_dir, clouds)

