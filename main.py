from datapoint import DataPoint
from sensor import Sensor
from farm import Farm

dp1 = DataPoint(19, 2, 1.5, .4, 6)
dp2 = DataPoint(25, 10, 2.4, .1, 9)

s1 = Sensor([4415.223,9255.432])
s1.update(dp1)
s1.update(dp2)

f1 = Farm([4412.254,9244.215])
f1.add_sensor(s1)
