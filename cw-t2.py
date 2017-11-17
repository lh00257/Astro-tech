import numpy as np
from astropy.constants import G, M_sun, au

a = 3.46 * au               #semi-maj axis in metres
e = 0.64                    #eccentricity

P = 2*np.pi*(a**(3/2)/((G*M_sun)**(1/2)))   #compute orbital period

r_p = a*(1-e)   #compute perihelion distance
r_a = a*(1+e)   #compute apohelion distance

E = -(G.cgs*M_sun.cgs)/(2*a.cgs)                #energy per unit mass
L = np.sqrt(G.cgs*M_sun.cgs*a.cgs*(1-(e**2)))     #angular momentum per unit mass

print("The orbital period is      = {:.4E}\n" .format(P))
print("The perihelion distance is = {:.4E}\n" .format(r_p))
print("The apohelion distance is  = {:.4E}\n" .format(r_a))
print("The energy per unit mass is  = {:.4E}\n" .format(E))
print("The angular momentum per unit mass is  = {:.4E}\n" .format(L))
