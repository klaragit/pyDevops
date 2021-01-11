# shift + 3 => comment
#  command + / => comment out all selected
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/k/Documents/DevOps/PythonForTesters/webdrivers/chromedriver')

browser.get('https://apis.emergecds.com/api/v1/search/launchNewRelic?AccountID=ATHENA-NMHI-PROD&SSOToken=64255e05-07c7-478a-941a-4e44d15c62ca&disableRefetch=true')
time.sleep(3)


# scroller
 # html = browser.find_element_by_tag_name('html')
 # for i in range(10):
 #    html.send_keys(Keys.DOWN)


# xpathbutton = '//*[@id="hplogo"]/a/img'
# button = browser.find_element_by_xpath(xpathbutton).click()



# xpathsearchbox = '/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input'
# searcher = browser.find_element_by_xpath(xpathsearchbox).send_keys('markyshka')



# browser.quit()
