import tushare as ts
import csv
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

gdp_years = ts.get_gdp_year()
gdp_quarters = ts.get_gdp_quarter().head(25)

years = []
yearsgdp = []
for i in range(5):
    years.append(gdp_years.iloc[i]['year'])
    yearsgdp.append(gdp_years.iloc[i]['gdp'])

quarters = []
quartersgdp = []
for i in range(25):
    qinfo = gdp_quarters.iloc[i]
    if qinfo.quarter > years[0]:
        continue
    elif qinfo.quarter < years[-1]:
        break
    
    quarters.append(qinfo.quarter)
    quartersgdp.append(qinfo.gdp)

years.reverse()
yearsgdp.reverse()
quarters.reverse()
quartersgdp.reverse()

interq = quartersgdp.copy()
for i in range(len(quartersgdp)):
    if i % 4 != 0:
        quartersgdp[i] -= interq[i-1]

plt.figure(1)
font = FontProperties(fname="./SimHei.ttc", size=10)

plt.subplot(211)
plt.bar(years,yearsgdp)
plt.xticks(years)
plt.ylabel(u'年度GDP', fontproperties=font)
plt.title(u'近五年GDP比较', fontproperties=font)

plt.subplot(212)
for i in range(0, 20, 4):
    plt.plot(np.arange(1, 5), quartersgdp[i:i+4], linestyle='dashed', marker='o', label=years[i//4])
plt.legend(loc='upper left')
plt.xticks([i for i in range(1, 5)])
plt.xlabel(u'季度', fontproperties=font)
plt.ylabel(u'单季度GDP', fontproperties=font)
plt.title(u'近五年单季度GDP走势', fontproperties=font)

plt.show()

