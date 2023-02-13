import pandas as pd

import requests
from bs4 import BeautifulSoup


url = 'https://www.google.com/search?q=site:myshopify.com+aa&sxsrf=AJOqlzXfWifj6GPig7RoicR81RV3DkQdDw:1676307840370&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwi-0--q_ZL9AhVvGFkFHWX2CMQQpwV6BAgBEBY&biw=1440&bih=655&dpr=2'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))


alphabet = list(map(chr, range(97, 123)))  # should be 123 for full alphabet

urls = []

for firstCharPosition in range(len(alphabet)):
    for secondCharPosition in range(len(alphabet)):
        url = 'https://www.google.com/search?q=site:myshopify.com+' + alphabet[firstCharPosition] + alphabet[secondCharPosition] + \
            '&sxsrf=AJOqlzXfWifj6GPig7RoicR81RV3DkQdDw:1676307840370&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwi-0--q_ZL9AhVvGFkFHWX2CMQQpwV6BAgBEBY&biw=1440&bih=655&dpr=2'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for link in soup.find_all('a'):
            lks = link.get('href')
            print(lks)
            urls.append(lks)
            print(urls)
            Dict = {'urls': urls}
            df = pd.DataFrame(Dict)
            print(df)
            df.to_csv(r'C\initialScrape.csv')
