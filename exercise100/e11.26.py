import os

def is_chinese(word):
    for x in word:
        if '\u4e00' <= x <= '\u9fa5':
            return True
    return False
    
txt = input('请输入一串字符：')
ndig = 0
nword =0
nspa = 0
ncwor =0
noth = 0
for i in txt:
    if i.isdigit():
        ndig += 1
    elif i.isspace():
        nspa += 1
    elif i.encode( 'UTF-8' ).isalpha():# 由于isalpha()会将中文也判断为英文字符，所以需添加encode( 'UTF-8' )
        nword += 1
    elif is_chinese(i):
        ncwor += 1
    else:
        noth += 1

print('有数字%i个，空格%i个，字母%i个，中文%i，其他%i个。'%(ndig,nspa,nword,ncwor,noth))
