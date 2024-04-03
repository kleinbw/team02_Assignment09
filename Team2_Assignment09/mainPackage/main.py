import json
import requests

from functionsPackage.functions import*

if __name__ == "__main__":
    url = "https://us-states.p.rapidapi.com/basic"
    
    headers = {
        "X-RapidAPI-Key": "e354a39aecmsh2c967112f19af0dp10dd88jsn9435c59da7e1",
        "X-RapidAPI-Host": "us-states.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        states_data = response.json()
        state_name = input("Enter the name of the state you want to search for: ")
        state_info = search_state_by_name(states_data, state_name)
        if state_info:
            print("State found:")
            print("Name:", state_info["name"])
            print("Postal Code:", state_info["postal"])
            print("Capital:", state_info["capital"]["name"])
            print("Capital Latitude:", state_info["capital"]["latitude"])
            print("Capital Longitude:", state_info["capital"]["longitude"])
            print("Population Density (per square km):", state_info["population"]["density_km"])
            print("Total Population:", state_info["population"]["total"])
        else:
            print("State not found.")
    else:
        print("Failed to fetch data from the API.")
