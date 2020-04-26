import numpy as np
import pandas as pd

# assignment 1
idata1 = np.random,randint(3,10,size=5)
s1 = pd.Series(data1,index=['a','b','c','d','e'])

# assignment 2
print('按位置索引：\n',s1[-3:])
print('按标签索引：\n',s1['c':'e'])

# assignment 3
df1 = [{'year':2017,'price':10},{'year':2018,'price':20},{'year':2019,'price':30}]
print('创建dataframe：')
print(pd.DataFrame(df1,index=list('012')))

# assignment 4
data2 = np.random.randint(5,15,size=(5,3))
df_text = pd.DataFrame(data2,index=list('acefg'),columns=['one','two','three'])

# assignment 5
df_text.loc['a','one'] = ''
df_text.loc['c','two'] = '-99'
df_text.loc['c','three'] = '-99'
df_text.loc['a','two'] = '-100'
df_text['four'] =['test','test','test','test','test']
df_text.reindex(['a','b','c','d','e','f','g','h'])
df_change = df_text

# assignment 6
df_change.dropna()
df_change.dropna(how = 'all')
df_change.fillna(0)
df_change.drop_duplicates()
