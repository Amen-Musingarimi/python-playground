def calc_rectangle_area(length: float = 15, width: float = 10) -> float:
    area = length * width
    return area


print(calc_rectangle_area())  # We call the function without parameters. It will be executed with default values.
print(calc_rectangle_area(20, 10))  # We specify the parameter values, which overwrites the default values.
