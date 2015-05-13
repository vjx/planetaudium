import ephem
import datetime
import time

localtime = datetime.datetime.utcnow() # Get time, not shure it I need to

lPos = [] # Lista para guardar a position.
lDia = [] # Lista para guardar o dia.

for x in range(0, 365) :
    dia = localtime + datetime.timedelta(x,0)
    marte = ephem.Mars(dia)
    lPos.append(marte.earth_distance)
    lDia.append(dia)

diaMinI = lPos.index(min(lPos))

print("Marte Dia de distancia minima:{}" .format(lDia[diaMinI]))
print "Min value element : ", min(lPos);
