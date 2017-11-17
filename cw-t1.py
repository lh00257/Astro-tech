import numpy as np
import pylab as plt

a = np.linspace(0,20,50)
b = np.array(1)
'''
def bes_0(x):
    b = [(np.sin(x)/x) for x in a]
    c = np.asarray(b)

    for i in c:     #iterate through array to find NAN's
        c[np.isnan(c)] = 1
    print(c)
    return c

def bes_1(x):
    b = [((np.sin(x)/x**2)-(np.cos(x)/x)) for x in a]
    c = np.asarray(b)

    for i in c:     #iterate through array to find NAN's
        c[np.isnan(c)] = 0
    print(c)
    return c

def bes_2(x):
    b = [(((3/x**2)-1)*(np.sin(x)/x)-((3*np.cos(x))/x**2)) for x in a]
    c = np.asarray(b)

    for i in c:     #iterate through array to find NAN's
        c[np.isnan(c)] = 0
    #print(c)
    return c
'''

def bes(n,x):
    if n == 0:
        b_0 = [(np.sin(x)/x) for x in a]
        c_0 = np.asarray(b_0)

        for i in c_0:     #iterate through array to find NAN's replacing with 1
            c_0[np.isnan(c_0)] = 1
        print(c_0)
        return c_0

    elif n == 1:
        b_1 = [((np.sin(x)/x**2)-(np.cos(x)/x)) for x in a]
        c_1 = np.asarray(b_1)

        for i in c_1:     #iterate through array to find NAN's replacing with 0
            c_1[np.isnan(c_1)] = 0
        print(c_1)
        return c_1

    elif n == 2:
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

plt.plot(a,bes(0,a), "r")
plt.plot(a,bes(1,a), "m")
plt.plot(a,bes(2,a), "k")
plt.show()
