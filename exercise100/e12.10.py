import os 

oritxt = input('请输入四位整数：')
outtxt = []
for i in oritxt:
    x = (int(i)+5)%10
    outtxt.append(x)

outtxt.reverse()

for i in range(4):
    print(outtxt[i],end='')

print()

