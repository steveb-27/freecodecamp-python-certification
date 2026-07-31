def square_root_bisection(value, tolerance, limit):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if value == 0 or value == 1:
        return f"The square root of {value} is {value}"