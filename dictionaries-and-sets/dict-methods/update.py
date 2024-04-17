from data import d

# The update() method -----------------------------------
# The update() is used to update the contents of a dictionary with elements from another dictionary or from an
# iterable of key-value pairs.

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three"
}

print("-----------The original 'd' dict--------------")
print(d)

print("-----------The updated 'd' dict--------------")
d.update(d2)
print(d)

print("-----------Iterate over the newly updated 'd' dict--------------")
for key, value in d.items():
    print(f"{key}: {value}")
