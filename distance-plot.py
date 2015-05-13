import ephem
import datetime
import time
import os

def send2pd(message=''):
    os.system("echo '" + message + "' | pdsend 3334")  # Send to pd. Investigate sockets for better code

localtime = datetime.datetime.utcnow() # Get time, not shure it I need to

lPos = [] # Lista para guardar a position.
lDia = [] # Lista para guardar o dia.

for x in range(0, 365) :
    dia = localtime + datetime.timedelta(x,0)
    mercury = ephem.Mercury(dia)
    lPos.append(mercury.earth_distance)
    lDia.append(dia)

for item in lPos:
    print item

diaMaxI = lPos.index(max(lPos))

print("Dia de distancia maxima:{}" .format(lDia[diaMaxI]))
print "Max value element : ", max(lPos);
