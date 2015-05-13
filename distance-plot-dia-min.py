import ephem
import datetime
import time

localtime = datetime.datetime(2015,05,31) 

lPos = [] # Lista para guardar a position.
lhora = [] # Lista para guardar o dia.

for x in range(0, 86400) :
    hora = localtime + datetime.timedelta(0,x)
    mercury = ephem.Mercury(hora)
    lPos.append(mercury.earth_distance)
    lhora.append(hora)


horaMinI = lPos.index(min(lPos))

print("hora de distancia minima:{}" .format(lhora[horaMinI]))
print "Min value element : ", min(lPos);
