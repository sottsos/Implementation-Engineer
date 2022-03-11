"""
RapidSOS grants you a nonexclusive copyright license to use this programming code example (subject to your explicit agreement to RapidSOS Terms of Service) from which you can generate similar function tailored to your own specific needs.  All sample code is provided by RapidSOS for illustrative purposes only. These examples have not been thoroughly tested under all conditions. RapidSOS, therefore, cannot guarantee or imply reliability, serviceability, or function of these programs.
"""

import requests

url = "https://api-sandbox.rapidsos.com/oauth/token"
payload = {
    "client_id": "",
    "client_secret": "",
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
    "callflow": "mojio_v1",
    "variables": {
        "webhook_url": "https://webhook.site/a3989873-a48a-4fd2-a988-9503919e7f28",
        "vehicle": {
            "color": "red",
            "make": "Honda",
            "model": "Civic",
            "year": "1993",
            "plate": "DE43E",
            "state": "NY",
            "vin": "Ckee32",
            "phone_number_device": "+16316642452"
        },
        "company": "Mojio",
        "company_id": "a7af9339-f2d2-4820-b635-aeb61fd64fe8",
        "user": {
            "full_name": "Steven Ott",
            "phone_number": "+16316642452",
            "account_id": "DF453"
        },
        "ivr_info_user": {
            "cancellation_key": "1",
            "confirmation_key": "2",
            "greeting_script": "Hey ${user.full_name} we heard that you may be in an accident. Press 1 to cancel press 2 to be connected to 9-1-1",
            "confirm_script": "Transfering you to 9-1-1",
            "decline_script": "You have declined. If you need further assistance please call 9-1-1",
            "no_response_script": "Hey",
            "monitoring_script": "Hey",
            "timeout": 15
        },
        "ivr_info_device": {
            "cancellation_key": "1",
            "confirmation_key": "2",
            "greeting_script": "Hey ",
            "confirm_script": "Hey",
            "decline_script": "Hey",
            "no_response_script": "Hey",
            "error_script": "Hey",
            "timeout": 14
        },
        "event_info": {
            "latitude": 29.834462,
            "longitude": -95.5641818,
            "uncertainty": 1,
            "time": 1645589467,
            "severity": 1
        }
    }
}
response = requests.post(url, headers=headers, json=payload)
print(response.text)
