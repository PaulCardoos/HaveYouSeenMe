from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()
driver.get("https://www.missingkids.org/poster/USVA/VA21-0619/1/screen")
time.sleep(2)

soup = BeautifulSoup(driver.page_source, features="html.parser")

name = {}
image = {}
missingSince = {}
location = {}
ageNow = {}
sex = {}
race = {}
hairColor = {}
eyeColor = {}
height = {}
weight = {}
details = {}

#get the name of the missing child
missingChildName = soup.find("h3").get_text(strip=True)
name["name"] = missingChildName

#get missing child image
image_url = soup.find("img", {"class" : "photo"}).attrs.get("src")
image["image"] = image_url

#get the date the child went missing
missing = soup.find("li", {"class" : "missingDate"})
dates = missing.find_all("li")
missingSince[dates[0].get_text()] = dates[1].get_text()

#get the location the child went missing from
missing = soup.find("li", {"class" : "missingLocation"})
locations = missing.find_all("li")
location[locations[0].get_text()] = locations[1].get_text()

#get the age the child is now
missing = soup.find("li", {"class" : "ageNow"})
ages = missing.find_all("li")
ageNow[ages[0].get_text()] = ages[1].get_text()

#get the gender of the missing child
missing = soup.find("li", {"class" : "sex"})
sexes = missing.find_all("li")
sex[sexes[0].get_text()] = sexes[1].get_text()

#get the race of the missing child
missing = soup.find("li", {"class" : "race"})
races = missing.find_all("li")
race[races[0].get_text()] = races[1].get_text()

#get the hair color of the missing child
missing = soup.find("li", {"class" : "hairColor"})
colors = missing.find_all("li")
hairColor[colors[0].get_text()] = colors[1].get_text()

# get the eye color of the missing child
missing = soup.find("li", {"class" : "eyeColor"})
eyeColors = missing.find_all("li")
eyeColor[eyeColors[0].get_text()] = eyeColors[1].get_text()

#get the height of the missing child
missing = soup.find("li", {"class" : "height"})
heights = missing.find_all("li")
height[heights[0].get_text()] = heights[1].get_text()

#get the weight of the missing child
missing = soup.find("li", {"class" : "weight"})
weights = missing.find_all("li")
weight[weights[0].get_text()] = weights[1].get_text()

#get details about the missing case
text = soup.find("p", {"class" : "narrativeTextBlock"}).get_text(strip=True)
details["details"] = text



print(name)
print(image)
print(missingSince)
print(location)
print(ageNow)
print(sex)
print(race)
print(hairColor)
print(eyeColor)
print(height)
print(weight)
print(details)



