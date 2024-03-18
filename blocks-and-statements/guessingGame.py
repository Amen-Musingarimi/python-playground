answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
  print("Your guess is too low. Please guess higher.")
elif guess > answer:
  print("Your guess is too high. Please guess lower.")
else:
  print("You got it first time.")