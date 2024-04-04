def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].lower() == string.lower()


sentence = input("Please enter a sentence to check: ")

if is_palindrome_sentence(sentence):
    print("'{}' is a palindrome.".format(sentence))
else:
    print("'{}' is not a palindrome.".format(sentence))