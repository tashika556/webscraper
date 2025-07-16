import requests
import csv
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.geturl()

soup = BeautifulSoup(response.text,'html.parser')
quotes = soup.findall('div',class_='quote')

