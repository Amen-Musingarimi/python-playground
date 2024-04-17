from data import d

# The keys() method --------------------------
# The keys() method returns a view object that displays a list of all the keys in the dictionary
# This method doesn't take any parameters. It simply returns a view object that provides a
# dynamic view of the dictionary's keys. A view object behaves like a set, meaning that you can iterate over it and
# perform set operations such as membership tests

keys = d.keys()
print(keys)
