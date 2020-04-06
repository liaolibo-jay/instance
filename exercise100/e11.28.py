import os

txt = input('输入一个字符串：')
num = input('输入要移除字符位置：')
list_txt = list(txt)
list_txt.pop(int(num)-1)
list_txt = ''.join(list_txt)
print(list_txt)
