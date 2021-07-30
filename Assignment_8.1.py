import requests
import json

#Validates location and returns a response (if successful) or error (if unsuccessful)
def GetWeather (location):
    connection = False

    #Repeats while an invalid location is detected
    while connection == False:
        try:
            #Checks for zip code location
            if location.isdigit():
                response = requests.get("http://api.openweathermap.org/data/2.5/forecast?zip={},US&units=imperial&appid=d56a5ad93c4f731841282b93a76c5a54".format(location))

                #Produces error if location isn't found
                if response.status_code == 400 or response.status_code == 404:
                    print("Location not found. Please enter a valid city or zip code.")
                    location = input("City/Zip code: ")

                #Stores response into a dictionary and passes it to function that formats the returned data
                else:
                    connection = True
                    #JSONFormat(response.json())
                    response_dict = response.json()
                    print(response_dict.keys())
                    FormatResponse(response_dict)
            #Checks for city location
            else:
                response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=d56a5ad93c4f731841282b93a76c5a54".format(location))

                #Produces error if location isn't found
                if response.status_code == 400 or response.status_code == 404:
                    print("Location not found. Please enter a valid city or zip code.")
                    location = input("City/Zip code: ")

                #Stores response into a dictionary and passes it to function that formats the returned data
                else:
                    connection = True
                    #JSONFormat(response.json())
                    response_dict = response.json()
                    print(response_dict.keys())
                    FormatResponse(response_dict)
        except:
            print("Connection unsuccessful, location invalid or network unavailable.")
            location = input("City/Zip code: ")

def FormatResponse (response_dict):
    forecast = response_dict['list']
    print(f"Lists: {len(forecast)}")

    #forecast = forecast[0]

    for key in forecast:

        weather = key['weather']

        print(f"""
    Date:           {key['dt_txt']}
    Temperature:    {key['main']['temp']} degrees
    Weather:        {weather[0]['description'].capitalize()}
    """)
    #JSONFormat(forecast)
    #print(f"Keys: {len(forecast)}")
    #for key in forecast:
    #    print(key)


def JSONFormat (forecast):
    text = json.dumps(forecast, sort_keys=True, indent=4)
    print(text)


#Program start
print("Welcome to PyWeather! Please enter either a city or zip code for the current forecast.\n")

#Asks for location and passes it into GetWeather function
location = input("City/Zip code: ")
GetWeather(location)

