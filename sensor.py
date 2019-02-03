"""This class is used to represent one instance of a sensor. It contains
a list of 5 DataPoint objects that represent the most recent 5 points collected
by the sensor
"""
import math
from datapoint import DataPoint

class Sensor:
    past = [None]*5
    water_angles = []

    def __init__(self, coords):
        self.coords = coords

    def update(self, point):
        self.past[4] = self.past[3]
        self.past[3] = self.past[2]
        self.past[2] = self.past[1]
        self.past[1] = self.past[0]
        self.past[0] = point

    def add_water(self, water_coords):
        angle = calculate_angle(self.coords, water_coords)
        self.water_angles.append(angle)


#Questionable function I found online to calculate the angle between coordinates

def calculate_angle(pointA, pointB):

    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)
    # Now we have the initial bearing but math.atan2 return values
    # from -180 to + 180 which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing
