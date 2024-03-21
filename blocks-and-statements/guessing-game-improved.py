import random

highest = 10
chances = 5
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0 # Initialize to any number that doesn't equal the answer.

while guess != answer:
  guess = int(input())

  if guess == 0:
    break

  if guess == answer:
      print("Well done, you guessed it right.")
  else:
      if guess < answer:
        print("Your guess is too low. Please guess higher.")
        chances = chances - 1
        print("{} remaining chances.".format(chances))
        if chances < 1:
           print("Game Over! You lost the game.")
           break
      else:
        print("Your guess is too high. Please guess lower.")
        chances = chances - 1
        print("{} remaining chances.".format(chances))
        if chances < 1:
           print("Game Over! You lost the game.")
           break
   
