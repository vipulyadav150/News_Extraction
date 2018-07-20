import requests
from bs4 import BeautifulSoup
from src.top_stories.extract_headlines import *
from src.top_stories.dispatch_op import *

def extract_latest_stories(n,main_url):
    content = requests.get(main_url)
    html_content = content.text
    soup = BeautifulSoup(html_content,'html.parser')
    requested_content = soup.findAll('div',{'class':'main-content'})
    title_list = []
    link_list= []
    for x in requested_content:
        for y in x.findAll('ul',{'data-vr-zone':'latest'}):
            for z in y.findAll('li'):
                for w in z.findAll('a'):
                    title = w.get('title')
                    links = w.get('href')
                    links = build_link(links,main_url)
                    dispatch(title,links)
                    title_list.append(title)
                    link_list.append(links)
    return title_list,link_list



# extract_latest_stories(n=0,main_url='https://timesofindia.indiatimes.com/')