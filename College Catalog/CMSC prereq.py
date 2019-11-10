#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:11:23 2019

@author: bingtian
"""

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
        "http://collegecatalog.uchicago.edu/thecollege/computerscience/")
soup = BeautifulSoup(page.content, 'html.parser')

prereq={}

text=soup.find_all(class_='courseblock main') + soup.find_all(class_='courseblock subsequence')

for i in range(len(text)):
    try:
        prereq["CMSC " + text[i].get_text().split('\n')[1][5:
        10]]=re.findall(r"Prerequisite\(s\): (.*)",text[i].get_text())[0]
    except IndexError:
        pass

for i in prereq:
    try: 
        prereq[i]=re.findall(r"(CMSC \d*)",prereq[i])
    except:
        pass

### enter prereq in the console after running ###
    
#for i in prereq:
#    if prereq[i]:
#        for j in range(len(prereq[i])):
#           print (prereq[i][j][5:10] + " -> " + i[5:10] + ";")
#    else:
#        print(i[5:10] + ";")