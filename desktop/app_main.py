#Made by Aadhav, check out GitHub: @aadhav-n1 || HackerRank: @aadhav_n1
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import datetime
from os import path
from jinja2 import Environment, FileSystemLoader
import eel

link_dict = {
    1: ('https://in.reuters.com/finance', 'Business'),
    2: ('https://in.reuters.com/finance/markets', 'Market'),
    3: ('https://in.reuters.com/news/top-news', 'India'),
    4: ('https://in.reuters.com/news/south-asia', 'South Asia'),
    5: ('https://in.reuters.com/news/world', 'World'),
    6: ('https://in.reuters.com/news/technology', 'Technology'),
    7: ('https://in.reuters.com/news/sports', 'Sports'),
    8: ('https://in.reuters.com/news/entertainment/bollywood', 'Bollywood')
}

def getNews(val):
    my_url = link_dict[val][0]

    #Opens connection
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    #Lists for storing content
    title_list = []
    content_list = []

    #Parses HTML
    page_soup = soup(page_html, "html.parser")

    #grabs containers
    containers = page_soup.findAll("article",{"class" : "story"})

    # #Saving file
    now = datetime.datetime.now()
    titlename = link_dict[val][1] + " News for "+ now.strftime('%A, %d %B %Y')
    f = open(titlename + ".csv", 'w')

    for container in containers:
        try:
            #Grab news content
            story_container = container.find("div",{"class": "story-content"})
            news_content = story_container.p.text
            content_list.append(news_content)

            #Grab news titles
            news_title = story_container.a.h3.text.strip()
            title_list.append(news_title)

            # #Write to CSV file
            # print("{0}\n\n{1}\n\n\n".format(news_title, news_content))            
            f.write(news_title.replace(';','').replace(',' , '') + "," + news_content.replace(';','').replace(',' , '') + "\n") 

        except AttributeError:
            pass

    return_data = {
        'news_1_title':title_list[0], 
        'news_2_title':title_list[1], 
        'news_3_title':title_list[2], 
        'news_4_title':title_list[3], 
        'news_5_title':title_list[4], 
        'news_1':content_list[0], 
        'news_2':content_list[1], 
        'news_3':content_list[2], 
        'news_4':content_list[3], 
        'news_5':content_list[4], 
        'title':titlename
    }

    f.close()

    return return_data


root = path.dirname(path.abspath(__file__))
src = path.join(root, "web")
eel.init("web")

import json

@eel.expose
def parseNews(n):
    return json.dumps(getNews(n))

@eel.expose
def return_news():
    data= get_return_data()
    return json.dumps(getNews())

eel.start("templates/display_page.html", jinja_templates='templates')
