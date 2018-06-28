import random
import requests
import json


def basic_contact_info(mccl_codes, csl_codes):
    name_data = name_and_gender()
    contact_profile = {
        "CategoryID": category_code(mccl_codes),
        "DateOfBirth": date_of_birth(),
        "Firstname": name_data['first_name'],
        "Gender": name_data['gender'],
        "Lastname": name_data['last_name'],
        "Middlename": name_data['middle_init'],
        "StatusID": status_code(csl_codes),
        "TaxID": tax_id(),
        "TypeID":"I"
    }
    return contact_profile


def basic_address(client_id):
    address_data = {
        "Address1": street_address(),
        "City": city(),
        "ClientID": client_id,
        "State": state(),
        "TypeID": address_type_id(),
        "Zip": zip()
    }
    return address_data


def basic_phone(client_id):
    phone_data = {
        "ClientID": client_id,
        "Number": phone_number(),
        "TypeID": phone_number_type_id()
    }
    return phone_data


def basic_internet(client_id, first_name, last_name):
    email_data = {
        "Address": email(first_name, last_name),
        "ClientID": client_id,
        "TypeID": 1
    }


def category_code(mccl_codes):
    return mccl_codes[random.randrange(0, len(mccl_codes)-1)]


def status_code(csl_codes):
    return csl_codes[random.randrange(0, len(csl_codes)-1)]


def date_of_birth():
    date_string = "/Date({})/".format(random.randrange(-1577923200000, 1009843200000))
    return date_string


def name_and_gender():
    r = requests.get('https://uinames.com/api/?region=united states')
    user_data = json.loads(r.text)
    details = {
        'first_name': str(user_data['name']),
        'last_name': str(user_data['surname']),
        'middle_init': chr(random.randrange(65, 65 + 26 + 1)),
        'gender': str(user_data['gender'])
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
    return area_code + str(random.randrange(1000,9999))


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