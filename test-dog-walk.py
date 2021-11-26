# created by Harry David Wills 26.11.2021
# A simple script that will gather the weather of your current city, and let you know if it is safe to walk your dog.

import requests
import geocoder
import time
import os

g = geocoder.ip('me')
def checkDogWalk(location):
    api_key = 'c7ccdc0ffb08653474936a54a25a7761'
    while True:
        if location == '1':
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}' .format(g.city, api_key)
        elif location == '2':
            city = input("Please enter name of the city you would like to check: ")
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}' .format(city, api_key)
        response = requests.get(weather_url)
        weather_data = response.json()
        if weather_data["cod"] == 200:
            kelvin = 273.15
            temp = int(weather_data['main']['temp'] - kelvin)
            if temp >= 24:
                print("\nIt is too hot to walk your dog today as the tempurature is currently {}°C." .format(temp))
            elif temp >=20 and temp <= 23:
                print("\nIt is okay to walk your dog, but be more cautious as the tempurature is currently {}°C." .format(temp))
            else:
                print("\nIt is safe to walk your dog today as the tempurature is currently {}°C." .format(temp))
            break
        elif weather_data['cod'] == '404':
            print("\nInvalid city. Please try again.")

def main():
    while True:
        os.system("clear")
        place = input("Would you like to check to walk your dog in your current location ({}), or another location?\n\nEnter 1 for current location, or 2 for own choice: " .format(g.city))
        if place == '1' or place == '2':
            checkDogWalk(place)
            time.sleep(2)
            while True:
                cont = input("Would you like to run the program again? (Y/N): ")
                if cont.upper() == "Y" or cont.upper() == "N":
                    os.system("clear")
                    break
                else:
                    print("Invalid input. Please try again.")
            if cont == "N" or cont == "n":
                    break
        else:
            print("Invalid entry, please try again.")
            time.sleep(2)

if __name__ == '__main__':
    main()