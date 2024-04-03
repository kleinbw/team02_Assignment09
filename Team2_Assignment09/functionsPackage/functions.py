def search_state_by_name(states_data, state_name):
    for state in states_data:
        if state['name'] == state_name:
            return state
    return None

