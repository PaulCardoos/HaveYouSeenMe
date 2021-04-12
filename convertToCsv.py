# Python program to convert
# JSON file to CSV
import json
import csv
  
  
# Opening JSON file and loading the data
# into the variable data
with open('kidJson.json') as json_file:
    data = json.load(json_file)
  

  
# now we will open a file for writing
data_file = open('missingKids.csv', 'w')
  
# create the csv writer object
csv_writer = csv.writer(data_file)
  
# Counter variable used for writing 
# headers to the CSV file
count = 0
  
for i in data:
    if count == 0:
  
        # Writing headers of CSV file
        header = ["_id", "firstName", "lastName", "middleName", "image", "missingSince", "city", "state","ageNow", "sex","race","hair color", "eye color", "height", "weight", "details"]
        csv_writer.writerow(header)
        count += 1
  
    # Writing data of CSV file
    try: 
        lastName = i["lastName"]
    except KeyError:
        lastName = ""   
    try: 
        firstName = i["firstName"]
    except KeyError:
        firstName = ""
    try: 
        middleName = i["middleName"]
    except KeyError:
        middleName = ""
    try: 
        details= i["details"]
    except KeyError:
        details = ""    
    try: 
        height= i["height"]
    except KeyError:
        height = ""
    try: 
        weight = i["weight"]
    except KeyError:
        weight = "" 
    try: 
        image = i["image "]
    except KeyError:
        image  = ""
    try: 
        missingSince = i["missingSince"]
    except KeyError:
        missingSince = "" 
    try: 
        city = i["city"]
    except KeyError:
        city = "" 
    try: 
        state = i["state"]
    except KeyError:
        state  = ""
    try: 
        ageNow = i["ageNow"]
    except KeyError:
        ageNow = "" 
    try: 
        sex = i["sex"]
    except KeyError:
        sex  = ""
    try: 
        race = i["race"]
    except KeyError:
        race = "" 
    try: 
        hairColor = i["Hair Color"]
    except KeyError:
        hairColor = ""
    try: 
        eyeColor = i["eyeColor"]
    except KeyError:
        eyeColor = "" 
        


    csv_writer.writerow([
        i["_id"],
        firstName,
        lastName,
        middleName,
        image,
        missingSince,
        city,
        state,
        ageNow,
        sex,
        race,
        hairColor,
        eyeColor,
        height,
        weight,
        details,
    ])
  
data_file.close()
