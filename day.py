"""This class is used to represent one instance of a sensor. It contains
a list of 5 DataPoint objects that represent the most recent 5 points collected
by the sensor
"""


class Sensor:
    past = [None]*5
    def __init__(self, point):
        self.past[0] = point

    def update(self, point):
        self[4] = self[3]
        self[3] = self[2]
        self[2] = self[1]
        self[1] = self[0]
        self[0] = point
