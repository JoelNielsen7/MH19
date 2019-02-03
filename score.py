""" this will hopefully score the gang"""

import math
import statics




""" need to find out how to get the correct data set"""
### takes in a farm object the sensor it wants to use and then the day
def score(farm, sensor_number, data ):
    if day==0:
        data = farm.sensors[sensor_number].past[0]
    else:
        data = Farm.future_forecast[day]
    pressurelist = []
    for sens in farm.sensors:
        pressurelist.append(sens.past[0].pressure)

    deltaT = deltaT()
    DT_VAL = norm(deltaT, 15)

    tempMAG = abs(16.666-data.temp)
    TEMP_VAL = norm(tempMAG, 20)

    pSTD = stdev(pressurelist)
    pSTD_VAL = norm(pSTD, 50)

    windMAG   = abs(2.7- data.wid_speed)
    wing_VAL = norm(windMAG, 10)

    cloudMAG = abs(.5-data.clouds)
    cloud_VAL = norm(cloudMAG, .5)


    rainAM = data.rain
    rain_VAL = norm(rainAM, 150)




# will take in a value normalize it from 0-1 wit the max beign well the max....
def norm(val, max):
    if val>max:
        normal = 1
    else:
        normal = val/max

    return(normal)
