# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:56:31 2025

@author: mkamr
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

service = Service("C:\\Users\\mkamr\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

products = []
prices = []
ratings = []

driver.get("https://www.flipkart.com/search?q=gaming+laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
time.sleep(5)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for a in soup.find_all('div', attrs={'class':"tUxRFH"}):
    name_tag = a.find('div', attrs={ 'class':'KzDlHZ'})
    price_tag = a.find('div', attrs={'class':'hl05eU'})
    rating_tag = a.find('div', attrs={'class':'XQDdHH'})

    if name_tag and price_tag and rating_tag:
        products.append(name_tag.text.strip())
        prices.append(price_tag.text.strip())
        ratings.append(rating_tag.text.strip())

driver.quit()

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')

print("✅ Scraping complete! Saved as products.csv")

