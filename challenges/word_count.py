def letter_counter(text: str) -> None:
    """
    Counts the number of times a character occurs in the given `text`.
    :param text: A string of words and characters.
    :return: the number of times each word appears in a given text.
    """
    counted_characters = []
    for character in text:
        if character not in counted_characters:
            count = text.count(character)
            counted_characters.append(character)
            print(f"Character: {character} appears {count}")

    print(counted_characters)


letter_counter("Amenae")
