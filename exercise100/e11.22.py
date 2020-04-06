import os
import math

for i in range(500):
    n = (i+100)**.5
    m = (i+168)**.5
    if (i+100)%n ==0 and (i+168)%n == 0:
        print('完全平方数为:',i)
