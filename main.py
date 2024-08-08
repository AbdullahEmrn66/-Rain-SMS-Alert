import requests
from twilio.rest import Client
import os

parameters = {
    "lat": "31.583688",
    "lon": "74.308509",
    "appid": "318bc5e4f7e480e162084c81b244be74",
    "cnt": "4"
}
account_sid = os.environ["AC6d781e7d0f4175c23ec0c787cca451d1"]
auth_token = os.environ["59ea997dcc80cfd33db3661a4f4bb992"]

OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(OWN_endpoint, params=parameters)
data = response.json()["list"]
will_rain = False
for hour in data:
    if hour["weather"][0]["id"] < 800:
        will_rain = True
    print(hour["weather"][0]["id"])

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="+12513254331",
        to="+923035987180",
    )

print("check your messages")
c = input()
