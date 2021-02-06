from urllib.request import urlopen
from bs4 import BeautifulSoup
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


for table in tags:
    lines = table.findAll("td")
    for line in lines:
        line = str(line)
        line = line.split(">")[1].split("<")[0]
        print(line)