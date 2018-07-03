import requests
from bs4 import BeautifulSoup
from src.top_stories.build_link import *
from src.top_stories.dispatch_op import *


def extraction_top_stories(n,main_url):
    content = requests.get(main_url)  # Returns status
    html_content = content.text
    soup = BeautifulSoup(html_content, 'html.parser')

    requested_content = soup.find('ul', {'data-vr-zone': 'top_stories'})

    for x in requested_content.findAll('li'):
        for y in x.findAll('a'):
            links = y.get('href')
            title =y.get('title')
            # print(title)
            # print(links)

            links =  build_link(links,main_url)

            dispatch(title,links)






# extraction_top_stories(n=0,url = 'https://timesofindia.indiatimes.com/')




if __name__=='__main__':
    extraction_top_stories(n=0,main_url='https://timesofindia.indiatimes.com/')



