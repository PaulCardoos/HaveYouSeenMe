from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getKidInformation(driver):
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    missingPerson = {}
    
    #get the name of the missing child 
    try:
        missingChildName = soup.find("h3").get_text(strip=True)
        print(missingChildName)
        name = missingChildName.split(" ")
        #split the first name and the last name for easier quesries
        missingPerson["firstName"] = name[0]
        #remove first and last name
        name.remove(name[0])
        missingPerson["lastName"] = name[-1]
        name.remove(name[-1])
        #check for middle name
        if(len(name) > 0):
            missingPerson["middleName"] = (" ").join(name)
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
        missingPerson["missingSince"] = dates[1].get_text()
    except: 
        pass

    #get the location the child went missing from
    try: 
        missing = soup.find("li", {"class" : "missingLocation"})
        locations = missing.find_all("li")
        missingPerson["missingFrom"] = locations[1].get_text()
    except: 
        pass

    #get the age the child is now
    try: 
        missing = soup.find("li", {"class" : "ageNow"})
        ages = missing.find_all("li")
        missingPerson["ageNow"] = ages[1].get_text()
    except: 
        pass
    
    #get the gender of the missing child
    try:     
        missing = soup.find("li", {"class" : "sex"})
        sexes = missing.find_all("li")
        missingPerson[sexes[0].get_text().lower()] = sexes[1].get_text()
    except: 
        pass

    #get the race of the missing child
    try: 
        missing = soup.find("li", {"class" : "race"})
        races = missing.find_all("li")
        missingPerson[races[0].get_text().lower()] = races[1].get_text()
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
        missingPerson["eyeColor"] = eyeColors[1].get_text()
    except: 
        pass

    #get the height of the missing child
    try: 
        missing = soup.find("li", {"class" : "height"})
        heights = missing.find_all("li")
        missingPerson[heights[0].get_text().lower()] = heights[1].get_text()
    except: 
        pass

    #get the weight of the missing child
    try:
        missing = soup.find("li", {"class" : "weight"})
        weights = missing.find_all("li")
        missingPerson[weights[0].get_text().lower()] = weights[1].get_text()
    except: 
        pass

    #get details about the missing case
    try: 
        text = soup.find_all("p", {"class" : "narrativeTextBlock"})
        details = text[0].get_text(strip=True)
        missingPerson["details"] = details
    except: 
        pass
    
    return missingPerson

