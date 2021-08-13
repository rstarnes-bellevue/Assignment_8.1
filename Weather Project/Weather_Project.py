import requests
import json
import time
import os

#Validates location and returns a response (if successful) or error (if unsuccessful)
def GetWeather (location, key):
    connection = False

    #Repeats while an invalid location is detected
    while connection == False:
        #Checks to make sure connection is valid
        try:
            #Checks for zip code location
            if location.isdigit():
                response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?zip={location},US&units=imperial&appid={key}")

                #Produces error if location isn't found
                if response.status_code == 400 or response.status_code == 404:
                    print("Location not found. Please enter a valid city or zip code.")
                    location = input("City/Zip code: ")

                #Stores response into a dictionary and passes it to function that formats the returned data
                else:
                    connection = True
                    #JSONFormat(response.json())
                    print("Connection successful. Displaying the 5 day/4 hour forecast.")
                    time.sleep(2)

                    response_dict = response.json()
                    #print(response_dict.keys())
                    OutputResponse(response_dict)
            #Checks for city location
            else:
                response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={location}&units=imperial&appid={key}")

                #Produces error if location isn't found
                if response.status_code == 400 or response.status_code == 404:
                    print("Location not found. Please enter a valid city or zip code.")
                    location = input("City/Zip code: ")

                #Stores response into a dictionary and passes it to function that formats the returned data
                else:
                    connection = True
                    #JSONFormat(response.json())
                    print("Connection successful. Displaying the 5 day/4 hour forecast.")
                    time.sleep(2)

                    response_dict = response.json()
                    #print(response_dict.keys())
                    OutputResponse(response_dict)
        #Produces an error if connection cannot be established
        except:
            print("Connection unsuccessful, location invalid or network unavailable. Please try again.")
            location = input("City/Zip code: ")

#Functio that displays the output based on location given
def OutputResponse (response_dict):
    forecast = response_dict['list']

    #print(f"Lists: {len(forecast)}")
    #forecast = forecast[0]

    for key in forecast:

        weather = key['weather']

        print(f"""
******************************************
*   Date:           {key['dt_txt']}  *
******************************************
    Temperature:    {key['main']['temp']} degrees      
    Weather:        {weather[0]['description'].capitalize()}          
""")
        #"Pictures" of weather conditions
        if weather[0]['main'] == 'Clouds':
            print("""
                 _
               (   )  ___
             _(     )(   )
           (     (        )
            (___(__________)
            """)
        elif weather[0]['main'] == 'Clear':
            print(f"""
                \ ___ /
             __  /   \  __
                 \___/
                /     \\
                  
            """)
        elif weather[0]['main'] == 'Rain':
            print("""
                _______
              _(       )
            (     (     )
             (___(________)
             /   /   /   /
              /   /   / 
            """)
        time.sleep(0.5)

    #JSONFormat(forecast)

    userInput = ""
    while userInput == "":
        print("\nPress [R] to enter a new location or press [Q] to quit.", end=" ")
        userInput = input()

        if userInput == "r" or userInput == "R":
            main()
        elif userInput == "q" or userInput == "Q":
            print("\nThank you for using PyWeather!\n")
            break
        else:
            print("Input not valid, please try again.")
            userInput = ""
    

#Takes API data and makes it more readable
#Mainly for testing/verification
def JSONFormat (forecast):
    text = json.dumps(forecast, sort_keys=True, indent=4)
    print(text)


#Program start/main function
def main():
    print("Welcome to PyWeather! Please enter either a city or zip code for the current forecast.\n")

    #Asks for location and passes it into GetWeather function
    location = input("City/Zip code: ")

    #Verify current directory
    #print(os.listdir())
    with open('Weather Project\key.txt') as file_object:
        key = file_object.read()
    #Calls GetWeather function and passes location from user input and API key from file
    GetWeather(location, key)

#Calls main function
if __name__ == "__main__":
    main()

