"""
RapidSOS grants you a nonexclusive copyright license to use this programming code example (subject to your explicit agreement to RapidSOS Terms of Service) from which you can generate similar function tailored to your own specific needs.  All sample code is provided by RapidSOS for illustrative purposes only. These examples have not been thoroughly tested under all conditions. RapidSOS, therefore, cannot guarantee or imply reliability, serviceability, or function of these programs.
"""
import requests
url = "https://api-sandbox.rapidsos.com/oauth/token"
payload = {
    "client_id": "[CONSUMER_KEY]",
    "client_secret": "[CONSUMER_SECRET]",
    "grant_type": "client_credentials"
}
response = requests.post(url, data=payload)
data = response.json()
access_token = data['access_token']
url = "https://api-sandbox.rapidsos.com/v1/rem/trigger"
headers = {
    "Authorization": "Bearer {access_token}".format(access_token=access_token)
}
payload = {
    "callflow": "Everbridge Demo",
    "variables": {
        "everbridge_profile": [
            {
                "firstName": "John",
                "lastName": "Doe",
                "source": "",
                "householdId": "134S3",
                "id": "3454d3",
                "confidence": "1",
                "address": {
                    "streetAddress": "Test way 123",
                    "city": "Salem",
                    "county": "Washington",
                    "state": "NY",
                    "postalCode": "11101"
                },
                "gis": {
                    "lon": "",
                    "lat": "",
                },
                "phones": [
                    {
                        "phoneType": "Cell",
                        "carrier": "Verizon",
                        "number": ""
                    }
                ],
                "householdMembers": [
                    {
                        "id": "343",
                        "firstName": "Jane",
                        "lastName": "Doe",
                        "phones": [
                            {
                                "phoneType": "Cell",
                                "carrier": "Verizon",
                                "number": ""
                            }
                        ],
                    }
                ],
            }
        ]
    }       
}
response = requests.post(url, headers=headers, json=payload)
print(response.text)