#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:21:15 2019

@author: bingtian
"""

import requests
from bs4 import BeautifulSoup

page = requests.get(
        "http://collegecatalog.uchicago.edu/thecollege/anthropology/")
soup = BeautifulSoup(page.content, 'html.parser')

major=[]
majorsoup=soup.select("li a")
for i in range (len(soup.select("li a"))):
    major.append(
            majorsoup[i].get_text())
major=major[7:71]


# code I used to scrape majorurl below    
# majorurlsoup=soup.select("li a", href=True)
# for i in majorurlsoup:
#     print ()   

majorurl=['http://collegecatalog.uchicago.edu/thecollege/anthropology',
 'http://collegecatalog.uchicago.edu/thecollege/architecturalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/arthistory/',
 'http://collegecatalog.uchicago.edu/thecollege/astronomyastrophysics/',
 'http://collegecatalog.uchicago.edu/thecollege/biologicalchemistry/',
 'http://collegecatalog.uchicago.edu/thecollege/biologicalsciences/',
 'http://collegecatalog.uchicago.edu/thecollege/chemistry/',
 'http://collegecatalog.uchicago.edu/thecollege/cinemamediastudies/',
 'http://collegecatalog.uchicago.edu/thecollege/classicalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/comparativehumandevelopment/',
 'http://collegecatalog.uchicago.edu/thecollege/comparativeliterature/',
 'http://collegecatalog.uchicago.edu/thecollege/comparativeraceethnicstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/caam/',
 'http://collegecatalog.uchicago.edu/thecollege/computationalneuroscience/',
 'http://collegecatalog.uchicago.edu/thecollege/computerscience/',
 'http://collegecatalog.uchicago.edu/thecollege/creativewriting/',
 'http://collegecatalog.uchicago.edu/thecollege/datascience/',
 'http://collegecatalog.uchicago.edu/thecollege/digitalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/eastasianlanguagescivilizations/',
 'http://collegecatalog.uchicago.edu/thecollege/economics/',
 'http://collegecatalog.uchicago.edu/thecollege/educationandsociety/',
 'http://collegecatalog.uchicago.edu/thecollege/englishlanguageliterature/',
 'http://collegecatalog.uchicago.edu/thecollege/environmentalscience/',
 'http://collegecatalog.uchicago.edu/thecollege/environmentalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/fundamentalsissuesandtexts/',
 'http://collegecatalog.uchicago.edu/thecollege/genderstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/geographicalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/geophysicalsciences/',
 'http://collegecatalog.uchicago.edu/thecollege/germanicstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/globalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/healthandsociety/',
 'http://collegecatalog.uchicago.edu/thecollege/history/',
 'http://collegecatalog.uchicago.edu/thecollege/scienceandmedicinehips/',
 'http://collegecatalog.uchicago.edu/thecollege/humanrights/',
 'http://collegecatalog.uchicago.edu/thecollege/inequalityandsocialchange/',
 'http://collegecatalog.uchicago.edu/thecollege/interdisciplinarystudieshumanities/',
 'http://collegecatalog.uchicago.edu/thecollege/jewishstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/latinamericanstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/lawlettersandsociety/',
 'http://collegecatalog.uchicago.edu/thecollege/linguistics/',
 'http://collegecatalog.uchicago.edu/thecollege/mathematics/',
 'http://collegecatalog.uchicago.edu/thecollege/MediaArtsandDesign/',
 'http://collegecatalog.uchicago.edu/thecollege/medievalstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/molecularengineering/',
 'http://collegecatalog.uchicago.edu/thecollege/music/',
 'http://collegecatalog.uchicago.edu/thecollege/neareasternlanguagescivilizations/',
 'http://collegecatalog.uchicago.edu/thecollege/neuroscience/',
 'http://collegecatalog.uchicago.edu/thecollege/newcollegiatedivision/',
 'http://collegecatalog.uchicago.edu/thecollege/norwegianstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/philosophy/',
 'http://collegecatalog.uchicago.edu/thecollege/physics/',
 'http://collegecatalog.uchicago.edu/thecollege/politicalscience/',
 'http://collegecatalog.uchicago.edu/thecollege/psychology/',
 'http://collegecatalog.uchicago.edu/thecollege/publicpolicystudies/',
 'http://collegecatalog.uchicago.edu/thecollege/religiousstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/renaissancestudies/',
 'http://collegecatalog.uchicago.edu/thecollege/romancelanguagesliteratures/',
 'http://collegecatalog.uchicago.edu/thecollege/slaviclanguagesliteratures/',
 'http://collegecatalog.uchicago.edu/thecollege/sociology/',
 'http://collegecatalog.uchicago.edu/thecollege/southasianlanguagescivilizations/',
 'http://collegecatalog.uchicago.edu/thecollege/statistics/',
 'http://collegecatalog.uchicago.edu/thecollege/theaterperformancestudies/',
 'http://collegecatalog.uchicago.edu/thecollege/tutorialstudies/',
 'http://collegecatalog.uchicago.edu/thecollege/visualarts/']



majorclassdict={}

for i in range(len(majorurl)): 
    page = requests.get(majorurl[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    majorclassdict[major[i]]=[]
    for j in range(len(soup.find_all(class_='courseblocktitle'))):
        majorclassdict[major[i]].append(
                soup.find_all(class_='courseblocktitle')[j].get_text()[5:-13])
    

#for j in major:
#    page = requests.get(
#        "http://collegecatalog.uchicago.edu/thecollege/anthropology/")
#    soup = BeautifulSoup(page.content, 'html.parser')
anthro=[]
for i in range (len(soup.find_all(class_='courseblocktitle'))):
        anthro.append(
                soup.find_all(class_='courseblocktitle')[i].get_text()[5:-13])
    
