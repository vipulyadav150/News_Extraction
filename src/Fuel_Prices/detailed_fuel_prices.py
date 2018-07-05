import json
import requests
from bs4 import BeautifulSoup
from src.Fuel_Prices.table import *

city_list = []
price_list = []
fuel_dict = {}
main_dict = {}
def extract_minimal():
    user_city = user_input()
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





    for keys in fuel_dict:
        if keys == user_city:
            print(keys +':'+fuel_dict[keys])

    n = input("Do you want to see the whole list(Press y for yes or n for no : ")
    n = n.lower()
    if n== 'y':
        table()
    else:
        return




def user_input():
    city  = input("Enter City : ").upper()
    return city





extract_minimal()

