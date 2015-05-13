import ephem
import datetime
import time
import sys

planetaSet = sys.argv[1] # Get firts attribute from command line

localtime = datetime.datetime.utcnow() # Get time, not shure it I need to use datetime

lPos = [] # Lista para guardar a position.
lDia = [] # Lista para guardar o dia.

for x in range(0, 365) :
    dia = localtime + datetime.timedelta(x,0)
    planeta = getattr(ephem,planetaSet)(dia)
    lPos.append(planeta.earth_distance)
    lDia.append(dia)

diaMaxI = lPos.index(max(lPos))

print("{} Dia de distancia maxima:{}" .format(planetaSet, lDia[diaMaxI]))
print "Max value element : ", max(lPos);
