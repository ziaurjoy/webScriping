# Import libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


# Scriping Pages

def tshart(pages):
    # define urls

    url = f'https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/' \
          f'pr?sid=clo%2Cash%2Cank%2Cedy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts&page={pages}'
    url_request = requests.get(url)
    soup = BeautifulSoup(url_request.content, 'html.parser')

    return soup


# function working for select data

def extract(soup):
    div = soup.find_all('div', class_='_1xHGtK')
    for items in div:
        title = items.find('a', class_='IRpwTa').text
        company_name = items.find('div', class_='_2WkVRV').text
        try:
            pack_of = items.find('div', class_='_3eWWd-').text
        except:
            pack_of = ''
        price = items.find('div', class_='_30jeq3').text.replace('₹', 'TK ')
        tshart = {
            'Product Name': title,
            'Company Name': company_name,
            'Pack Of': pack_of,
            'Price': price
        }

        tshart_list.append(tshart)
    return len(div)

# all data append to list

tshart_list = []

# select number of pages
for i in range(1, 6):
    print(f'Scriping pages {i}')
    extract(tshart(i))

df = pd.DataFrame(tshart_list)
df.to_csv('tsharts.csv')





