from data import pantry_items

# THE fromkeys() METHOD: -----------------------------------

# fromkeys() is method that creates a new dictionary with keys from a provided iterable and assigns each key a
# default value. is useful when you want to initialize a dictionary with a predefined set of keys, all having the
# same initial value. It expects two arguments, the iterable and the default value. If the default value is not
# specified `None` will be assigned as a default value
new_dict = dict.fromkeys(pantry_items)  # With no specified default value.
second_dict = dict.fromkeys(pantry_items, 0)  # 0 will be the default value for every key
print(new_dict)
print(second_dict)
