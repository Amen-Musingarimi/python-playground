import random

highest = 10
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0 # Initialize to any number that doesn't equal the answer.

while guess != answer:
  guess = int(input())

  if guess == answer:
      print("Well done, you guessed it right.")
  else:
      if guess < answer:
        print("Your guess is too low. Please guess higher.")
      else:
        print("Your guess is too high. Please guess lower.")
   
