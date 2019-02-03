"""Program used to test the implementation of our classes"""

import sys
import farm
from farm import Farm
import sensor
from sensor import Sensor
import score

def main():
    lat = float(sys.argv[1])
    lon = float(sys.argv[2])

    testfarm = Farm((lat, lon))
    senone = Sensor((44.790300, -92.931998))
    sentwo = Sensor((44.790300, -92.931998))
    senthree = Sensor((44.790300, -92.931998))

    testfarm.add_sensor(senone)
    testfarm.add_sensor(sentwo)
    testfarm.add_sensor(senthree)

    testfarm.pull_current()
    testfarm.pull_forecast()

    returnlist = score.ranker(testfarm, testfarm.sensors[1])
    print(returnlist[0])

if __name__ == '__main__':
    main()
