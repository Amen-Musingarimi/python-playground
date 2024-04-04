# A palindrome is a word that reads the same backwards as forwards.

def is_palindrome(string):
    backwards = string[::-1].lower()
    print(backwards)
    return backwards == string


word = input("Please enter a word to check: ")

if is_palindrome(word.lower()):
    print("'{}' is a palindrome.".format(word.casefold()))
else:
    print("'{}' is not a palindrome.".format(word.casefold()))
