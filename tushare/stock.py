import tushare as ts
import csv

stock_info = ts.get_stock_basics()
stocks = stock_info.head(10)
stocks['riseDays'] = 0

for sindex in range(10):
    current_code = stocks.iloc[sindex].name
    history = ts.get_hist_data(current_code)
    rising_days = 0
    if history.iloc[0]['price_change'] < 0:
        continue
    else:
        for hindex in range(len(history.index)):
            if history.iloc[hindex]['price_change'] > 0:
                rising_days += 1
            else:
                break
    stocks.loc[(current_code, 'riseDays')] = rising_days

stocks.to_csv('stocks_infos.csv', encoding='gbk')
