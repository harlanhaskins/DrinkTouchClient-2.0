from selenium import webdriver

browser = None

def open_url(url):
    global browser
    if not browser:
        browser = new_browser()
    browser.get(url)

def new_browser():
    return webdriver.Firefox()

if __name__ == "__main__":
    import time

    while True:
        time.sleep(4)
        open_url("http://google.com")
