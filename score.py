""" this will hopefully score the gang"""

import math
import statistics
from sensor import calculate_angle

""" need to find out how to get the correct data set"""
### takes in a farm object the sensor it wants to use and then the day
def score(farm, data, sensor):
    #temperature subscore
    #ideal below 30C
    tempMAG = abs(16.666-data.temp)
    TEMP_VAL = norm(tempMAG, 20)

    #wind subscore
    #ideal between 5 and 10km/h
    windMAG   = abs(2.7- data.wind_speed)
    wind_VAL = norm(windMAG, 10)

    #deltaT (evaporation rate) subscore
    #ideal between 2 and 8, not more than 10
    deltaT = calc_dT(data.temp, data.humidity, data.pressure)
    DT_VAL = norm(deltaT, 15)

    #pressure subscore
    pressurelist=[]
    for sens in farm.sensors:
        pressurelist.append(sens.point.pressure)

    pSTD_VAL = 0
    if len(pressurelist) > 1:
        pSTD = statistics.stdev(pressurelist)
        pSTD_VAL = norm(pSTD, 50)

    #rain subscore
    rainAM = data.rain
    rain_VAL = norm(rainAM, 150)

    #angle to body of water subscore
    deltaA_VAL = 0
    deltaA = 0
    if sensor.water_angle != None:
        angle = sensor.water_angle
        deltaA = angle - data.wind_dir
        if deltaA < 0:
            deltaA = abs(deltaA)
        if deltaA > 180:
            deltaA = 360 - deltaA
    deltaA= norm(deltaA, 180)
    deltaA_VAL = 1 - deltaA
    deltaA_VAL = norm(deltaA, 180)

    #values between 0-1
    subscores = [TEMP_VAL, wind_VAL, DT_VAL, pSTD_VAL, rain_VAL, deltaA_VAL]
    return subscores

def aggregateScore(farm, data, sensor):
    #return a score between 1-10

    subscores = score(farm, data, sensor)
    #weight each subscore
    #current weights are arbitrary, with a greater weight given to those
    #preferred by the GRDC Weather Essentials for Pesticide Application article
    subscores[0] *= .233    #temperature
    subscores[1] *= .233    #wind
    subscores[2] *= .233    #deltaT (evaporation factor)
    subscores[3] *= .10     #pressure
    subscores[4] *= .10     #rain
    subscores[5] *= .10     #deltaA (water body factor)

    # multiply by factor of 10/6 to scale for 6 items
    return sum(subscores) * 10 / 6

def responsetext(scorelist):
    avg = sum(scorelist) / 6

    parray = ["\n The temperature is took to keep particles together","\n The wind will help move the pesticide but not blow it away","\n The evaporation rate will increase the effectivenss of your spray ","\n There are few drafts and gusts","\n there is no rain forecasted", "\n The pesticide will not blow into any water"]
    narray = ["\n the temprature is to high","\n It is very windy", "\n"+"The evaporation rate is high","\n The pressure diffrence is high","\n it is a bit rainy","\n The wind is pointing towards a close body of water"]
    if bool:
        responsetext = "We recommend spraying because"
        neg = "\n Maybe hold off becuase"

        sortlist = scorelist
        sortlist.sort()
        top = sortlist[len(sortlist)-1]
        second = sortlist[len(sortlist)-2]

        bad = sortlist[0]

        responsetext+= parray[scorelist.index(top)]
        responsetext+= parray[scorelist.index(second)]
        responsetext+=neg
        responsetext+= narray[scorelist.index(bad)]

    return(responsetext)

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
    print(dT)
    return dT

# will take in a value normalize it from 0-1
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



    timecounter = .00
    scorelist = []
    for x in scorelistOG:
        cor = x * timecounter
        val = x - cor
        scorelist.append(val)
        timecounter+=.05/8
    return(scorelist)

# returns index of the max
def maxfinder(scorelist):
    maxbit = max(scorelist)
    distance = scorelist.index(maxbit)
    return(distance)
