import requests

#def GetWeather (location):
 #   try:
  #      response = pro.openweathermap.org/data/2.5/forecast/hourly?zip=77706,US&appid=d56a5ad93c4f731841282b93a76c5a54







print("Welcome to PyWeather! Please enter either a city or zip code for the current forecast.\n")

#location = input("City/Zip code: ")

response = requests.get("https://api.openweathermap.org/data/2.5/forecast/hourly?zip=77706,US&appid=d56a5ad93c4f731841282b93a76c5a54")

print(response.json())