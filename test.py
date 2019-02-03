"""Program used to test the implementation of our classes"""

import farm
from farm import Farm
import sensor
from sensor import Sensor
import score

def main():
    testfarm = Farm((0,0))
    senone = Sensor((44.790300, -92.931998))
    sentwo = Sensor((44.790300, -92.931998))
    senthree = Sensor((44.790300, -92.931998))

    testfarm.add_sensor(senone)
    testfarm.add_sensor(sentwo)
    testfarm.add_sensor(senthree)

    testfarm.pull_current()
    testfarm.pull_forecast()

    print(testfarm.future_forecast)

    #prints out some random weather data from sensors
    """
    i = 0
    while i < len(testfarm.sensors):
        print(testfarm.sensors[i].point)
        i += 1
    """

    returnlist = score.ranker(testfarm, testfarm.sensors[1])

    print(returnlist)

main()
