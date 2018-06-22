import requests
import json
import datetime
import time
import getpass
import inquirer

import redtail  # Custom Redtail file created to hold all Redtail API calls and API Key
import input_check

data_type = [
    inquirer.List('data_type',
                  message='Select data type to seed',
                  choices=['Contacts', 'Accounts',
                           'Calendar Activities', 'Opportunities', 'Seminars'],
                  ),
]

# Input setup
rt_un = input('Redtail Username: ')
rt_pw = getpass.getpass('Redtail Password: ')
headers = redtail.headers(rt_un, rt_pw)
data_type = inquirer.prompt(data_type)['data_type']
data_volume = input_check.get_int('How many?')

api_calls = {
    'Contacts': redtail.create_contact,
    'Accounts': redtail.create_account,
    'Calendar Activities': redtail.create_act,
    'Opportunities': redtail.create_opp,
    'Seminars': redtail.create_seminar
}
api_call = api_calls[data_type]
# Create loop using data_volume integer as iteration counter that calls Redtail API to create data. Sleep 100ms between calls. 
# api_call(headers)
