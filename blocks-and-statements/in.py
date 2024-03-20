parrot = "Norwegian Blue"

letter = input("Please enter any character: ")

if letter in parrot:
  print("{} is in {}".format(letter, parrot))
else:
  print("I don't need that letter.")