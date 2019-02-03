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

    print("\n\n\nRandomized Example Sensor Data")
    print("------------------------------")

    i = 0
    while i < len(testfarm.sensors):
        print("sensor " + str(i + 1))
        print(testfarm.sensors[i].point)
        i += 1

    print("\n\n\nExample Aggregate Scores")
    print("------------------------")

    box = score.score(testfarm, senone.point, senone)

    list = []
    for datapoints in testfarm.future_forecast:
        box = score.aggregateScore(testfarm, datapoints, senone)
        list.append(box)

    print(list)

main()
