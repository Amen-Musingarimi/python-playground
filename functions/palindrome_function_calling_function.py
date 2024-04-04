def is_palindrome(string):
    backwards = string[::-1]
    print(backwards)
    return backwards.lower() == string.lower()


def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)


sentence = input("Please enter a sentence to check: ")

if is_palindrome_sentence(sentence):
    print("'{}' is a palindrome.".format(sentence))
else:
    print("'{}' is not a palindrome.".format(sentence))