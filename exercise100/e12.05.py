import os

lst = [2,4,1,100,5,0]
amax = lst[0]
amin = lst[0]
for i in lst:
    if i > amax:
        amax = i
    if i < amin:
        amin = i

print('最大值与最小值的差为：',amax-amin)
