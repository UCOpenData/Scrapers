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
	with open(output_file_name, 'w', newline='', encoding="utf-8") as file:
		driver = webdriver.Chrome(executable_path = driver_path)
		#driver = webdriver.Chrome('./chromedriver')
		writer = csv.DictWriter(file, ['Link', 'Subject', 'Course', 'Instructor', 'Year', 'Term', 'Rating'])
	
		#driver, writer = initialize_driver()
		flag = True
		writer.writeheader()
		URL = get_url(driver, 'MATH', '2020', 'Summer')
		sleep(40)
		for subject in subjects:
			for year in years:
				for term in terms:
					URL = get_url(driver, subject, year, term)
					scroll(driver)
					if empty_check(driver):
						continue
					else:
						while(flag):
							cells = driver.find_elements_by_class_name('title')
							for cell in cells:
								link = driver.find_element_by_tag_name('a')
								(classname, instructor, mean) = scrape_data(link)
								write_to_csv(subject, year, term, link, writer, classname, instructor, mean)
								scroll(driver)
								if(driver.find_element_by_tag_name('footer').isDisplayed()):
									flag = False


def empty_check(driver):
	if driver.find_element_by_class_name('messages error').size() == 0:
		return True
	else:
		return False



def initialize_driver():
	#driver = webdriver.Chrome(ChromeDriverManager().install())
	driver = webdriver.Chrome(executable_path = driver_path)
		#driver = webdriver.Chrome('./chromedriver')
	with open(output_file_name, 'w', newline='') as file:
		writer = csv.DictWriter(file, ['Link', 'Subject', 'Course', 'Instructor', 'Year', 'Term', 'Rating'])
	return (driver, writer)

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
	sleep(1)
	driver.page_source

def write_to_csv(subject, year, term, link, writer, classname, instructor, mean):
	writer.writerow({'Subject' : subject, 'Year' : year, 'Term' : term, 'Link' : link, 'Course' : classname, 'Instructor' : instructor, 'Rating' : mean})

main()