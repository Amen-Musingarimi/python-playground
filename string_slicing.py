parrot = "Norwegian Blue"

# Slice takes a range up to, but not including the value of a range
print('-----String Slicing------')
print(parrot[0:6]) # Norweg
print(parrot[3: 5])
print(parrot[0:9]) #Norwegian
print(parrot[:9]) #Norwegian
print(parrot[10:]) #Blue

print(parrot[:6] + parrot[6:])  
print(parrot[:])

print("------Slicing using negative indexing------")
print(parrot[-4:2]) #This doesn't print anything because slice can't go backwards from the starting value(index)
print(parrot[-4: -2])