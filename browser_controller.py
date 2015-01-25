import requests
import time
from selenium import webdriver

browser = webdriver.Firefox()

def openUrl(url):
    browser.get(url)

#browser.get("http://rit.edu")
#browser.get("http://google.com")

while(True):
    time.sleep(4)
    openUrl("http://rit.edu")
