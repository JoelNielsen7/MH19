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

import math

def calc_dT(temp, humidity, pressure):
    #celsius, percentage, millibar

    dewPoint = ((humidity / 100) ** (1/8)) * (112 + 0.9 * temp) + 0.1 * temp - 112
    vapour = 6.112 * (math.e ** ((17.67 * dewPoint) / (243.5 + dewPoint)))

    tHigher = temp
    tLower = dewPoint
    wetGuess = dewPoint

    while True:
        previousGuess = wetGuess
        wetGuess = (tLower + tHigher) / 2
        if abs(previousGuess - wetGuess) < 0.005:
            break
        EwGuess = 6.112 * (math.e ** ((17.67 * wetGuess) / (243.5 + wetGuess)))
        ActVpGuess = EwGuess - (0.00066 * (1 + 0.00115 * wetGuess) * (temp - wetGuess) * pressure)
        EDelta = vapour - ActVpGuess
        if EDelta < 0:
            tHigher = wetGuess
        else:
            tLower = wetGuess

    dT = temp - wetGuess
    return dT
