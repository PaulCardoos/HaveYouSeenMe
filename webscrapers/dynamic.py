import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

people = []

driver = webdriver.Chrome()
driver.get('https://www.missingkids.org/gethelpnow/search/poster-results')

driver.find_element_by_class_name("missing-filter-submit").click()
#need to wait for page to load
time.sleep(2)


l = driver.find_element_by_link_text(">")
l.click()
time.sleep(2)
names = driver.find_elements_by_class_name("missing-person-name")
for i in names:
    name = i.text
    people.append(name)

print(people)

#after we open a page we want to shut it to avoid having 5000 tabs open

for person in people:
    posters = driver.find_element_by_link_text(person)
    posters.click()
    #save the main page
    main_window = driver.current_window_handle
    #put focus on neew tab open which has poster of missing child
    driver.switch_to.window(driver.window_handles[1])
    #sleep for a second and wait for the page to load
    time.sleep(3)
    #close the current page that we are focused on
    driver.close()
    #switch back to main page
    driver.switch_to_window(main_window)
    

   

    


# soup = BeautifulSoup(driver.page_source, "html.parser")
# persons = soup.find_all("div", attrs={"class" : "missing-person-info"})

# for person in persons: 
#     data = person.find_all("div", attrs={"class" : "missing-person-personal-info"})
    
#     name = person.find("a", attrs={"class" : "missing-person-name"}).get_text(strip=True)    
#     print(name)
#     for info in data: 
#         i = info.get_text(strip =True)
#         print(i)

# driver.quit()

    

