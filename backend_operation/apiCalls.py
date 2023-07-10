import requests
import json
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','credentials','token.json'))

def createPersonalization(information):

    with open(path) as f:
        data = json.load(f)
        token = data['Bearer_token']

    header = { "Authorization": f"Bearer {token}"}
    url = "https://careers.turtl.co/api/v1/personalizations"

    try:
        response = requests.get(url, headers=header)
        print("Somthing")
    
    except Exception as error:
        print("There was an error")

    return