import requests
from datetime import datetime


location = input("Enter your City Name : ")
complete_link_api = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=7e0bff74867d9a734d58da9510717bf5&units=metric"

api_link = requests.get(complete_link_api)
api_data = api_link.json()


if api_data["cod"] == "404":
    print(f"Invalid City Name : {location}, Please enter valid City Name")
else:
    temp_city = api_data["main"]["temp"]
    weather_desc = api_data["weather"][0]["description"]
    hmdt = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    data_time = datetime.now()


print("********************************")
print(f"Weather State  for - {location.upper()}")
print("********************************")

print(f"Current temperature is : {temp_city:.2f} deg C")
print(f"Current weather dec    : {weather_desc}")
print(f"Current humidity       : {hmdt} %")
print(f"Current wind_spd       : {wind_spd} kmph")