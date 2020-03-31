import os
import re

with open('from.txt') as f:
    content = f.read()

rule=r'[a-zA-Z]+'

n = len(re.findall(rule,content))

print('There are %i words in %s' %(n, 'from.txt'))
