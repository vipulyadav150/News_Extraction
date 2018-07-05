from src.Fuel_Prices.extract_place import *
from src.Fuel_Prices.scrape_content import *
from src.Fuel_Prices.dispatch_prices import *
import requests



def extract_fuel_prices():
    r_c , main_url,manual_city = scrape_content()
    # print(r_c)
    print(main_url)
    for x in r_c:
        link = x.find('li').find('a').get('href')
        generated_link =  main_url+'/'+'/'.join(link.split('/')[3:])

        new_soup = BeautifulSoup(requests.get(generated_link).text,'html.parser')
        required = new_soup.find('div',{'class':'Normal'}).text
        dispatch_price(generated_link,required,manual_city)



if __name__ == '__main__':
    extract_fuel_prices()