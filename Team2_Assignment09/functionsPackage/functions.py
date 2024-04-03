# Name: TJ Harrington, Ben Klein, Ryan Wilkins
# email: kleinbw@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/04/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a group assignment and it has us call an API and display the API information.
# Brief Description of what this module does: This file define the search_state_by_name function which will return the state.




#Here we define our function to search for the state name
def search_state_by_name(states_data, state_name):
    for state in states_data:
        if state['name'] == state_name:
            return state
    return None

