# importing all necessory scripts or functions
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests

# Getting data from website in text format



page_range = (10)


name_list = []
price_list = []


product = ("iphones")

# url = 'https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='

url = 'https://www.flipkart.com/search?q='
rurl = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='


class webscreapping:

    def __init__(self, url):

        for page in range(page_range):
            r = requests.get(url + str(product) + rurl + str(page))
            data = r.content
            soup = BeautifulSoup(data, "html.parser")  # parsing html parcer to data
            names = soup.findAll('div', attrs={'class': '_4rR01T'})
            prices = soup.findAll('div', attrs={'class': '_30jeq3 _1_WHN1'})

            for name in names:
                name_list.append(name.text)
            for price in prices:
                price_list.append(price.text)


def processingdata(name_list, price_list):
    df = pd.DataFrame()
    df['Name'] = name_list
    df['Price'] = price_list
    df["Price"] = df["Price"].str.replace("₹", "")
    df["Price"] = df["Price"].str.replace(",", "")
    df["Price"] = pd.to_numeric(df["Price"])
    df.to_csv("flipkart_iphones.csv", index=False)
    print("_____________ Data Scrapping 100% Done ________________")


ws1 = webscreapping(url)
processingdata(name_list, price_list)
