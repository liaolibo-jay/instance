import os

try:
    num = int(input('请输入一个数字：'))
    if num:
        if num <= 1:
            print('{}不是质数'.format(num))
        if num ==2:
            print('{}是一个质数'.format(num))
        for i in range(2,num):
            if (num%i) == 0:
                print('{}不是质数'.format(num))
                break
            else:
                print('{}是一个质数'.format(num))
                break
except ValueError:
    print('输入错误！')
