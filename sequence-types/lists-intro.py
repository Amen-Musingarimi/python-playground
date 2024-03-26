computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

# Looping through the list
for part in computer_parts:
  print(part)

# Indexing the list
print("-" * 60)
print(computer_parts[2])

# Slicing the list. It produces another list in return
print("-" * 60)
print(computer_parts[0:3]) #Returns first 3 items in a list
print(computer_parts[-1]) #Returns the last item in a list