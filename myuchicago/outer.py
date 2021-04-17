from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import csv
import config
from vardata import *
import re
from coursescraper import *

def main():
	with open(output_file_name, 'a', newline='', encoding="utf-8") as file:
		driver = webdriver.Chrome(executable_path = driver_path)
		#driver = webdriver.Chrome('./chromedriver')
		writer = csv.DictWriter(file, ['Link', 'Raw Title', 'Subject', 'Course', 'Instructor', 'Year', 'Term', 'Rating'])
	
		#driver, writer = initialize_driver()
		flag = True
		#writer.writeheader()
		URL = get_url(driver, 'MATH', '2020', 'Summer')
		sleep(30)
		for subject in subjects:
			for year in years:
				for term in terms:
					flag = True
					URL = get_url(driver, subject, year, term)
					scroll(driver)
					if empty_check(driver):
						continue
					else:
						while(flag):
							links = driver.find_elements_by_xpath("//td[@class='title']/a")
							for link in links:
								link = link.get_attribute('href')
								driver.execute_script("window.open('');")
								driver.switch_to.window(driver.window_handles[1])
								driver.get(link)
								sleep(1)
								source = driver.page_source
								(classname, instructor, mean, raw) = scrape_data(driver, source)
								# close tab
								driver.close()
								# switch back to main tab
								driver.switch_to.window(driver.window_handles[0])
								write_to_csv(subject, year, term, link, writer, classname, instructor, mean, raw)
								scroll(driver)
								if(driver.find_elements_by_tag_name('footer') != 0):
									flag = False


def empty_check(driver):
	if len(driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div/div/div/span')) == 1:
		return True
	else:
		return False


def get_url(driver, dept, year, term):
	#URL = 'https://www.google.com'
	URL = 'https://evaluations.uchicago.edu/?Department=' + dept + '&AcademicYear=' + year + '&AcademicTerm=' + term
	driver.get(URL)
	driver.maximize_window()
	return URL

def scroll(driver):
	# scroll to end of page
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)
	#sleep(0.5)
	driver.page_source

def write_to_csv(subject, year, term, link, writer, classname, instructor, mean, raw):
	writer.writerow({'Subject' : subject, 'Year' : year, 'Term' : term, 'Link' : link, 'Course' : classname, 'Instructor' : instructor, 'Rating' : mean, 'Raw Title' : raw})

main()