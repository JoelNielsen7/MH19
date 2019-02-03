"""Contains methods to retrieve current and future weather data for a given location"""

import requests

# Stores a snapshot of current weather conditions
class DataPoint:
    def __init__(self, time, temp, pressure, humidity, wind_speed, wind_dir, clouds, rain=0):
        self.time = time                # millis since epoch
        self.temp = temp                # degrees celcius
        self.pressure = pressure        # hPa AKA mb
        self.humidity = humidity        # 0 to 1
        self.wind_speed = wind_speed    # meter/sec
        self.wind_dir = wind_dir        # degrees, meteorological
        self.clouds = clouds            # 0 to 1
        self.rain = rain                # mm for the past 3 hours

    def __str__(self):
        return "{time=%d; temp=%f; pressure=%f; humidity=%f; wind_speed=%f; wind_dir=%d; clouds=%f; rain=%d}" % (self.time, self.temp, self.pressure, self.humidity, self.wind_speed, self.wind_dir, self.clouds, self.rain)

#Returns current datapoint for the given lat/long
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
    if 'rain' in result:
        rain = int(result['rain']['3h'])
    else:
        rain = 0;

    return DataPoint(time, temp, pressure, humidity, wind_speed, wind_dir, clouds, rain)


#Returns a list of forecasted datapoints for the given lat/long
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
        rain = 0;
        if 'rain' in entry:
            if '3h' in entry['rain']:
                rain = int(entry['rain']['3h'])

        datapoint_list.append(DataPoint(time, temp, pressure, humidity, wind_speed, wind_dir, clouds, rain))

    return datapoint_list
