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

    testfarm = Farm((lat,lon ))
    senone = Sensor((44.790300, -92.931998))
    sentwo = Sensor((44.790300, -92.931998))
    senthree = Sensor((44.790300, -92.931998))

    senone.add_water((44.790302, -92.931994))
    sentwo.add_water((44.790302, -92.931994))
    senthree.add_water((44.790302, -92.931994))



    testfarm.add_sensor(senone)
    testfarm.add_sensor(sentwo)
    testfarm.add_sensor(senthree)

    testfarm.pull_current()
    testfarm.pull_forecast()


    box = score.score(testfarm, senone.point, senone)

    print(score)
    print(score.responsetext(box))

if __name__ == '__main__':
    main()

main()
