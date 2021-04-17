import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from vardata import *
import pickle
import pandas as pd 
import requests
import config
import re

def main():
	companies, opentype, timeframe = user_pref()
	with open(output_file_name, opentype, newline='', encoding="utf-8") as file:
		driver, writer = initialize_driver(file)
		# write file header if rewriting file
		if opentype == 'w':
			writer.writeheader()
		for news_channel in news_channels:
			for company in companies:
				company_aliases = get_aliases(company)
				URL = get_url(driver, company, news_channel, timeframe)
				overall_count = 0
				valid = True 
				it = 0
				while valid:
					scroll(driver)
					it = it + 1
					count = 0
					link_tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
					#iterate over videos found
					for tag in link_tags:
						if overall_count != 0 and it != 1 and count < overall_count:
							continue
						link = tag.get_attribute('href')
						try:
							name = tag.get_attribute('aria-label')
						except Exception as e:
							print(e)
							continue
						#check for right uploader and trim file name
						if news_channel == None or name == None:
							continue
						if ('by ' + news_channel.lower()) in name.lower():
							name, ceo_name = get_names(news_channel, companies, company, name)
							if(ceo_name != "0"):
								if ((any(x in name.lower() for x in TALK_KEYWORDS)) \
                                and (any(y in name.lower() for y in PEOPLE_KEYWORDS)) \
                                and (any(z in name.lower() for z in company_aliases))) \
                                or ((any(x in name.lower() for x in TALK_KEYWORDS) \
                                and (ceo_name.lower() in name.lower()))):
									date, count, overall_count = write_data(writer, count, overall_count, driver, company, news_channel, name, link)
							else:
								if((any(x in name.lower() for x in TALK_KEYWORDS)) \
                                and (any(y in name.lower() for y in PEOPLE_KEYWORDS)) \
                                and (any(z in name.lower() for z in company_aliases))):
									date, count, overall_count = write_data(writer, count, overall_count, driver, company, news_channel, name, link)
					#check if any relevant videos found in iteration, if not, set loop condition to false
					if count == 0:
						valid = False
	driver.close()
	delete_duplicates()

def get_aliases(company):
	company_aliases = []
	try:
		df=pd.read_csv(company_aliases_file)
		aliases = str(df.loc[df.key == company].iloc[0])
		row = int(re.findall("Name: (.*),"  , aliases)[0])
		for i in range(5):
			if df.isnull().iat[row,i] == False:
				company_aliases.append(df.iat[row, i].lower())
	except Exception as e:
		print(e, company)
		company_aliases.append(company)
	return company_aliases

def user_pref():
	while True:
		ceo_name_input = input("Refresh CEO names? (y/n) ")
		if(ceo_name_input.lower() == 'y' or ceo_name_input.lower() == 'n'):
			break
		else:
			print("Invalid, please try again.")
	while True:
		timeframe = input("'refresh' to refresh all data, 'new' to fetch only one week's data: ")
		if(timeframe.lower() == 'refresh' or timeframe.lower() == 'new'):
			break
		else:
			print("Invalid, please try again.")
	if(ceo_name_input == 'y'):
		exec(open('./ceo_name.py').read())
		pickle_in = open('dict.pickle', 'rb')
		companies = pickle.load(pickle_in)
	else:
		try:
			pickle_in = open('dict.pickle', 'rb')
			companies = pickle.load(pickle_in)
		except:
			print('Warning: No file found')
			sys.exit(1)
	if(timeframe.lower() == 'refresh'):
		opentype = 'w'
	elif timeframe.lower() == 'new':
		opentype = 'a'
	return (companies, opentype, timeframe)

def initialize_driver(file):
	if config.path == '':
		driver = webdriver.Chrome(ChromeDriverManager().install())
	else:
		driver = webdriver.Chrome(executable_path = config.path)
	writer = csv.DictWriter(file, ['Company', 'News Channel', 'Name', 'Date', 'Link'])
	return (driver, writer)

def get_date(driver, link):
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.get(link)
	sleep(5)
	# find date
	try:
		date = driver.find_elements_by_xpath('//*[@id="date"]/yt-formatted-string')[0].text
	except:
		date = None
	try:
		date = date.split("Streamed live on ", 1)[1]
	except:
		pass
	# close tab
	driver.close()
	# switch back to main tab
	driver.switch_to.window(driver.window_handles[0])
	return date

def get_url(driver, company, news_channel, timeframe):
	URL = 'https://www.youtube.com/results?search_query=' + company.replace(' ', '+') + '+' + news_channel.replace(' ', '+') + '+interview'
	if (timeframe.lower() == 'new'): 
		URL = URL + '&sp=EgIIAw%253D%253D'
	driver.get(URL)
	return URL

def scroll(driver):
	# scroll to end of page
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)
	sleep(3)
	driver.page_source

def get_names(news_channel, companies, company, name):
	name = name.split('by ' + news_channel)[0]
	#check for interview
	try:
		ceo_name = companies[company]
	except:
		ceo_name = "0"
	return (name, ceo_name)

def write_data(writer, count, overall_count, driver, company, news_channel, name, link):
	date = get_date(driver, link)
	#add to csv
	writer.writerow({'Company' : company, 'News Channel' : news_channel, 'Name': name, 'Date': date, 'Link' : link})
	count = count + 1
	overall_count = count + 1
	return (date, count, overall_count)

def delete_duplicates():
	# delete duplicate entries
	data = pd.read_csv(output_file_name)
	data.sort_values('Link', inplace=True)
	data.drop_duplicates(inplace=True) 
	data.sort_values('Company', inplace=True)
	data.to_csv(output_file_name, index=False)

main()