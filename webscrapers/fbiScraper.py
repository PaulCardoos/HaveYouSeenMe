import requests
from bs4 import BeautifulSoup
import json
from Connect import connect

#may need header to avoid recaptcha in some cases

class FbiScraper: 
    #scraper to retrieve all missing persons from fbi website
    def __init__(self, url, headers, params):
        self.headers = headers
        self.url = url
        self.params = params
        self.people = {}
        self.missingPersons = []

    #get, use, and saveHTML is just for development purpose so 
    # we do not constantly send requests to the target site
    
    def getHTML(self, url="", headers={}, params={}):
        #get site content and save response to html
        site = requests.get(self.url ,params=params, headers=self.headers)
        soup = BeautifulSoup(site.content, features='html.parser')
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
    
    def getMissingNames(self, repeat):
        #get the names of each individual in the missing fbi db
        for i in range(1, repeat+1):
            params = {"page" : str(i)}
            s = self.getHTML(self.url, self.headers, params)
            titles = s.find_all("h3" , attrs={"class" : "title"})
            #creates a key : value mapping for name and next url to scrape
            for title in titles: 
                urls = title.find("a").attrs.get("href")
                names = title.find("a").get_text(strip=True)
                
                self.people[names] = urls
    
    def getMissingPersonInfo(self, url):
        r = requests.get(url)
        html = BeautifulSoup(r.content, features="html.parser")
    
        missingPersons = {}
        try:
            name = html.find("h1", attrs={"class" : "documentFirstHeading"}).get_text(strip=True).capitalize()
            missingPersons["name"] = name
        except: 
            pass

        try:
            summary = html.find("p", attrs={"class" : "summary"})

            #convert to string to apply string methods
            string = str(summary)
            string = string.split("<br/>")

            #the html on this page was poorly written so the parse was a bit complicated
            dateMissing = string[0].strip().split(">")[1]
            missingPersons["dateMissing"] = dateMissing
            locationMissing = string[1].strip().split("<")[0]
            missingPersons["locationMissing"] = locationMissing
        except:
            pass
        
        descriptionTable = html.find("tbody")
        #get a list of the elements in the table
        try:
            trs = descriptionTable.find_all("tr")
            for tr in trs:
                try: 
                    t = tr.find_all("td")
                    missingPersons[t[0].get_text(strip=True)] = t[1].get_text(strip=True)
                except:
                    pass
        except:
            pass

        #lastly get remarks and details and add to json
        try: 
            remark = html.find("div", attrs={"class" : "wanted-person-remarks"}).find("p").get_text(strip=True)
            missingPersons["remarks"] = remark
            details = html.find("div", attrs={"class" : "wanted-person-details"}).find("p").get_text(strip=True)
            missingPersons["details"] = details
        except: 
            pass

        
        image = html.find("div" , attrs={"class":"lightbox-content"}).find("img").attrs.get("src")
        missingPersons["image"] = image 
      
        #add dictionary to list to set up for dumps
        self.missingPersons.append(missingPersons)
       
    def getAllPeople(self):
        for person in self.people:
            self.getMissingPersonInfo(self.people[person])
        
    def writeJsonToFile(self):
        print(self.missingPersons)
        jString = json.dumps(self.missingPersons)
        with open("missing-person.json", "w") as jsonFile:
            jsonFile.write(jString)

    def run(self):
        #the three is to go three pages deep
        self.getMissingNames(3)
        self.getAllPeople()
        self.writeJsonToFile()

if __name__ == '__main__':
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '__cfduid=d0de7924c351b30b1544c9354c3d5dad61616604944; __castle_fv__=shown; _ga=GA1.2.624132444.1616604982; _gid=GA1.2.327284271.1616604982; sticky-footer=no-animation; _4c_=%7B%22_4c_s_%22%3A%22jVJNr5swEPwrTz4%2FJ%2F7CNrlVrVT10FurHiODDVihgIwT%2Bhrlv3cNhPSll3JhPbsz3p31FU2N69CBSiolzYTKVCZe0cm9jehwRcHb9LugA%2BI0k1Izi4WjHAtBNM5ZrjEnjNGSOUZUgV7Rr6TFBNck14xzentF5bBqXFHZWwdaNN9RsaO4GoERfwOCmSAQD6G35zIe49uQ6iZXvIz2BAnrLr50x8nb2MwCjDzQxvm6iQkmeoaHkA4QTb6z%2FfSgQWMPdKPlMge0CP00usT82IT%2Bp3vRCe3BB%2FRjJqRmg6tcCHMVnEYfU5tV4Xd1f1kB8G7B8IINyT2pITqHFsImxmE87PfTNO1W5n4yXXR2f%2FK2M8PenLzBY2OmLhrs6rp1Y%2Bw7EHBd0hqChbjtS9Om213KfP5w%2FP7lU7qICcqZEGBvWikRsAbIfwu%2Brl346mLTw0rhbKyPvu9MmwyDFwBmVubcxnRMppStGUdfWjeeYj%2Bg27paKhWhWmqtNKwuwkBaCpK%2B2zLqvGmpn8tl%2Fm%2F54jh23cajZOPJnApB59f4zINO769SFJkplLWYGS6wyJTAplQFLlmhJCslMVyj%2F9Ls7pIPH7a3TAmwZAZlfoj3Vmd7M8hoJp5qAUm1d0XzrLXkw7RJrQnOc%2Fm%2BNCFQetm0iCNVoaoMS8YZFiWpcMF5gXNjOeFMFUbRvwamioH5mq0DU73Me7v9AQ%3D%3D%22%7D',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    params = { 
        'page' : "1"
    }

    url = "https://www.fbi.gov/wanted/kidnap/@@castle.cms.querylisting/querylisting-1"

    fbi = FbiScraper(url, headers, params)
    fbi.run()
    #print(fbi.people)
    print(fbi.missingPersons)
    #s = fbi.getHTML()
    #fbi.saveHTML(s)
    #s = fbi.useHTML("index.html")
    #fbi.testMissingPersonInfo(s)
    #print(fbi.missingPersons)
    #n = fbi.getMissingNames(3)
    #fbi.getIndividualInfo()
    #print(n)
    #soup = fbi.useHTML("index.html")
    #names = fbi.getMissingNames(soup)
