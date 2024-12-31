from venv import create

import requests
from twilio.rest import Client

# AY42E9WB4WDLHY4TBSCKUHNQ

my_key = "f69a86b76e2af2b93027a5e876aec6bb"
end_point = "https://api.openweathermap.org/data/2.5/forecast"
acc_sid = "AC90b7cea5299b0c28637dc2eb23e1be23"
acc_token = "01cf4c9cbeba6f58eac9a98141755731"

weather_para = {
    "lat" : 30.283937,
    "lon" : 57.083363,
    "appid": my_key,

}

response = requests.get(end_point, params=weather_para)
data = response.json()
# for particular id: -
# print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(acc_sid, acc_token)
    message = client.messages.create(
        messaging_service_sid='MG5a11d04b4f562027f61f61f0e15968ab',
        body='Its going to rain today. Take your umbrella!!',
        to='+917348187026'
    )
