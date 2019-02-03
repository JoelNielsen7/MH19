""" this will hopefully score the gang"""

import math
import statistics
from sensor import calculate_angle




""" need to find out how to get the correct data set"""
### takes in a farm object the sensor it wants to use and then the day
def score(scorelist):
    avg = svg(scorelist)

    parray = ["\n The temperature is took to keep particles together","\n The wind will help move the pesticide but not blow it away","\n The evaporation rate will increase the effectivenss of your spray ","\n There are few drafts and gusts","\n there is no rain forecasted", "\n The pesticide will not blow into any water"]
    narray = ["\n the temprature is to high","\n It is very windy", "\n"+"The evaporation rate is high","\n The pressure diffrence is high","\n it is a bit raint","\n The wind is pointing towards a close body of water",]
    temp wind dt pressure rain da
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
