import random

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#(10  points): As a user, I want to display my completed trip in the console

#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

destinations = ['New York City', 'Dallas', 'Washington D.C.', 'Philadelphia']
restaurants = ['Steakhouse', 'Mcdonalds', 'Del Taco', 'Hibachi']
forms_of_entertainment = ['NFL game', 'Comedy Show', 'Concert', 'Nightclub']
modes_of_transportation = ['Uber', 'Limo Service', 'Sports Car', 'Bus']
list_of_events = [destinations, restaurants, forms_of_entertainment, modes_of_transportation]

def run_day_trip_generator():
    city = random.choice(destinations)
    restaraunt = random.choice(restaurants)
    form_of_entertainment = random.choice(forms_of_entertainment)
    mode_of_transport = random.choice(modes_of_transportation)
    return (f'''Here's your trip!
City: {city}
Restaurant: {restaraunt}
Form of entertainment: {form_of_entertainment}
Mode of Transport: {mode_of_transport}''')

#run_day_trip_generator()

current_trip = run_day_trip_generator()

print(current_trip)

#def satisfied(current_trip, list_of_events):
#    if current_trip == 
