import pylab as plt
import numpy as np
import matplotlib.cm as cm

data = np.loadtxt('galaxies.dat.gz')

c = [i[1] for i in data]
x = [i[2] for i in data]
y = [i[3] for i in data]
t=np.arange(len(x))

plt.scatter(x, y, c=t, cmap=cm.cmap_name_r)
plt.xlabel(" ")
plt.ylabel(" ")

plt.show()

#plt.savefig("HRdiag.png")
