import ephem
import datetime
import time

localtime = datetime.datetime(2015,11,20) 

lPos = [] # Lista para guardar a position.
lhora = [] # Lista para guardar o dia.

for x in range(0, 86400) :
    hora = localtime + datetime.timedelta(0,x)
    mercury = ephem.Mercury(hora)
    lPos.append(mercury.earth_distance)
    lhora.append(hora)

horaMaxI = lPos.index(max(lPos))

print("hora de distancia maxima:{}" .format(lhora[horaMaxI]))
print "Max value element : ", max(lPos);
