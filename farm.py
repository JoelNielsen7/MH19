"""This class is used to represent one instance of a farm. Each farm can contain
many sensor objects that each have their own list of data points. In addition,
each farm has a list of past, current, and future global data pulled from a
weather API"""

#test coordinates: 44.790300, -92.931998

import weather
from weather import DataPoint
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
        today = weather.get_weather(self.coords[0], self.coords[1])

#pulls (randomized) data into each sensor object based on current weather
    def pull_current(self):
        i = 0
        while i < len(self.sensors):
            self.sensors[i].get_current()
            self.sensors[i].randomize()
            i += 1

#fills future_forecast with forecasted weather
    def pull_forecast(self):
        self.future_forecast = weather.get_forecast(self.coords[0], self.coords[1])

    def get_time(self, idx):
        if idx == 0:
            return 0
        else:
            return self.future_forecast[idx - 1].time - today.time / (8.64 * (10 ** 7))
