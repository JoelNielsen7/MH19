"""Program used to test the implementation of our classes"""

from datapoint import DataPoint
from sensor import Sensor
from farm import Farm

dp1 = DataPoint(19, 2, 90, 1.5, .4, 6)
dp2 = DataPoint(25, 10, 257, 2.4, .1, 9)

s1 = Sensor([45.0,90])
s1.update(dp1)
s1.update(dp2)

s1.add_water([90,90])
print(s1.water_angles)


f1 = Farm([0,90])
f1.add_sensor(s1)
