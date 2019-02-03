"""This class is used as one instance of data point from either one of our sensors
or from the weather data pulled from online
"""
class DataPoint:
    def __init__(self, temp, wind, uv, rain, delta_t):
        self.temp = temp
        self.wind = wind
        self.uv = uv
        self.rain = rain
        self.delta_t = delta_t
