import os
import numpy as np
import matplotlib.pyplot as plt

# assignment 1
arr1 = np.array(range(4),dtype=float).reshape(2,2) #创建一个类型为float的2*2数组
# assignment 2
arr2 = np.zeros(36).reshape(6,6) #创建一个6*6的矩阵
arr3 = np.ones(36).reshape(6,6) #创建一个6*6的矩阵
arr4 = np.eye(6) #创建一个6*6的单位矩阵
# assignment 3
arr5 = np.arange(0,10,2) #创建一个步长为 2 的整数序列
# assignment 4
arr6 = np.linspace(1,10,6) #创建一个1-10等差数列
# assignment 5
arr7 = np.random.randint(1,50,size=(10)) #创建一个10位的整数随机数
arr7[np.argmax(arr7)] = 0 #利用argmax得到最大值位置并替换为0
# assignment 6
x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])
disxy = np.linalg.norm(x-y) #计算欧式距离
# assignment 7
np.random.seed(1) # 固定随机数种子
values = np.random.randn(1000).cumsum() #创建一个价值曲线值
plt.plot(values) #画图
#plt.savefig("ass7.eps")
# assignment 8
max_drawdown = np.max(np.maximum.accumulate(values) - values) #计算最大回撤

