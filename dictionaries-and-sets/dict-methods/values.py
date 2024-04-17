from data import d

# The values() method is a built-in dictionary method that returns a view object that displays a list of all the
# values in the dictionary.
# This method doesn't take any parameters. It simply returns a view object that provides a dynamic view of the
# dictionary's values. Similar to the keys() method, a view object behaves like a set, meaning that you can iterate
# over it and perform set operations such as membership tests.


v = d.values()
print(v)

print("four" in v)
print("eleven" in v)
