import csv
import os
import numpy as np

# assignment 1: 读取文件
with open('iris.csv') as fl:
    data = np.loadtxt(fl,delimiter = ',')

# assignment 2: 找出最大最小值的位置
imax = np.argmax(data)
imin = np.argmin(data)

# assignment 3: 找出最大值最小值
dmax = data[imax]
dmin = data[imin]

# assignment 4: 从小到大排序
data.sort()

# assignment 5: 去重
newdata = np.unique(data)

# assignment 6: 计算平均值
meanvalue = np.mean(data)

# assignment 7: 标准差和方差
stdvalue = np.std(data)
varvalue = np.var(data)

# assignment 8: 总长
totvalue = np.sum(data)

# assignment 9: 累积总长
cumvalue = np.cumsum(newdata)

# assignment 10: 大于标准值的数目
ncalyx = (data>5.84).sum()
print('最大值为{},位置是{},最小值为{},位置是{},平均值为{},标准差为{},方差为{},总长为{},累计总长为{},大于平均值的个数为{}'.
        format(dmax,imax,dmin,imin,meanvalue,stdvalue,varvalue,totvalue,cumvalue,ncalyx))
