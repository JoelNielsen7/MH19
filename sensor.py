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

def calculate_angle(one, two):
    lat1 = one[0]
    long1 = one[1]
    lat2 = two[0]
    long2 = two[1]

    dLon = (long2 - long1)

    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

    brng = math.atan2(y, x)

    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng # count degrees clockwise - remove to make counter-clockwise

    return brng
