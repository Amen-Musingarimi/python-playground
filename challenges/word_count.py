def letter_counter(text: str) -> None:
    """
    Counts the number of times a character occurs in the given `text`.
    :param text: A string of words and characters.
    :return: the number of times each word appears in a given text.
    """
    counted_characters = []
    for character in text:
        char = character.casefold()
        if char not in counted_characters and char.isalnum():
            count = text.count(char.casefold())
            counted_characters.append(char.casefold())
            print(f"Character: {char} appears {count}")

    print(counted_characters)


letter_counter("Later in the course, you'll see how to use the collections Counter class.")
