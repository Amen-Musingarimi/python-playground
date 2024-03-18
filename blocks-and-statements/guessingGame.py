answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
  print("Your guess is too low. Please guess higher.")
  guess = int(input())
  if guess == answer:
    print("Well done, you guessed it right.")
elif guess > answer:
  print("Your guess is too high. Please guess lower.")
  guess = int(input())
  if guess == answer:
    print("Well done, you guessed it right.")
else:
  print("You got it first time.")