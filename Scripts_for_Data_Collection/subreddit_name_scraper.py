from bs4 import BeautifulSoup as bs
import requests
import lxml
import pandas as pd
import numpy as np

def get_text(num):
    get = requests.get(f'http://redditlist.com/all?page={num}')
    soup = bs(get.content, 'lxml')
    items = soup.find_all('div', class_='listing-item')
    text = [i.find('span',class_='subreddit-url').a.text for i in items]
    return(text)

df = pd.DataFrame([], columns=['names'])

for i in range(41):
    text = get_text(i)
    dfa = pd.DataFrame(text, columns=['names'])
    df = df.append(dfa)
    if i % 5 == 0:
        print(f"Page {i} of 40.")

df = df.drop_duplicates(subset=None, keep='first')

df.to_csv('subreddit_names.csv')
