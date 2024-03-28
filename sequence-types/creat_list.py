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

print(list(digits)) # list(digits) - returns a list of items but without being reordered or sorted.