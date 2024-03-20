# providing a start and end value
for i in range(1, 6):
  print("i is now {}".format(i)) 

print("*" * 60)

# providing an end value. The start value defaults to zero
for i in range(5):
  print("i is now {}".format(i)) 

print("*" * 60)

# providing step value in a range. Counting upwards
for i in range(0, 10, 2):
  print("i is now {}".format(i)) 

print("*" * 60)

# providing step value in a range. Counting backwards
for i in range(10, 0, -2):
  print("i is now {}".format(i)) 