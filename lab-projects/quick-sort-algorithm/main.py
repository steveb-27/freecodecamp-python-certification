def quick_sort(array):
    if not array:
        return []
    pivot_index = len(array) - 1
    pivot = array[pivot_index]

    lt = [value for value in array if value < pivot]
    if len(lt) > 1:
        lt = quick_sort(lt)
    eq = [value for value in array if value == pivot]
    # eq is already sorted
    gt = [value for value in array if value > pivot]
    if len(gt) > 1:
        gt = quick_sort(gt)

    return lt + eq + gt

if __name__ == '__main__':
    print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
    # Should return [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]