"""This class is used to represent one instance of a sensor. It contains
a list of 5 DataPoint objects that represent the most recent 5 points collected
by the sensor
"""

from datapoint import DataPoint

class Sensor:
    past = [None]*5

    def __init__(self, coords):
        self.coords = coords

    def update(self, point):
        self.past[4] = self.past[3]
        self.past[3] = self.past[2]
        self.past[2] = self.past[1]
        self.past[1] = self.past[0]
        self.past[0] = point
