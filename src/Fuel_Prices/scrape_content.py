from src.Fuel_Prices.extract_place import *
from bs4 import BeautifulSoup
import requests

def scrape_content():
    main_url,manual_city = extract_location("https://timesofindia.indiatimes.com/city")
    # print(main_url)
    soup = BeautifulSoup(requests.get(main_url).text,"html.parser")
    req_content = soup.find('div',{'id':'fuelList'})
    return req_content,main_url,manual_city


