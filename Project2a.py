import random

def rnum():
    a = 24693 #float(input('Please type a value for a (the multiplier):'))
    x0 = 1000 #float(input('Please type a value for x0 (the starting value):'))
    c = 3517 #float(input('Please type a value for c (increment):'))
    K = 131072 #float(input('Please type a value for K (modulus):'))

    x = x0
    count = 0

    while (count < 1):
        x = round(((x*a+c)%K)/K, 4)
        #print (x)
        count += 1

    return x
    
rnum()
