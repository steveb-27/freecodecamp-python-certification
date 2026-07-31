def selection_sort(array):
    print(f"Starting with {array}")
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array
    else:
        for i in range(len(array)):
            testing = array[i:]
            if len(testing) == 0:
                continue
            low = min(array[i:])
            low_position = array[i:].index(low) + i
            if i == low_position:
                continue
            else:
                array[low_position] = array[i]
                array[i] = low
    return array


if __name__ == '__main__':
    print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
    # should return [3, 5, 12, 15, 16, 23, 72, 99, 567].

    print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
    # should return [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]