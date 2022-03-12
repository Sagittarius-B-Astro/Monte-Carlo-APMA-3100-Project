import random
import numpy as np
import math
import Project2a

def probless (allwt, num):
    count = 0
    for i in allwt:
        if (allwt[i] < num):
            count += 1
    return count/len(allwt)

n = int(input('Please type a value for n (the number of simulations):'))
allwt = [] #total wait time

for i in range(n):
    wt = 0 #wait time
    cc = 0 #call count by provider
    while cc < 4:
        wt = wt + 6
        x1 = Project2a.rnum() #generate random number to determine if available
        if x1 < 0.2: #if line is busy
            wt += 3
            cc += 1
        elif x1 < 0.5 and x1 > 0.2: #if customer is unavailable
            wt += 25
            cc += 1
        elif x1 < 1 and x1 > 0.5: #if available...
            x2 = Project2a.rnum()
            if x2 < ((1-exp(-25/12))/12): #wait time if available AND answers
                cc = 4
                X = -12*log(1-x2*12)
                wt += X
            elif x2 > ((1-exp(-25/12))/12): #wait time if avilable but no answer
                cc += 1
                wt += 25
    print(wt)
    allwt.append(wt)

meanwt = (np.sum(allwt))/n
stdwt = np.std(allwt)
medianwt = np.median(allwt)
fqtwt = meanwt-stdwt
tqtwt = meanwt+stdwt

print("The Statistics for Call Wait Time (W) is as follows:")
print("Mean: " + str(meanwt) + ", Median: " + str(medianwt) + ", First Quartile: " + str(fqtwt) + ", Third Quartile: " + str(tqtwt))
print(str(probless(allwt, 15)), str(probless(allwt, 20)), str(probless(allwt, 30)), str(1-probless(allwt, 40)))




