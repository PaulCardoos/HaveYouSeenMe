from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getKidInformation(driver):
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    missingPerson = {}
    
    #get the name of the missing child 
    try:
        missingChildName = soup.find("h3").get_text(strip=True)
        missingPerson["name"] = missingChildName
    except:
        pass
    
    #get missing child image
    try:
        image_url = soup.find("img", {"class" : "photo"}).attrs.get("src")
        missingPerson["image"] = image_url
    except: 
        pass

    #get the date the child went missing
    try: 
        missing = soup.find("li", {"class" : "missingDate"})
        dates = missing.find_all("li")
        missingPerson[dates[0].get_text()] = dates[1].get_text()
    except: 
        pass

    #get the location the child went missing from
    try: 
        missing = soup.find("li", {"class" : "missingLocation"})
        locations = missing.find_all("li")
        missingPerson[locations[0].get_text()] = locations[1].get_text()
    except: 
        pass

    #get the age the child is now
    try: 
        missing = soup.find("li", {"class" : "ageNow"})
        ages = missing.find_all("li")
        missingPerson[ages[0].get_text()] = ages[1].get_text()
    except: 
        pass
    
    #get the gender of the missing child
    try:     
        missing = soup.find("li", {"class" : "sex"})
        sexes = missing.find_all("li")
        missingPerson[sexes[0].get_text()] = sexes[1].get_text()
    except: 
        pass

    #get the race of the missing child
    try: 
        missing = soup.find("li", {"class" : "race"})
        races = missing.find_all("li")
        missingPerson[races[0].get_text()] = races[1].get_text()
    except: 
        pass

    #get the hair color of the missing child
    try:       
        missing = soup.find("li", {"class" : "hairColor"})
        colors = missing.find_all("li")
        missingPerson[colors[0].get_text()] = colors[1].get_text()
    except: 
        pass

    # get the eye color of the missing child
    try:
        missing = soup.find("li", {"class" : "eyeColor"})
        eyeColors = missing.find_all("li")
        missingPerson[eyeColors[0].get_text()] = eyeColors[1].get_text()
    except: 
        pass

    #get the height of the missing child
    try: 
        missing = soup.find("li", {"class" : "height"})
        heights = missing.find_all("li")
        missingPerson[heights[0].get_text()] = heights[1].get_text()
    except: 
        pass

    #get the weight of the missing child
    try:
        missing = soup.find("li", {"class" : "weight"})
        weights = missing.find_all("li")
        missingPerson[weights[0].get_text()] = weights[1].get_text()
    except: 
        pass

    #get details about the missing case
    try: 
        text = soup.find_all("p", {"class" : "narrativeTextBlock"})
        details = text[0].get_text(strip=True)
        missingPerson["details"] = details
    except: 
        pass
    print(missingPerson)
    return missingPerson

