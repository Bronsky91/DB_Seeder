import requests
import json
import base64

api_key = 'DA353598-8FF5-4DBF-B153-8B2EE3A22D3E'


def headers(rt_un, rt_pw):
    encoded_string = '{}:{}:{}'.format(api_key, rt_un, rt_pw)
    encoded_string = encoded_string.encode('ascii')
    headers = {
        'content-type': 'application/json', 'authorization': 'Basic ' +
        base64.b64encode(encoded_string).decode("utf-8") 
    }
    return headers


def get_user(rt_un, rt_pw):
    r = requests.get(
        'https://api2.redtailtechnology.com/crm/v1/rest/authentication', headers=headers(rt_un, rt_pw))
    rt_user_id = int()
    if r.status_code == 200:
        auth = json.loads(r.text)
        rt_user_id = int(auth['UserID'])
    return rt_user_id


def create_act(headers, request_body):
    request_body = {
        'Subject': subject,
        'StartDate': '/Date({})/'.format(date),
        'EndDate': '/Date({})/'.format(date),
    }
    r = requests.put(
        'https://api2.redtailtechnology.com/crm/v1/rest/calendar/activities/0',
        headers=headers,
        json=request_body
    )
    return_body = json.loads(r.text)
    return return_body['RecID']


def create_contact(headers, request_body):
    r = requests.put(
        'https://api2.redtailtechnology.com/crm/v1/rest/contacts/0',
        headers=headers,
        json=request_body
    )
    contact = json.loads(r.text)
    c_id = contact['ClientID']
    print(c_id)
    return c_id


def create_address(headers, request_body):
    r = requests.put(
        'https://api2.redtailtechnology.com/crm/v1/rest/contacts/{}/addresses/0'.format(request_body['ClientID']),
        headers=headers,
        json=request_body
    )
    print(request_body)
    return r.status_code


def create_phone(headers, request_body):
    r = requests.put(
        'https://api2.redtailtechnology.com/crm/v1/rest/contacts/{}/phones/0'.format(request_body['ClientID']),
        headers=headers,
        json=request_body
    )
    print(request_body)
    return r.status_code


def create_internet(headers, request_body):
    r = requests.put(
        'https://api2.redtailtechnology.com/crm/v1/rest/contacts/{}/internets/0'.format(request_body['ClientID']),
        headers=headers,
        json=request_body
    )
    print(request_body)
    return r.status_code

def mccl_codes(headers):
    r = requests.get(
        'https://api2.redtailtechnology.com/crm/v1/rest/settings/mccl',
        headers=headers
    )
    return_body = json.loads(r.text)
    return return_body

def csl_codes(headers):
    r = requests.get(
        'https://api2.redtailtechnology.com/crm/v1/rest/settings/csl',
        headers=headers
    )
    return_body = json.loads(r.text)
    return return_body


def create_note(headers):
    request_body = {
        "ClientID":8,
        "Note":"String content"
    }
    r = requests.put(
        'https://api2.redtailtechnology.com/crm/v1/rest/contacts/8/notes/0',
        headers=headers,
        json=request_body
    )


def create_seminar(headers, request_body):
    pass


def create_account(headers, request_body):
    pass


def create_opp(headers, request_body):
    pass
