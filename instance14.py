import os
import re

with open('from.txt','r') as f:
    content = f.read()

rule = r'[a-zA-Z]+'
words= re.findall(rule, content)
words= '\n'.join(words)

with open('to.txt','w') as f:
    for i in words:
        f.writelines(i)
