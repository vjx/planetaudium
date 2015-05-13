import ephem
import datetime
import time
import sys

planetaSet = sys.argv[1] # Get planet name

user_input = sys.argv[2] # Get date string

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

horaMaxI = lPos.index(max(lPos))

print("{} hora de distancia maxima:{}" .format(planetaSet, lhora[horaMaxI]))
print "Max value element : ", max(lPos);
