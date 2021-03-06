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

#finds title in header 2 tag
title = soup.findAll("h2")
for line in title:
        line = str(line)
        line = line.split(">")[1].split("<")[0]
        line = line.split("-  Instructor(s):")
        classname = line[0].strip()
        instructor = line[1].strip()

#iterates through all tables to find tags
lst = pd.read_html(html, "instructor")
for df in lst:
        if "Comments" in df.columns:
                continue
        mean = df.mean(axis = 0)["Mean"]

print("class -", classname)
print("instructor(s) -", instructor)
print("mean -",mean)