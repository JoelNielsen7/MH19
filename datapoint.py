"""This class is used as one instance of data point from either one of our sensors
or from the weather data pulled from online
"""
class DataPoint:
    def __init__(self, time, temp, pressure, humidity, wind_speed, wind_dir, clouds, rain):
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
    
