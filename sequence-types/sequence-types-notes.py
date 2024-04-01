# A sequence is an ordered collection of items.

# Note the word ordered is important

# When you iterate over a sequence - using a for loop, for example - you will always get the items in the same order.

# A sequence types can be iterated over, e.g strings, lists, etc.

# Indexing and Slicing works the same on both Strings and Lists because they are both sequence types. But the main difference between the 2 is strings are immutable(they cannot be changed) while lists are mutable(can be changed)

# List of immutable types in Python:
  #1 Int 
  #2 Float
  #3 bool (true/false): a subclass of int
  #4 str (string)
  #5 tuple
  #6 frozenset
  #7 bytes

# A mutable object is the one whose value can be changed. 
# Python has the following mutable objects
  #1 List
  #2 Dict
  #3 Set
  #4 Bytearray

# Operations that can be performed on mutable objects
  # len() returns the number of items in a list
  # append is used to add a new item to a list
  # enumerate returns each item, with its index position
  # the sort method sorts the items in a list either ascending or descending order using the reverse and 
  # Note that the sort method does not mutate the list
  # The sorted() function can be used to sort any iterables e.g strings and lists
  # The sorted function returns the list containing all letters in order
  # The difference between the sort and sorted functions is that the sort method alters the given iterable while the sorted function returns a new iterable
  # Note that we cannot pass the sort() method to a variable as it will return Note e.g sorted_numbers = numbers.sort() - this will return None
  # Please note that when using the sorted() function it will start with the white spaces and  then the capital letters. 
  # To solve the capital letters issue we use the key method e.g key=str.casefold then the capital letters will be sorted just like other letters
  # sorted() and list() boths returns a list however the returned list for sorted() will be sorted while for list() will not be sorted.

# TUPLES
  # A tuple is a mathematical name for an ordered set of data
  # Tuples are another sequence type along with strings, lists, and ranges
  # Tuples differ from lists because they are immutable. They can't be changed once they are created, just like strings
  # A tuple will be in paretheses and a list in square brackets. 