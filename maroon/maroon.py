"""
Created on Sat Nov 14 16:47:01 2020

@author: deblina
"""
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

FRONT_PAGE_SELECTOR = '.media-heading , .stronger-headline, .blurb-text, strong, .plain-link em'

page = requests.get("https://www.chicagomaroon.com/")
soup = BeautifulSoup(page.content, 'html.parser')


text=soup.select(FRONT_PAGE_SELECTOR)

for i in text: 
    print(i)
    break; 
    

