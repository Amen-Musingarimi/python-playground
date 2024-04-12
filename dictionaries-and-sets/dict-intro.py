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

# Deleting items from a dictionary
del vehicles['starfighter']

# Deleting items from a dictionary using the pop() method. The pop method deletes an item from the dictionary but it
# will return an error if you try and delete a non-existing item. To avoid the error we have to pop() method a
# default value e.g vehicles.pop('f1', None).
vehicles.pop('f1', None)
# Setting a default message when the item does not exist
vehicles.pop('subaru', 'not present')

# Iterating over a dictionary
for key in vehicles:
    print(key, vehicles[key], sep=', ')

print("*" * 60)

for key, value in vehicles.items():
    print(key, value, sep=', ')
