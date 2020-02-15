## Author : Lee Kang jin
## Description : Input - Location Type
##               Output - Auction Data List

from selenium import webdriver
import time

driver = webdriver.Chrome()
response = driver.get('https://www.courtauction.go.kr/')

time.sleep(5)
ch_tag = driver.find_element_by_css_selector('#idSidoCode1 > option:nth-child(5)') 
ch_tag.click()