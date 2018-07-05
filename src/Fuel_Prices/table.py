import numpy as np
import pandas as pd
from numpy.random import randn
from bs4 import BeautifulSoup
import requests


city_list = []
price_list = []
fuel_dict ={}
def table():
    r = requests.get('https://www.bankbazaar.com/fuel/petrol-price-india.html?ck=Y%2BziX71XnZjIM9ZwEflsyDYlRL7gaN4W0xhuJSr9Iq7aMYwRm2IPACTQB2XBBtGG&rc=1')
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    r_c = soup.findAll('div', {'class': 'tab-content'})

    for x in r_c:
        r1_c = x.find('table', {'class': 'table table-curved tabdetails'}).find('tbody').findAll('tr')
        for y in r1_c:
            city = y.find('td', {'align': 'left'}).text
            price = y.findAll('td')[1].text
            if not city == 'City':
                city_list.append(city)
                price_list.append(price)
                fuel_dict[city] = price

    # print(city_list)
    df = pd.DataFrame(data = price_list,index=city_list,columns = ['price'])
    pd.set_option('display.max_rows', len(city_list))
    print(df)
    pd.reset_option('display.max_rows')


