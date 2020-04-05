import os

txt = input('请输入一段文字：')
outdic = {}
for i in txt:
    outdic[i] = outdic.get(i,0) +1 # dict.get(key, default), 若指定的key不存在，则返回默认值
#    if i in outdic:
#        outdic[i] = 1
#    else:
#        outdic[i] = outdic[i] +1

for i in outdic:
    print('字符：%s，出现次数：%s。'%(i,outdic[i]))
    
