# A palindrome is a word that reads the same backwards as forwards.

def is_palindrome(string):
    backwards = string[::-1]
    print(backwards)
    return backwards == string


word = input("Please enter a word to check: ")

if is_palindrome(word):
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))