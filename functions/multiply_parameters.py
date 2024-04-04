def multiply(a, b):
    result = a * b
    return result


answer = multiply(4, 2)
answer2 = multiply(10.5, 4)
print(answer)
print(answer2)

for value in range(1, 5):
    two_times = multiply(2, value)
    print(two_times)
