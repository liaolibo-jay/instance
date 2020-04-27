import numpy as np
import pandas as pd

data = pd.read_csv('~/instance/anabase/sh.600000.csv') # 读取CSV文件
print(data[:5])
print(data[-5:]) # 查看前五行和后五行数据
print(data.info())
print(data.describe()) # 查看统计描述和字段概况

print(data[:3]) # 利用[]位置索引选取前三行数据
print(data['date'])
print(type(data['date'])) #使用 [ ] 标签索引方式，选取出 “date” 一列，并用 type 查看返回的数据类型

print(data[['date','open','close']])
print(type(data[['date','open','close']])) #使用 [ ] 标签索引方式，取出 “date”、“open” 列和 “colse” 列，并用 type 查看返回的数据类型
print(data[data['close']>11.08]) #使用 [ ] 标签索引方式，选取收盘价大于 11.08 的所有数据

# 将 date 设置为索引，并重新命名数据库为 df1，使用 df.loc[] 标签定位方式，选取 df1 数据库中 2017-12-11 至 2017-12-20 的所有数据 
df1 = data.set_index('date')
print(df1.loc['2017-12-11':'2017-12-20'])
print(df1.loc[:,'open':'close']) # 使用 df.loc[] 标签定位方式，选取 df1 数据库中 open 至 close 间的所有列
print(df1.loc['2018-07-01':'2018-07-08','open':'close']) # 使用 df.loc[] 标签定位方式，选取 df1 数据库中时间从 2018-07-01 至 2018-07-08，open 至 close 间的所有列

