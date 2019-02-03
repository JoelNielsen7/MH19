""" this will hopefully score the gang"""

import math
import statistics
from sensor import calculate_angle




""" need to find out how to get the correct data set"""
### takes in a farm object the sensor it wants to use and then the day
def score(farm, data, sensor):
    #pressurelist=[]
    #for sens in farm.sensors:
    #    pressurelist.append(sens.past[0].pressure)

    deltaT = calc_dT(data.temp, data.humidity, data.pressure)
    DT_VAL = norm(deltaT, 15)

    tempMAG = abs(16.666-data.temp)
    TEMP_VAL = norm(tempMAG, 20)

    #pSTD = statistics.stdev(pressurelist)
    #pSTD_VAL = norm(pSTD, 50)

    windMAG   = abs(2.7- data.wind_speed)
    wing_VAL = norm(windMAG, 10)

    cloudMAG = abs(.5-data.clouds)
    cloud_VAL = norm(cloudMAG, .5)

    rainAM = data.rain
    rain_VAL = norm(rainAM, 150)

    deltaA_VAL = 0
    pSTD_VAL = 0
    """
    angle = sensor.water_angles[0] #TODO
    deltaA = angle - data.wind_dir
    if deltaA < 0:
        deltaA = abs(deltaA)
    if deltaA > 180:
        deltaA = 360 - deltaA

    deltaA_VAL = norm(deltaA, 180)
    """
    score = cloud_VAL+wing_VAL+DT_VAL+pSTD_VAL+TEMP_VAL+deltaA_VAL

    return(score)

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




# will take in a value normalize it from 0-1 wit the max beign well the max....
def norm(val, max):
    if val>max:
        normal = 1
    else:
        normal = val/max

    return(normal)


def ranker(farm, sensor):
    scorelistOG = []

    scorelistOG.append(score(farm, sensor.point, sensor))

    for datapoint in farm.future_forecast:
        scorelistOG.append(score(farm, datapoint, sensor))

    print(scorelistOG)
    
    timecounter = .00
    scorelist = []
    for x in scorelistOG:
        cor = x * timecounter
        val = x - cor
        scorelist.append(val)
        timecounter+=.05/8
    return(scorelist)


def maxfinder(scorelist):
    max = max(list)
    distance = list.index(max)
    return(distance)
