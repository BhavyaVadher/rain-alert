
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "3fd5fa2d4468650cf1cb75cb71e20a60"
account_sid = "ACd55ae8e7eb2fff7d7e2fc38ea8ed73c6"
auth_token = "986ffeed5b92d191673b171a82f9ef08"

weather_params = {
    "lat": "22.310050",
    "lon": "70.739680",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
weather_slice = weather_data['weather'][0]["main"]
# print(weather_slice)


if weather_slice=="Rain":
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+13023435251",
        to="+91 79901 17767"
    )
        
    print(message.status)
    
elif weather_slice=="Clouds":
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's cloudy weather outside of your home. Don't forgot to take sunglasses😎 with you !",
        from_="+13023435251",
        to="+91 79901 17767"
    )
        
    print(message.status)

