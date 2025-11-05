
import pandas as pd
from bs4 import BeautifulSoup
import requests

name = []
km = []
yom = []
trans = []
ftype = []
price = []

url = 'https://www.cars24.com/buy-used-cars-chennai/?sort=bestmatch&serveWarrantyCount=true&storeCityId=5732'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
box = soup.find_all('a', {'class':'styles_carCardWrapper__sXLIp'})

for i in box:
    span = i.find('span', {'class': 'sc-braxZu kjFjan'})
    if span:
        name_parts = span.get_text().split()[1:]  # Skip brand name (e.g., 'Toyota')
        full_name = ' '.join(name_parts)
        name.append(full_name)
print(name)

km_list = []

for i in box:
    km_tags = i.find_all('p', {'class': 'sc-braxZu kvfdZL'})
    if km_tags:  # Make sure the tag exists
        kmtext = km_tags[0].get_text()  # Usually the first <p> contains km info
        km.append(kmtext)
print(km)

for i in box:
    span = i.find('span', {'class': 'sc-braxZu kjFjan'})
    if span:
        name = span.get_text().split()[0]  # Skip brand name (e.g., 'Toyota')
        yom.append(name)
print(yom)

for b in box:
    ft = b.find_all('p', {'class': 'sc-braxZu kvfdZL'})
    if len(ft) > 1:
        ftype.append(ft[1].get_text().strip())
print(ftype)

for b in box:
    tr = b.find_all('p', {'class': 'sc-braxZu kvfdZL'})
    if len(tr) > 1:
        trans.append(ft[2].get_text().strip())
print(trans)

for b in box:
    pr = b.find('p', {'class': 'sc-braxZu cyPhJl'}).get_text()
    price.append(pr)
print(price)