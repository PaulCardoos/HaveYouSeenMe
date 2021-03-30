import time
import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

#note for concern, this program cannot break

class missingKidScraper: 
    def __init__(self, headers, params, url):
        self.headers = headers
        self.params = params
        self.url = url
        self.names = {}
        self.missingKidScraper
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        
    #get, use, and saveHTML is just for development purpose so 
    # we do not constantly send requests to the target site
    # when we refactor, develop and interface
    def getDriver(self):
        self.driver.find_element_by_class_name("missing-filter-submit").click()
        time.sleep(3)
        return self.driver.page_source

    def getHTML(self, url="", headers={}, params={}):
        #get site content and save response to html
        driver = webdriver.Chrome()
        driver.get(url, self.headers)
        html = driver.page_source
        driver.find_element_by_class_name('missing-person-personal-info')
        soup = BeautifulSoup(site.content, features='html.parser')
        print(soup)
        return soup

    def useHTML(self, html):
        #we want to be able to use the html we save to avoid be banned
        with open(html, "r") as file:
            soup = BeautifulSoup(file, features="html.parser")
        return soup

    def saveHTML(self, soup):
        #save soup context to html file
        with open("index.html", "w") as file:
            file.write(str(soup))

    def run(self):
        print(self.getDriver())


if __name__ == "__main__":
    headers = {}
    params = {}
    url = "https://www.missingkids.org/gethelpnow/search/poster-results"


    kids = missingKidScraper(headers, params, url)
    kids.run()
