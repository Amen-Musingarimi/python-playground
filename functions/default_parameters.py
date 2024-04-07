def calc_rectangle_area(length=15, width=10):
    area = length * width
    return area


print(calc_rectangle_area())  # We call the function without parameters. It will be executed with default values.
print(calc_rectangle_area(20, 10))  # We specify the parameter values, which overwrites the default values.
