import requests
import json
import datetime
import time
import getpass
import inquirer

import redtail  # Custom Redtail file created to hold all Redtail API calls and API Key
import input_check
import random_gen


class ApiCall:
    """ Creates a Request instance that forms and makes the API call. Accepts headers, volume (number) of calls to make, and the type of data you want to send to the API. 
    """

    api_calls = {
    'Contacts': redtail.create_contact,
    'Accounts': redtail.create_account,
    'Calendar Activities': redtail.create_act,
    'Opportunities': redtail.create_opp,
    'Seminars': redtail.create_seminar
    }

    # api_call = api_calls[self.data_type]


    def __init__(self, data_type, headers, volume):
        self.data_type = data_type
        self.headers = headers
        self.volume = volume
    

    def request(self, *args):
        """ If no args are given the random_gen.basic pre-made request body will be used for API call. Otherwise any arguments made to the method will be added to the request body and sent to Redtail API"""
        if len(args) == 0:
            pass
        else:
            pass



data_type = [
    inquirer.List('data_type',
                  message='Select data type to seed',
                  choices=['Contacts', 'Accounts',
                           'Calendar Activities', 'Opportunities', 'Seminars'],
                  ),
]

# Boilerplate basic opton
# Second option which lists all fields per data_type as checklist for fields to be populated

# Input setup
rt_un = raw_input('Redtail Username: ')
rt_pw = getpass.getpass('Redtail Password: ')
headers = redtail.headers(rt_un, rt_pw)
data_type = inquirer.prompt(data_type)['data_type']
data_volume = input_check.get_int('How many?: ')