import requests
from bs4 import BeautifulSoup



title_list = []
pg_list = []
nav_link_list = []
def extract_city_news(main_url):
    manual_city = input("Enter city name: ")
    manual_city = manual_city.lower()

    main_url = main_url + '/' + manual_city

    content = requests.get(main_url)
    html_content = content.text
    soup = BeautifulSoup(html_content, "html.parser")
    print(main_url)
    req_content = soup.find('script',{'type':'application/ld+json'})
    r_c = soup.find('ul',{'class':'top-newslist clearfix'})
    data = req_content.text


    for x in r_c.findAll('li'):
        for y in x.findAll('a'):
            inner_link = y.get('href')
            pg = y.get('pg')
            title = y.get('title')
            inner_link = build_link(inner_link,main_url)

            title_list.append(title)
            nav_link_list.append(inner_link)
            pg_list.append(pg)
    dispatch_wall(title_list,nav_link_list,pg_list)


def build_link(link,main_url):
    if link.__contains__('/city'):
        link_list = link.split('/')
        link_list = link_list[3:]
        new_link = '/'.join(link_list)
        main_url = main_url+'/'
        upd_link = main_url+new_link
        return upd_link



def dispatch_wall(title_list,nav_link_list,pg_list):
    l = len(title_list)
    print(str(l))
    x=0
    while x<l:
        print(str(x))
        print(title_list[x])
        print(nav_link_list[x])
        print(pg_list[x])
        print('\n')
        x=x+1



extract_city_news("https://timesofindia.indiatimes.com/city")