name = input("What is your name?: ")

age = int(input("How old are you?: "))

if age >= 18 and age <= 30:
  print("{}, welcome to the 18-30 holiday.".format(name))
else:
  print("You are not authorized to go for the 18-30 holiday.")