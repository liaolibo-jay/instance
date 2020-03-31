import os
import re
kw = input('请输入关键字:')

def fileinfo_match(name):
    try:
        with open(name) as f:
            return f.readlines()
    except:
        return []
        pass

fmatch=[]
txt = []
fdir=os.listdir(path='.')
for i in fdir:
    if kw in i:
        fmatch.append(i)
    else:
        txt = fileinfo_match(i)
        for j in txt:
            if kw in j.strip():
                fmatch.append(i)
                break

print(fmatch)
