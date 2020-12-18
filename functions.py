
######## Libraries ###############
import requests
import pandas as pd
from bs4 import BeautifulSoup

def euromillions_web_scraping():
    
    webpage_response = requests.get('https://www.euro-millions.com/results-history-2020')
    soup = BeautifulSoup(webpage_response.content)
    results = soup.select("div.archives")
    date_list = []

    for result in results:
        date = result.find('a', attrs={'class':'title'}).text # result not results
        date_list.append(date)
    # date_list

    # [li.string for li in soup.find_all('ul', {'class': 'balls small'}).findAll('li')]
    balls = []
    for ultag in soup.find_all('ul', {'class': 'balls small'}):
        numbers = [int(litag.text) for litag in ultag.find_all('li')]
        balls.append(numbers)
    
    # balls
    return date_list, balls

