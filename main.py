import bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup

with open("flipkart1.html",encoding = 'UTF-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content,"html.parser")
print(soup.title)
links = soup.find_all('a',attrs={'class':'wjcEIp'})
links