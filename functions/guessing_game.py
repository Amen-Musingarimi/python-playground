import random


def get_integer(prompt) -> int:
    """
    Get an integer from Standard Input (stdin).
    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return:  The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        #     print("Invalid! This is not a number. Enter a valid number.")
        print("Invalid! This is not a number. Enter a valid number.")
        # Note that the else statement is not necessary since we only reach the print()
        # line when the prompt is not an integer


highest = 10
chances = 5
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0  # Initialize to any number that doesn't equal the answer.

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break

    if guess == answer:
        print("Well done, you guessed it right.")
    else:
        if guess < answer:
            print("Your guess is too low. Please guess higher.")
            # chances = chances - 1
            chances -= 1
            print("{} remaining chances.".format(chances))
            if chances < 1:
                print("Game Over! You lost the game.")
                break
        else:
            print("Your guess is too high. Please guess lower.")
            # chances = chances - 1
            chances -= 1
            print("{} remaining chances.".format(chances))
            if chances < 1:
                print("Game Over! You lost the game.")
                break
