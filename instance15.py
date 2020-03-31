import os
import requests
while True:
    city = input('请输入城市(输入no退出)：')
    if city == 'no':
        print('退出查询')
        break
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' %(city))
    weather = req.json().get('data')
    if weather:
        print('温度： ',weather.get('wendu'))
    else:
        print('查询失败，无该城市')

