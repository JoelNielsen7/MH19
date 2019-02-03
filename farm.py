"""This class is used to represent one instance of a farm. Each farm can contain
many sensor objects that each have their own list of data points. In addition,
each farm has a list of past, current, and future global data pulled from a
weather API"""

class Farm:
    sensors = []
    global_past = []
    future_forecast = []


#not sure if we actually need anything in the constructor
    def __init__(self):
        x=0

#add a sensor to the list
    def add_sensor(self, sensor):
        sensors.add(sensor)

#pull a group of 
    def pull_global(self):
