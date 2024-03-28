empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = "432985617"
# print(sorted(digits)) # sorted(digits) - returns a new list of sorted numbers as strings just like as the original
# print(list(digits)) # list(digits) - returns a list of items but without being reordered or sorted.

more_numbers = list(numbers)
print(more_numbers)

print(numbers is more_numbers) # Checks if the two variables(lists) are the same in terms of identity not contents. Returns True/False
print(numbers == more_numbers) # Checks if the two variables are the same in terms of contents not identity.

some_more_numbers = numbers.copy() # Create a copy of the numbers variable. Therefore creating a copy of the list
print(some_more_numbers)