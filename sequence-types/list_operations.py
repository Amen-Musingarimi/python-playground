computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]

print(computer_parts)

print("---------------------REPLACING LIST ITEMS USING INDEXING-----------------------")
computer_parts[3] = "trackball"
print(computer_parts)

print("---------------------REPLACING LIST ITEMS USING SLICING-----------------------")
print(computer_parts[3:]) # Prints the list item from index position 3 to the end
computer_parts[3:] = ["mouse"] # Replaces all items in the list from the index 3 up to the end with one list item "mouse"
print(computer_parts)

print("---------------------DELETING LIST ITEMS-----------------------")
data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
print(data)
del data[0:2] # Deletes the first 2 items of the list
print(data)
del data[13:] # Deletes the last 2 items of the list
print(data)

min_valid = 120
max_valid = 170

# Note that this code will not work as the index changes as each item is deleted, meaning some items will not be deleted
for index, value in enumerate(data):
  if (value < min_valid) or (value > max_valid):
    del data[index]

print(data)