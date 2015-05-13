import ephem
import datetime
import time
import os

def send2pd(message=''):
    os.system("echo '" + message + "' | pdsend 3333")
    
while True:

    localtime = datetime.datetime.utcnow() # Get time, not shure it I need to
    passado = localtime - datetime.timedelta(0,500) # See the past to calculate speed

    def hpos(body): return body.hlon, body.hlat 
        

    mercury = ephem.Mercury(localtime)
    mercuryp = ephem.Mercury(passado)
    
    venus = ephem.Venus(localtime)
    venusp = ephem.Venus(passado)
    
    mars = ephem.Mars(localtime)
    marsp = ephem.Mars(passado)
    
    jupiter = ephem.Jupiter(localtime)
    jupiterp = ephem.Jupiter(passado)
    

    saturn = ephem.Saturn(localtime)
    saturnp = ephem.Saturn(passado)

    uranus = ephem.Uranus(localtime)
    uranusp = ephem.Uranus(passado)

    neptune = ephem.Neptune(localtime)
    neptunep = ephem.Neptune(passado)

    pluto = ephem.Pluto(localtime)
    plutop = ephem.Pluto(passado)

    print("-----------------")
        
    print(localtime)
    print(passado)

    mercSpeed = repr(ephem.separation(hpos(mercury), hpos(mercuryp)))
    venuSpeed = repr(ephem.separation(hpos(venus), hpos(venusp)))
    marsSpeed = repr(ephem.separation(hpos(mars), hpos(marsp)))
    jupiSpeed = repr(ephem.separation(hpos(jupiter), hpos(jupiterp)))
    satuSpeed = repr(ephem.separation(hpos(saturn), hpos(saturnp)))
    uranSpeed = repr(ephem.separation(hpos(uranus), hpos(uranusp)))
    neptSpeed = repr(ephem.separation(hpos(neptune), hpos(neptunep)))
    plutSpeed = repr(ephem.separation(hpos(pluto), hpos(plutop)))
    
    send2pd("Mercurio Dist-terra {};" .format(mercury.earth_distance))
    send2pd("Mercurio Fase {};" .format(mercury.phase))
    send2pd("Mercurio Velocidade {};" .format(mercSpeed))

    send2pd("Venus Dist-terra {};" .format(venus.earth_distance))
    send2pd("Venus Fase {};" .format(venus.phase))
    send2pd("Venus Velocidade {};" .format(venuSpeed))

    send2pd("Marte Dist-terra {};" .format(mars.earth_distance))
    send2pd("Marte Fase {};" .format(mars.phase))
    send2pd("Marte Velocidade {};" .format(marsSpeed))

    send2pd("Jupiter Dist-terra {};" .format(jupiter.earth_distance))
    send2pd("Jupiter Fase {};" .format(mars.phase))
    send2pd("Jupiter Velocidade {};" .format(jupiSpeed))

    

    print("Mercurio Dist-terra:{} Fase:{} Velocidade:{}" .format(mercury.earth_distance, mercury.phase, mercSpeed))

    print("Venus Dist-terra:{} Fase:{} Velocidade:{}" .format(venus.earth_distance, venus.phase, (ephem.separation(hpos(venus), hpos(venusp)))))
    print("Marte Dist-terra:{} Fase:{} Velocidade:{}" .format(mars.earth_distance, mars.phase,  (ephem.separation(hpos(mars), hpos(marsp)))))
    print("Jupiter Dist-terra:{} Fase:{} Velocidade:{}" .format(jupiter.earth_distance, jupiter.phase,  (ephem.separation(hpos(jupiter), hpos(jupiterp)))))
    print("Saturno Dist-terra:{} Fase:{} Velocidade:{}" .format(saturn.earth_distance, saturn.phase, (ephem.separation(hpos(saturn), hpos(saturnp)))))
    print("Urano Dist-terra:{} Fase:{} Velocidade:{}" .format(uranus.earth_distance, uranus.phase, (ephem.separation(hpos(uranus), hpos(uranusp)))))
    print("Neptuno Dist-terra:{} Fase:{} Velocidade:{}" .format(neptune.earth_distance, neptune.phase, (ephem.separation(hpos(neptune), hpos(neptunep)))))
    print("Plutao Dist-terra:{} Fase:{} Velocidade:{}" .format(pluto.earth_distance, pluto.phase, (ephem.separation(hpos(pluto), hpos(plutop)))))
    
    time.sleep(1)
 

