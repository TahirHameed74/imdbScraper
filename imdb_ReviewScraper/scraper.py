from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import re
import os
from operator import itemgetter 
import json
import time



url = "https://www.imdb.com/find?q=movieName&ref_=nv_sr_sm"

def scrapeFromEagleTracess():
	with open("movienames.txt") as file_in:
	    lines = []
	    for line in file_in:
	        lines.append(line)
	lines = [line.rstrip('\n') for line in lines]
	lines = [line.rstrip('\r') for line in lines]

	chrome_options = Options()  
	# chrome_options.add_argument("--headless") 
	driver = webdriver.Chrome(chrome_options=chrome_options)

	try:
		div = soup.find('div',{"class": "sc-12ddmbl-0 kEGgBM"})
	except Exception as e:
		print(e)

	
	for line in lines:
		f = open("myfile.txt", "a")
		refineMovieName = line.replace(" ", "+")
		_url = url.replace("movieName",refineMovieName)
		driver.get(_url)
		wait = WebDriverWait(driver, 20)
		soup = BeautifulSoup(driver.page_source,'lxml')
		try:
			getMovieLink = soup.find("div",{"class":"findSection"})
		except Exception as e:
			print e
		try:
			getMovieLink = getMovieLink.find("table",{"class":"findList"})
		except Exception as e:
			print e
		try:
			getMovieLink = getMovieLink.find("td",{"class":"result_text"})
		except Exception as e:
			print e
		try:
			getMovieLink = getMovieLink.find("a")["href"]
		except Exception as e:
			print e

		try:
			movieUrl = "https://www.imdb.com"+getMovieLink
			print(movieUrl)
		except Exception as e:
			movieUrl = "https://www.imdb.com"

		driver.get(movieUrl)
		wait = WebDriverWait(driver, 20)
		soupp = BeautifulSoup(driver.page_source,"lxml")
		try:
			movieRating = soupp.find("div",{"class":"AggregateRatingButton__ContentWrap-sc-1ll29m0-0 hmJkIS"})
			movieRating = movieRating.find("div",{"class":"AggregateRatingButton__Rating-sc-1ll29m0-2 bmbYRW"})
			movieRating = movieRating.find("span",{"class":"AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"}).get_text()
		except Exception as e:
			movieRating = 0
		
		print(line, movieRating)

		try:
			f.write(line)
			f.write(",")
			f.write(movieRating)
			f.write("\n")
			f.close()

		except Exception as e:
			print e

	



	#suppliersInfo=[x.encode('utf-8') for x in suppliersInfo]
	driver.close()



if __name__== "__main__":
  suppliersInfo = scrapeFromEagleTracess()


  # supplierName = suppliersInfo[::2]
  # supplierPhone = suppliersInfo[1::2]
  # for (i,j) in zip(supplierPhone,supplierName):
  # 		scrapeFromHipaaSpace(i,j)

















