import os

list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']
a_dic = {}
for i in list_s:
    count = 0
    for j in list_s:
        if i ==j:
            count+=1
            a_dic[i] = count
print(a_dic)
