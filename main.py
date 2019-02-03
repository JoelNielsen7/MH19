"""Program used to test the implementation of our classes"""

import weather
from weather import DataPoint
from sensor import Sensor
from farm import Farm

def main():
    dp0 = weather.get_weather(15.0, 12.0)
    print(dp0)
    fc = weather.get_forecast(66.0, 14.0)
    print(fc[0])

    dp1 = DataPoint(19, 2, 90, 1.5, .4, 6,5)
    dp2 = DataPoint(25, 10, 257, 2.4, .1, 9,5)

    s1 = Sensor((20.0,50.0))
    s1.update(dp1)
    s1.update(dp2)

    s1.add_water((47.0,88.0))
    print(s1.water_angles)

    f1 = Farm((0.0,90.0))
    f1.add_sensor(s1)

    score(f1, 0, s1.past[0])

if __name__ == "__main__":
    main()
