import os
import random
lstlet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N = 0
a_dic={}
while N != 200:
    random.shuffle(lstlet)
    l_str = ''.join(lstlet[0:8])
    if l_str not in a_dic:
        a_dic[N]=l_str
        N+=1
    else:
        continue
print(a_dic)
