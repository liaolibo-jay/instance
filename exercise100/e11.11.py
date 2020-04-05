import os
import re

count = 0
txt = input('请输入一段英文：')
for i in txt:
    if i == 'b':
        count += 1

print(count)
