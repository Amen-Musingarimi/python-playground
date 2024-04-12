vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4'
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get('er5')
print(learner)

# Adding items to a dictionary
vehicles['starfighter'] = 'Lockheed F-104'
vehicles['learjet'] = 'Bombardier Learjet 75'
vehicles['toy'] = 'Glider'
print(vehicles)

# Changing item values in a dictionary
# Updating the Virago
vehicles['virago'] = 'Yamaha XV535'

# Iterating over a dictionary
for key in vehicles:
    print(key, vehicles[key], sep=', ')

print("*" * 60)

for key, value in vehicles.items():
    print(key, value, sep=', ')
