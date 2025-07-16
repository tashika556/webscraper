import requests
import csv
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.geturl()

soup = BeautifulSoup(response.text,'html.parser')
quotes = soup.findall('div',class_='quote')

with open('quotesextracted.csv','w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote','Author'])

for quote in quotes:
    text = quote.find('span',class_='text').text.strip()
    author = quote.find('small',class_='author').text.strip()  
    writer.writerow([text,author])

print("Quotes saved successfully in csv file.")
