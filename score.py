""" this will hopefully score the gang"""

import math
import statics




""" need to find out how to get the correct data set"""
### takes in a farm object the sensor it wants to use and then the day
def scre(farm, sensor_number, ):
    if day==0:
        data = farm.sensors[sensor_number].past[0]
    else:
        data = Farm.future_forecast[day]
    pressurelist = []
    for sens in farm.sensors:
        pressurelist.append(sens.past[0].pressure)


    tempMAG = abs(16.666-data.temp)
    pSTD = stdev(pressurelist)
    windMAG   = abs(2.7- data.wid_speed)
    cloudMAG = abs(.5-data.clouds)
