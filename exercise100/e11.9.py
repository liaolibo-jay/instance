import os

while True:
    a= str(input('请输入一个大于6位数的整数：'))
    if a.isdigit() and len(a) > 6:
        print('输出：%s' %(a[-7:-3]))
        break
    else:
        print('不合要求，重新输入')

