def gcd_naive(a,b):
    for i in range(min(a, b), 0, -1):
        if a % i ==0 and b % i == 0: return i

def gcd(a, b):
    return gcd(b, a%b) if a%b !=0 else b

def gcd2(a, b):
    while a % b != 0 : a, b = b, a%b 
    return b

import math
math.gcd(1,2)

# 주피터에서의 속도측정
# %time (gcd(10*30, 2*30)

