# Demostrate that enumerate() returns tuples of the character and its index value.
print("------------------------Return tuples-------------------------")
for char in enumerate("abcdefgh"):
  print(char)

print("------------------------Return unpacked tuples-------------------------")
# Demostrate unpacking a tuple for the index and tuple item to be returned seperately
for index, character in enumerate("abcdefgh"):
  print(index, character)