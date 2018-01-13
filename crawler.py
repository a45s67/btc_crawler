import requests
res= requests.get('https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E6%AF%94%E7%89%B9%E5%B9%A3/usd')
from bs4 import BeautifulSoup
soup= BeautifulSoup(res.text,'html.parser')

data_prices=soup.select('#coin_portfolio_price_chart_btc')[0].prettify('utf-8').decode('utf-8')


import re 
m=re.search('data-prices="(.*?)"',data_prices)

import json
jd=json.loads(m.group(1))
len(jd)

