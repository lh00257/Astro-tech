import pylab as plt
import numpy as np

data = np.loadtxt('times.dat')

plt.loglog(data[:,0], data[:,1], 'b--', label="T-orb")
plt.loglog(data[:,0], data[:,2], 'm')   #What does this mean?
plt.loglog(data[:,0], data[:,5], 'r-.')
plt.xlabel("r(pc)")
plt.ylabel("T(yr)")
plt.text(0.001, 10, "T(orb)")
plt.text(0.1, 100000000, "T(RP)")
plt.text(0.001, 1000000, "T(NP)")
plt.axvspan(0.1, 0.4, color="r", alpha=0.5)
plt.savefig('times.png')

plt.show()
