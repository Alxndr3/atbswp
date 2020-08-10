#! python3
# random_quiz_generator.py - Creates quizzes with questions and answers in random order, along with the answer key.
import random

# The random_quiz_generator data. Keys are the states and values are their capitals
states = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
          'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
          'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
          'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
          'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
          'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
          'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
          'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
          'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
          'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
          'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
          'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
          'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate 35 random_quiz_generator files.
state = list()
capital = list()
capital_list = list()
for quiz_num in range(35):
    for x, y in states.items():
        state.append(x)
        capital.append(y)
    state_ = random.choice(state)
    capital_list.append(states[state_])
    for r in range(3):
        capital_list.append(random.choice(capital))
    print('What is the capital of: ' + state_)
    random.shuffle(capital_list)
    print(f'a) {capital_list[0]} b) {capital_list[1]} c) {capital_list[2]} d) {capital_list[3]}')
    answer = str(input('> ')).title().strip()
    print(states[state_])
    if answer == states[state_]:
        print('Nice!')
    else:
        print("Your're Doomed!")
    print()
    capital_list.clear()

