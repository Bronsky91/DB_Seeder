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
    'Address': redtail.create_address,
    'Internet': redtail.create_internet,
    'Phone': redtail.create_phone,
    'Accounts': redtail.create_account,
    'Calendar Activities': redtail.create_act,
    'Opportunities': redtail.create_opp,
    'Seminars': redtail.create_seminar,
    'MCCL': redtail.mccl_codes,
    'CSL': redtail.csl_codes
    }

    # api_call = api_calls[self.data_type]


    def __init__(self, data_type, headers, volume):
        self.data_type = data_type
        self.headers = headers
        self.volume = volume
    

    def request(self, *args):
        """ If no args are given the random_gen.basic pre-made request body will be used for API call. Otherwise any arguments made to the method will be added to the request body and sent to Redtail API"""
        if self.data_type == 'Contacts':
            contacts = {}
            client_data = []
            mccl_data = ApiCall.api_calls['MCCL'](self.headers)
            csl_data = ApiCall.api_calls['CSL'](self.headers)
            # Loop that creates a list of all mccl codes for the database
            mccl_codes = []
            for mccl_dict in mccl_data:
                mccl_codes.append(mccl_dict['MCCLCode'])
            # Loop that creates a list of all csl codes for the database
            csl_codes = []
            for csl_dict in csl_data:
                csl_codes.append(csl_dict['CSLCode'])
            # Loop that generates all random client data needed
            i = 0
            while i < self.volume:
                client_data.append(random_gen.basic_contact_info(mccl_codes, csl_codes))
                i += 1
            # Loop that makes api calls to Redtail per each contact randomly generated
            for client in client_data:
                contacts[ApiCall.api_calls[self.data_type](
                    self.headers, client
                )] = client
            # Loop that addes in Phone, Address, and Email data for each contact
            for c_id, value in contacts.iteritems():
                ApiCall.api_calls['Address'](self.headers, random_gen.basic_address(c_id))
                ApiCall.api_calls['Internet'](self.headers, random_gen.basic_internet(
                    c_id, value['Firstname'], value['Lastname']))
                ApiCall.api_calls['Phone'](self.headers, random_gen.basic_phone(c_id))
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

api_call = ApiCall(data_type, headers, data_volume)
api_call.request()