def square_root_bisection(value, tolerance=0.01, limit=100):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if value == 0 or value == 1:
        print(f"The square root of {value} is {value}")
        return value
    if value < 1:
        low = value
        high = 1
    else:
        low = 0
        high = value

    mid = (high + low) / 2
    last_value = low
    iteration = 1
    while mid ** 2 != value:
        if iteration > limit:
            print(f"Failed to converge within {limit} iterations")
            return None
        if abs(last_value - mid) <= tolerance:
            print(f"The square root of {value} is approximately {mid}")
            return mid
        if mid ** 2 > value:
            high = mid
            last_value = mid
            mid = (high + low) / 2
            iteration += 1
        else:
            low = mid
            last_value = mid
            mid = (high + low) / 2
            iteration += 1
    print(f"The square root of {value} is {mid}")
    return mid


square_root_bisection(.1, 1e-7, 50)