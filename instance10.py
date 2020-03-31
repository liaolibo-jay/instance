import os
with open('source.txt') as f:
    txt = f.readlines()

info=input('请输入字符串：')
for i in txt:
    info = info.replace(i.strip(),'*'*len(i.strip()))

print(info)

