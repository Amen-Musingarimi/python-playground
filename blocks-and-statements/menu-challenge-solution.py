print("Please choose your option from the list below:")
print("1. \tLearn Python")
print("2. \tLearn Java")
print("3. \tGo Swimming")
print("4. \tHave Dinner")
print("5. \tGo To Bed")
print("0. \tExit")

while True:
  choice = input()

  if choice == "0":
    break
  elif choice in "12345":
    print("You chose option {}.".format(choice))