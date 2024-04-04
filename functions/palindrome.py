# A palindrome is a word that reads the same backwards as forwards.

def is_palindrome(string):
    backwards = string[::-1]
    print(backwards)
    return backwards == string


answer = is_palindrome("Takudzwa")
print(answer)

