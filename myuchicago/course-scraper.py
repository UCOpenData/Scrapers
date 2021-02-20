from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

# Retrieve all of the anchor tags
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('table')

#finds title in header 2 tag
h = soup.findAll("h2")
for line in h:
        line = str(line)
        line = line.split(">")[1].split("<")[0]
        print(line)

#iterates through all tables to find tags
for table in tags:
    th = table.findAll("th")
    td = table.findAll("td")
    for line in th:
        line = str(line)
        line = line.split(">")[1].split("<")[0]
        print(line)
    for line in td:
        line = str(line)
        line = line.split(">")[1].split("<")[0]
        print(line)