# Numeric Data Types
# 1 int - whole numbers with no fractional part
# 2 float - real numbers with fractional part after the decimal point.
# 3 complex

a = 12
b = 3

print(a + b)  #15
print(a - b)  #9
print(a * b)  #36
print(a / b)  #4.0
print(a // b) #4 integer division, rounded down towards minus infinity
print(a % b)  #0 modulo: the remainder after integer division

print()

for i in range(1, a // b):  # a / b returns an an error because it returns a float number after division
  print(i)