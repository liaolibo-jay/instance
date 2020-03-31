import os
import random

lst1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
lst2=['A','B','C','D']
totlst=[]
for i in lst1:
    for j in lst2:
        totlst.append(str(i)+str(j))
totlst.append('K')
totlst.append('Q')

random.shuffle(totlst)
print(totlst)

fir=totlst[:-3:3]
sec=totlst[1:-3:3]
thi=totlst[2:-3:3]
end=totlst[-3:]
print(fir)
print(sec)
print(thi)
print(end)
