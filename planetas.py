import ephem

mars = ephem.Mars()
mars.compute()
print mars.ra, mars.dec
