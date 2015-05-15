
# find the day that a planet is the maximum distance from earth
# arguments: planetname date
# example Jupiter 2015-11-22

import ephem
import datetime
import time
import sys

planetaSet = sys.argv[1] # Get planet name, first argument

user_input = sys.argv[2] # Get date string, secound argument

year_month_day = user_input.split('-')  # Split it into [year, month, day]

year = int(year_month_day[0])
month = int(year_month_day[1])
day = int(year_month_day[2])

localtime = datetime.datetime(year, month, day)

lPos = [] # Lista para guardar a position.
lhora = [] # Lista para guardar o dia.

for x in range(0, 172800) :
    hora = localtime + datetime.timedelta(0,x)
    planeta = getattr(ephem,planetaSet)(hora)
    lPos.append(planeta.earth_distance)
    lhora.append(hora)

horaMinI = lPos.index(min(lPos))

print("{} hora de distancia minima:{}" .format(planetaSet, lhora[horaMinI]))
print "Min value element : ", min(lPos);
