import numpy as np      #Import relevant packages for computation
import pylab as plt

a = np.linspace(0,20,50)    #Define array from 0 - 20 with 50 spaces

def bes(n,x):
    if n == 0:      #For the J0 Bessel function
        b_0 = [(np.sin(x)/x) for x in a]    #Computes firs Bessel function for
        c_0 = np.asarray(b_0)               #each value in 'a'

        for i in c_0:     #iterate through array to find NAN's replacing with 1
            c_0[np.isnan(c_0)] = 1
        print(c_0)
        return c_0      #Return array to be used for plotting

    elif n == 1:    #For the J1 Bessel function
        b_1 = [((np.sin(x)/x**2)-(np.cos(x)/x)) for x in a]
        c_1 = np.asarray(b_1)

        for i in c_1:     #iterate through array to find NAN's replacing with 0
            c_1[np.isnan(c_1)] = 0
        print(c_1)
        return c_1

    elif n == 2:   #For the J2 Bessel function
        b_2 = [(((3/x**2)-1)*(np.sin(x)/x)-((3*np.cos(x))/x**2)) for x in a]
        c_2 = np.asarray(b_2)

        for i in c_2:     #iterate through array to find NAN's replacing with 0
            c_2[np.isnan(c_2)] = 0
        print(c_2)
        return c_2

d = np.stack((a,bes(0,a)),1) #rotates matrix
e = np.stack((a,bes(1,a)),1) #rotates matrix
f = np.stack((a,bes(2,a)),1) #rotates matrix

print (d)
print(" ")
print (e)
print(" ")
print (f)

plt.plot(a,bes(0,a), linestyle = "--", color="r", label = "J0") #Plot each fn.
plt.plot(a,bes(1,a), linestyle = ":", color="m", label = "J1")
plt.plot(a,bes(2,a), "k", label = "J2")
plt.xlim(0, 20)     #Define the x limit of the plot
plt.xlabel("x")     #Label x axis
plt.ylabel("y")     #Label y axis
plt.legend(loc=1)   #Plot the legend
plt.title("A Graph Showing the First Three Spherical Bessel Functions")
plt.savefig("Bessel.png")       #Save plot as png image

plt.show()
