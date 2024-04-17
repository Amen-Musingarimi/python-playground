d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# THE fromkeys() METHOD: ----------------------------------- fromkeys() is method that creates a new dictionary with
# keys from a provided iterable and assigns each key a default value. is useful when you want to initialize a
# dictionary with a predefined set of keys, all having the same initial value. It expects two arguments,
# the iterable and the default value. If the default value is not specified `None` will be assigned as a default value
new_dict = dict.fromkeys(pantry_items)
print(new_dict)
