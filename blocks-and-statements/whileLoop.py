# The while loop continues to loop as long as the condition is true and stops when the condition becomes false it stops looping.
i = 0

while i < 10:
  print("i is now {}.".format(i))
  i += 1 

available_exits = ["north", "south", "east", "west"]

choosen_exit = ""

while choosen_exit not in available_exits:
  choosen_exit = input("Please choose a direction: ")
  if choosen_exit == "quit":
    print("Game Over!")
    break

print("Aren't you glad you got out of there?")