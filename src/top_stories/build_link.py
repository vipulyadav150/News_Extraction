from src.top_stories.extract_headlines import *


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





