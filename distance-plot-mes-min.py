import ephem
import datetime
import time
import sys

planetaSet = sys.argv[1] # Get firts attribute from command line

localtime = datetime.datetime.utcnow() # Get time, not shure it I need to use datetime

lPos = [] # Lista para guardar a position.
lDia = [] # Lista para guardar o dia.

for x in range(0, 730) :
    dia = localtime + datetime.timedelta(x,0)
    planeta = getattr(ephem,planetaSet)(dia)
    lPos.append(planeta.earth_distance)
    lDia.append(dia)

diaMinI = lPos.index(min(lPos))

print("{} Dia de distancia minima:{}" .format(planetaSet, lDia[diaMinI]))
print "Min value element : ", min(lPos);
