#script works fine, but there's scope for a lot of improvement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os,time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")#doesn't seem to work but not an error either
driver=webdriver.Chrome()
file=open("links.txt","r")

for i in file:
	#print(i)
	i="https://www.ss"+i[12:]
	#print(i[0:])
	driver.get(i[0:])
	options.add_argument("--disable-notifications")
	time.sleep(8)#lower this depending on your internet speed

	driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a").click()
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[0])
	

	
	