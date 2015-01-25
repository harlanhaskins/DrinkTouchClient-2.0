import requests
import time
from selenium import webdriver

browser = webdriver.Firefox()

def open_url(url):
    browser.get(url)

#browser.get("http://rit.edu")
#browser.get("http://google.com")

while(True):
    time.sleep(4)
    open_url("http://rit.edu")
