from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import ssl

def scrape_data(driver, source):
# Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        # Retrieve all of the anchor tags
        #, context=ctx).read()
        soup = BeautifulSoup(source, "html.parser")
        flag = 0
        #title = driver.find_elements_by_tag("h2")
        #finds title in header 2 tag
        title = soup.findAll("h2")
        for line in title:
                line = str(line)
                raw = line
                line = line.split(">")[1].split("<")[0]
                line = line.split("Instructor(s):")
                try:
                        classname = line[0].strip()
                        instructor = line[1].strip()
                except:
                        classname = "NA"
                        instructor = "NA"

        #iterates through all tables to find tags
        mean = "NA"
        try:
                lst = pd.read_html(source, "instructor")
        except:
                try:
                        lst = pd.read_html(source, "course")
                except: 
                        flag = 1
        if flag == 0:
                for df in lst:
                        if "Comments" in df.columns:
                                continue
                        try:
                                mean = df.mean(axis = 0)["Mean"]
                        except:
                                pass
        return (classname, instructor, mean, raw)