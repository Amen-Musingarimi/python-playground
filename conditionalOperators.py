answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
  if guess < answer:
    print("Please guess higher.")
  else:
    print("Please guess lower.")


# if guess < answer:
#   print("Your guess is too low. Please guess higher.")
#   guess = int(input())
#   if guess == answer:
#     print("Well done, you guessed it right.")
#   else:
#     print("Sorry, you have not guessed correctly.")
# elif guess > answer:
#   print("Your guess is too high. Please guess lower.")
#   guess = int(input())
#   if guess == answer:
#     print("Well done, you guessed it right.")
#   else:
#     print("Sorry, you have not guessed correctly.")
# else:
#   print("You got it first time.")