"""
Created on Sat Nov 14 16:47:01 2020

@author: deblina
"""
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.chicagomaroon.com/")
soup = BeautifulSoup(page.content, 'html.parser')

