import requests
import json
import datetime
import time
import getpass
import inquirer

import redtail  # Custom Redtail file created to hold all Redtail API calls and API Key
import prod_redtail
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
    'Notes': redtail.create_note,
    'Accounts': redtail.create_account,
    'Calendar Activities': redtail.create_act,
    'Opportunities': redtail.create_opp,
    'Seminars': redtail.create_seminar,
    'MCCL': redtail.mccl_codes,
    'CSL': redtail.csl_codes
    }

    prod_api_calls = {
    'Contacts': prod_redtail.create_contact,
    'Address': prod_redtail.create_address,
    'Internet': prod_redtail.create_internet,
    'Phone': prod_redtail.create_phone,
    'Notes': prod_redtail.create_note,
    'Accounts': prod_redtail.create_account,
    'Calendar Activities': prod_redtail.create_act,
    'Opportunities': prod_redtail.create_opp,
    'Seminars': prod_redtail.create_seminar,
    'MCCL': prod_redtail.mccl_codes,
    'CSL': prod_redtail.csl_codes
    }

    # api_call = api_calls[self.data_type]


    def __init__(self, data_type, headers, volume, environment):
        self.data_type = data_type
        self.headers = headers
        self.volume = volume
        self.environment = environment
    

    def request(self, *args):
        """ If no args are given the random_gen.basic pre-made request body will be used for API call. Otherwise any arguments made to the method will be added to the request body and sent to Redtail API"""
        if self.environment == 'dev':
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
                for c_id, value in contacts.items():
                    ApiCall.api_calls['Address'](self.headers, random_gen.basic_address(c_id))
                    ApiCall.api_calls['Internet'](self.headers, random_gen.basic_internet(
                        c_id, value['Firstname'], value['Lastname']))
                    ApiCall.api_calls['Phone'](self.headers, random_gen.basic_phone(c_id))
        elif self.environment == 'prod':
            if self.data_type == 'Contacts':
                contacts = {}
                client_data = []
                mccl_data = ApiCall.prod_api_calls['MCCL'](self.headers)
                csl_data = ApiCall.prod_api_calls['CSL'](self.headers)
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
                    print(client)
                    contacts[ApiCall.prod_api_calls[self.data_type](
                        self.headers, client
                    )] = client
                # Loop that addes in Phone, Address, and Email data for each contact
                for c_id, value in contacts.iteritems():
                    ApiCall.prod_api_calls['Address'](self.headers, random_gen.basic_address(c_id))
                    ApiCall.prod_api_calls['Internet'](self.headers, random_gen.basic_internet(
                        c_id, value['Firstname'], value['Lastname']))
                    ApiCall.prod_api_calls['Phone'](self.headers, random_gen.basic_phone(c_id))
            elif self.data_type == 'Notes':
                for i in range(self.volume):
                    ApiCall.prod_api_calls['Notes'](self.headers)



data_type = [
    inquirer.List('data_type',
                  message='Select data type to seed',
                  choices=['Contacts', 'Accounts',
                           'Calendar Activities', 'Opportunities', 'Seminars'],
                  ),
]

env = [
    inquirer.List('env',
                  message='Selected Environment',
                  choices=['prod','dev'],
                  ),
]


# Boilerplate basic opton
# Second option which lists all fields per data_type as checklist for fields to be populated

# Input setup
rt_un = input('Redtail Username: ')
rt_pw = getpass.getpass('Redtail Password: ')
data_type = inquirer.prompt(data_type)['data_type']
data_volume = input_check.get_int('How many?: ')
environment = inquirer.prompt(env)['env']
if environment == 'dev':
    headers = redtail.headers(rt_un, rt_pw)
else:
    headers = prod_redtail.headers(rt_un, rt_pw)

api_call = ApiCall(data_type, headers, data_volume, environment)
api_call.request()