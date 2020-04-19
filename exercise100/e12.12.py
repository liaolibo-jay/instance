import os

def income(num):
    out = 0
    if num <= 10:
        out = num *0.1
    elif num > 10 and num <= 20:
        out = 1 + (num - 10)*0.075
    elif num >20 and num <= 40:
        out = 1 + 0.75 + (num - 20) *0.05
    elif num > 40 and num <= 60:
        out = 1 + 0.75 + 1 +(num - 40) * 0.03
    elif num >60 and num <= 100:
        out = 1 + 0.75 +1 + 0.6 +(num -60) * 0.015
    else:
        out = 1 + 0.75 + 1 + 0.6 + 0.6 + (num - 100)*0.01

    return out

price = float(input('请输入利润(万元)：'))
print('发放奖金{}万元'. format(income(price)))
