computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]

print(computer_parts)

print("---------------------REPLACING LIST ITEMS USING INDEXING-----------------------")
computer_parts[3] = "trackball"
print(computer_parts)

print("---------------------REPLACING LIST ITEMS USING SLICING-----------------------")
print(computer_parts[3:]) # Prints the list item from index position 3 to the end
computer_parts[3:] = ["mouse"] # Replaces all items in the list from the index 3 up to the end with one list item "mouse"
print(computer_parts)