Pesto-Mode 2k19

Table Number: 33

Group Members: Joel Nielsen, Callen Shutts, Jack Troshinsky, Alex Zhu,
Dominic Voto

What is it?
Pesto-Mode is a web application that advises a farmer when the ideal time to spray
their pesticides is. This is accomplished by placing IoT based sensors into the
field that communicate live weather data. It also pulls online weather data to
help make it's decisions.


How does it make its decisions?
Pesto-Mode takes in a wide variety of factors when calculating the "score" for
spraying pesticides on a certain day.

  1.  Wind speed: during the day, the ideal wind speed is between 5 and 15 km/h.
  If it's too windy the pesticides will spread too much resulting in less effective
  application and more environmental damage. If the wind speed is too small, the
  pesticides will not get distributed enough.

  2.  Wind direction: our web interface allows users to mark bodies of water that
  are nearby their farm. The model will then give a lower score if the wind is
  blowing in a similar direction as the water. This is to help prevent leaking of
  pesticides into the local ecosystem.

  3.  Temperature: based on our research, in most cases lower temperatures are
  ideal for pesticide application. As temperature rises, droplets evaporate faster
  and air becomes more turbulent resulting in less effective application. Therefore,
  our model prefers lower temperatures, with a temperature of roughly 60 degrees
  Fahrenheit being ideal.

  4.  Delta-T Value: the delta-t value represents the rate of evaporation of liquid.
  While we cannot directly measure this, it can be calculated using temperature,
  humidity, and pressure. A delta-t value between 2 and 12 is preferred with numbers
  near 2 being ideal.

  5.  Pressure differences throughout the field: a similar pressure across the
  farmer's entire field indicate ideal conditions for spraying. This is because
  pressure gradients throughout the field will results in unstable surface
  conditions and volatility of particle movement. Therefore, if a field has multiple
  sensors in it (which we envision most will), we check that the pressures at the
  various sensors are similar.

  6.  Rain: rain occurring soon after pesticide application is not ideal for many
  reasons. Firstly, this decreases the effectiveness of the application as many of
  the pesticides will be washed away. Secondly, as a consequence of this wash-away,
  the local ecosystem will be flooded with pesticides that are harmful to plants
  and animals. Therefore, our model looks to avoid rain in the days following
  pesticide application.

How to run?
Pesto-mode can be run through main.py. (ADD MORE HERE)

Sources:
https://grdc.com.au/__data/assets/pdf_file/0024/248181/GRDC-Weather-Essentials-for-Pesticide-Application-2017.pdf
