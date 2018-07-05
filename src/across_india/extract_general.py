import requests
from bs4 import BeautifulSoup




def general_extraction(main_url):
    print('ACROSS INDIA TODAY :' + '\n')
    soup = BeautifulSoup(requests.get(main_url).text,'html.parser')
    req_content = soup.findAll('ul',{'data-vr-zone':'across_toi'})
    for x in req_content:
        r_c = x.findAll('li')
        for y in r_c:
            r1_c = y.findAll('a')
            for z in r1_c:
                title = z.get('title')
                pg = z.get('pg')
                link = z.get('href')
                link = build_link(link,main_url)
                dispatch_op(title,link,pg)


def build_link(link,main_url):
    if not link.__contains__(main_url):
        if link[0]=='/':
            link = link[1:]
            link = main_url+link

    else:
        if link[0]=='/':
            link = link[1:]
            link = main_url+link
    return link

def dispatch_op(title,link,pg):

    print(title)
    print(link)
    print(pg + '\n')


general_extraction(main_url='https://timesofindia.indiatimes.com/')