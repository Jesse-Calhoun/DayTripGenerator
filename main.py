import random

destinations = ['New York City', 'Dallas', 'Washington D.C.', 'Philadelphia']
restaurants = ['Steakhouse', 'Mcdonalds', 'Del Taco', 'Hibachi']
forms_of_entertainment = ['NFL game', 'Comedy Show', 'Concert', 'Nightclub']
modes_of_transportation = ['Uber', 'Limo Service', 'Sports Car', 'Bus']

def run_day_trip_generator():
    results = day_trip_generator()
    print(results)
    results = satisfied(results)
    print(results)
    satisfied(results)

def day_trip_generator():
    destination = random.choice(destinations)
    restaraunt = random.choice(restaurants)
    form_of_entertainment = random.choice(forms_of_entertainment)
    mode_of_transport = random.choice(modes_of_transportation)
    return [destination, restaraunt, form_of_entertainment, mode_of_transport]

def satisfied(list_of_events):
    print()
    response = input('Are you satisfied with this trip? y/n ') 
    print()
    while response == 'n':
        change_request = input('What would you like to change about your trip? Type done when finished. ')
        if change_request == 'destination':
            list_of_events[0] = random.choice(destinations)
        elif change_request == 'restaurant':
            list_of_events[1] = random.choice(restaurants)
        elif change_request == 'form of entertainment':
            list_of_events[2] = random.choice(forms_of_entertainment)
        elif change_request == 'mode of transport':
            list_of_events[3] = random.choice(modes_of_transportation)
        elif change_request == 'done':
            return list_of_events
        print(list_of_events)
    else:
        print(f'''Here's your final trip!
 {list_of_events}''')    

run_day_trip_generator()



