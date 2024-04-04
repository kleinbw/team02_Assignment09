# Name: TJ Harrington, Ben Klein, Ryan Wilkins
# email: kleinbw@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/04/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a group assignment and it has us call an API and display the API information.
# Brief Description of what this module does: This module calls the API and uses the search_state_by_name function to create a new dictionary which we then print






import json
import requests

from functionsPackage.functions import*

if __name__ == "__main__":
    url = "https://us-states.p.rapidapi.com/basic"
    #Here is the API Key
    headers = {
        "X-RapidAPI-Key": "e354a39aecmsh2c967112f19af0dp10dd88jsn9435c59da7e1",
        "X-RapidAPI-Host": "us-states.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        states_data = response.json()
        state_name = input("Enter the name of the state you want to search for: ")
        #State Info is the dictionary for which the data is being stored
        state_info = search_state_by_name(states_data, state_name)
        #Here we will be printing the information in state_info
        if state_info:
            print("State found:")
            print("Name:", state_info["name"])
            state_data_select = input("Would you like to know state info, capital info, or population info: ")
            if state_data_select == "state info":
                print("Postal Code:", state_info["postal"])
                print("Capital:", state_info["capital"]["name"])
                print("Total Population:", state_info["population"]["total"])
            elif state_data_select == "capital info":
                print("Capital:", state_info["capital"]["name"])
                print("Capital Latitude:", state_info["capital"]["latitude"])
                print("Capital Longitude:", state_info["capital"]["longitude"])
            elif state_data_select == "population info":
                print("Population Density (per square km):", state_info["population"]["density_km"])
                print("Total Population:", state_info["population"]["total"])
        else:
            print("State not found.")
    else:
        print("Failed to fetch data from the API.")
