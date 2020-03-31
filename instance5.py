import os
import random

ag = 'y'
nrd = 0 #猜数字轮数
totc = 0 #总共猜的次数
while ag == 'y': # 只有同意才会继续进行猜数字
    rn = random.randint(1,5) # 产生一个1-5的随机数
    nrd += 1
    guessn = int(input('猜数字（输入一个1-5的数）:' ))
    count = 0
    while guessn != rn : 
        print('错了！再猜。')
        guessn = int(input('猜数字（输入一个1-5的数）:' ))
        count+=1
       
    print('恭喜你!')
    print('猜了 %i 次' % (count))
    totc += count
    ag = str(input('还玩嘛？(玩输入y，不玩输入n):' ))
print('共猜了%i轮,平均猜了 %.2f次' %(nrd, float(totc/nrd)))


