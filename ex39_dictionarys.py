states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'

    }

cities = {
    'CA':'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'

}

cities['NY'] = 'New york'
cities['OR'] = 'Portland'


print ('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])


print('-' * 10)
print("Michigan's abbrevation is:", states['Michigan'])
print("Florida's abbrevations is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']]) # using key from other dict to get out value
print("Florida has ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

city = cities.get ('TX','Does not exist')
print(f"The city for the state 'TX' is: {city}")