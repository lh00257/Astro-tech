import numpy as np

a = np.array([4,6,2,4,2,5,6,8,9])

for counter, value in enumerate(a,1):   #Second value tells where to start counter from
    print(counter, value)
