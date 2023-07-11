import requests
import json
import os
from urllib.parse import urlparse

# Token path
path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','credentials','token.json'))

def createPersonalization(information):

    with open(path) as f:
        data = json.load(f)
        token = data['Bearer_token']

    header = { "Authorization": f"Bearer {token}"}
    url= "https://careers.turtl.co/api/v1/docs"
    CreatePersonalization_Endpointurl = "https://careers.turtl.co/api/v1/personalizations"

    try:
        response = requests.get(url, headers=header) # List all docs
        response = response.text
        inJsonFormat = json.loads(response)

        for people in inJsonFormat['docs']:
            if "Saurabh" in people['title']: # Get my doc ID
                docID= people['id']
                break
    
    except Exception as error:
        print("There was an error")

    # Loop through the objects within "information" object variable and make a POST request
    # by sending all the object information dynamically within "payload"
    for item in information:

        itemDomain = urlparse(item[" logo"]).netloc

        payload = {
            "bearer_authorization": f"Authorization: Bearer {token}",
            "docId": "64a7e93c109059c1be4e21be",
            "docUrl": "https://careers.turtl.co/story/64a7e93c109059c1be4e21be",
            "title": "My Personalizations",
            "fields": {
                "name": f"{item['name']}",
                "company": f"{item[' company']}",
                "sector": f"{item[' sector']}",
                "logo-domain": f'{itemDomain}',
            }
        }

        try:
            response = requests.post(url=CreatePersonalization_Endpointurl, json=payload, headers=header)

            if response.status_code == 201:
                print(f"Personalization created for {item['name']}")
            else:
                print("There was an error")
        
        except Exception as error:
            print(f"There was an error: {error}")
        

    return "Success"