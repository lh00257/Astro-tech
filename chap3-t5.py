import numpy as np
import math

'''
#function one
var = int(input('Enter a number'))

def fsin(x):
    result = (np.sin(x)/x)
    return result

print (fsin(var))
'''

#funtion 2
a = np.linspace(0,20,50)
b = np.array(1)
def fsin(x):
    b = [(np.sin(x)/x) for x in a]
    return b

print (a)
print (' ')
print (fsin(a))
print (' ')
c = np.stack((a,fsin(a)),1)

for counter, value in enumerate(c,1):   #Second value tells where to start counter from
    #if not (value.math.isnan):
    #    value[counter] = None
    print(counter, value)

print (c)

np.savetxt('chap3-t5.txt', c, header = 'value, calculation', fmt="%12.1f")
