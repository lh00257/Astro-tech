import pylab as plt
import numpy as np

data = np.loadtxt('stars.dat')

x = [i[0] for i in data]
y = [i[1] for i in data]

plt.scatter(x, y, s=30, alpha=0.75)
plt.xlabel("Temperature")
plt.ylabel("Magnitude")

plt.show()

plt.savefig("HRdiag.png")
