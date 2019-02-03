"""This class is used as one instance of data point from either one of our sensors
or from the weather data pulled from online
"""
class DataPoint:
    def __init__(self, time, temp, pressure, humidity, wind_speed, wind_dir, clouds):
        self.time = time                # millis since epoch
        self.temp = temp                # degrees celcius
        self.pressure = pressure        # hPa AKA mb
        self.humidity = humidity        # 0 to 1
        self.wind_speed = wind_speed    # meter/sec
        self.wind_dir = wind_dir        # degrees, meteorological
        self.clouds = clouds            # 0 to 1

    
