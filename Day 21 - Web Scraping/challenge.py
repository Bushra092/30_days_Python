
#? 🎯 Challenge
#? -  Scrape headlines from a news site

import requests
from bs4 import BeautifulSoup


URL = 'https://www.ndtv.com/'
Top_news_headings = []

try:
    response = requests.get(URL)
    response.raise_for_status()
    news = BeautifulSoup(response.text,  'html.parser')
    news_headings = news.find_all('h3', class_="crd_lnk") 
    for news in news_headings:
        a_tag = news.find('a')
        Top_news_headings.append(a_tag.text.strip())
        

except Exception as e:
    print(e)


print('\n\t\t\t News Headings From NDTV ')
for news in Top_news_headings:
    print('_________________________________________________________\n',news)


print(' _________________________________________________________\n\t\t\t\tNews Headings Ends \n ')