#script works fine, but there's scope for a lot of improvement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os,time
from selenium.webdriver.chrome.options import Options
driver=webdriver.Chrome()
file=open("links.txt","r")

for i in file:
	#print(i)
	i="https://www.ss"+i[12:]
	#print(i[0:])
	driver.get(i[0:])
	options.add_argument("--disable-notifications")
	time.sleep(8)#lower if your internet's fast

	driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a").click()
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[0])//
	"" savefrom.net website redirects you to a new tab. I haven't
	figured out a way to close it, as of yet, so line 20 just takes you back to the original tab***
	

	
	
