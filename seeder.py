import requests
import json
import datetime
import time
import getpass
import inquirer

import redtail  # Custom Redtail file created to hold all Redtail API calls and API Key

datatype_question = [
    inquirer.List('tz',
                  message='Select data type to seed',
                  choices=['Contacts', 'Accounts',
                           'Calendar Activities', 'Opportunities', 'Seminars'],
                  ),
]
# Input setup
rt_un = raw_input('Redtail Username: ')
rt_pw = getpass.getpass('Redtail Password: ')
tz = inquirer.prompt(datatype_question)['tz']

