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
        self.missingChildren = {}
        self.childrenNames = []
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        
    #get, use, and saveHTML is just for development purpose so 
    # we do not constantly send requests to the target site
    # when we refactor, develop and interface
    def open(self):
        self.driver.find_element_by_class_name("missing-filter-submit").click()
        time.sleep(3)

    def scrape(self):
        for person in self.childrenNames:
            posters = self.driver.find_element_by_link_text(person)
            posters.click()
            #save the main page
            main_window = self.driver.current_window_handle
            #put focus on neew tab open which has poster of missing child
            self.driver.switch_to.window(self.driver.window_handles[1])
            #sleep for a second and wait for the page to load
            time.sleep(4)
            #close the current page that we are focused on
            self.driver.close()
            #switch back to main page
            self.driver.switch_to_window(main_window)

    def getNames(self):
        #this function is just responsible for scraping the names off the page
        try:
            time.sleep(3)
            names = self.driver.find_elements_by_class_name("missing-person-name")
            for i in names:
                name = i.text
                self.childrenNames.append(name)
        except:
            pass

    def switchPages(self):
        #this function is strictly responsible for handling the pagination
        l = self.driver.find_element_by_link_text(">")
        l.click()
        self.childrenNames = []

    def getKidInformation(self, driver):
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        soup.find_element_by_class_name()

    def run(self):
        self.open()
        self.getNames()
        self.scrape()
        self.switchPages()


if __name__ == "__main__":
    headers = {}
    params = {}
    url = "https://www.missingkids.org/gethelpnow/search/poster-results"

    kids = missingKidScraper(headers, params, url)
    kids.run()