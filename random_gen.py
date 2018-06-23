import random
import requests
import json

# File that will hold functions that create and pull random data values
# http://namey.muffinlabs.com/api.js

# Create random Contact data
# 
    # Email
    #"Address":"String content",
	#"ClientID":2147483647,
	#"TypeID":1

    # Phones
    #"ClientID":2147483647,
	#"Number":"String content",
	#"TypeID":"String content"

    # Physical address
	#"Address1":"String content",
	#"City":"String content",
	#"ClientID":2147483647,
	#"State":"String content",
	#"TypeID":"String content",
	#"Zip":"String content",

    #"AnniversaryDate":"\/Date(928174800000-0700)\/",
	#"CategoryID":2147483647,
	#"ClientID":2147483647,
	#"ClientSinceDate":"\/Date(928174800000-0700)\/",
	#"DateOfBirth":"\/Date(928174800000-0700)\/",
	#"Firstname":"String content",
	#"Gender":"String content",
	#"Lastname":"String content",
	#"Middlename":"String content",
	#"StatusID":1,
	#"TaxID":"String content",
	#"TypeID":"I"

def date_of_birth():
    date_string = "\/Date({})\/".format(random.randrange(-1577923200000, 1009843200000))
    return date_string


def name_and_gender():
    r = requests.get('https://uinames.com/api/?region=united states')
    user_data = json.loads(r.text)
    details = {
        first_name: str(user_data['name']),
        last_name: str(user_data['surname']),
        middle_init: chr(random.randrange(65, 65 + 26 + 1)),
        gender: user_data['gender']
    }
    return details


def tax_id():
    return str(random.randrange(100000000,999999999))


def email(first_name, last_name):
    return "{}.{}@email.com".format(first_name, last_name)


def phone_number_type_id():
    types = ['HM','CL','WK']
    return types[random.randrange(0,2)]


def phone_number():
    area_code = str(random.randrange(201,998))
    return area_code + random.randrange(1000,9999)


def street_address():
    r = requests.get('https://uinames.com/api/?region=united states')
    user_data = json.loads(r.text)
    street_name = str(user_data['surname'])
    res_number = str(random.randrange(100,3000))
    directions = ['W','S','E','N']
    suffix = ['Dr','Rd','Ln','Ct','Ave','St']
    address = "{} {} {} {}".format(res_number, directions[random.randrange(0,3)], street_name, suffix[random.randrange(0,5)])
    return address

        
def city():
    cities = ['Phoenix','Sacramento','Atlanta']
    return cities[random.randrange(0,2)]


def state():
    states = ['AZ','CA','GA']
    return states[random.randrange(0,2)]


def address_type_id():
    types = ['H', 'M', 'W']
    return types[random.randrange(0,2)]


def zip():
    zip_string = ''
    i = 0
    while i < 5:
        zip_string += str(random.randrange(0,9))
        i += 1
    return zip_string


# Create random calendar data
#   subjects (Call Backs, Reviews, etc)


# Create random Account data
#   add data check for contact records in Redtail file, extra api call before put calls


# Create random Seminar data


# Create random Opp data