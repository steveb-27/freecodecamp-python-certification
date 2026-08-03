def adjacency_list_to_matrix(adjacency_list):
    size = len(adjacency_list)
    matrix = [[False] * size for _ in range(size)]
    for start_pos in range(size):
        for end_pos in range(size):
            distance = 0
            test_array = [start_pos]
            for distance in range(size):
                if end_pos in test_array:
                    if not matrix[start_pos][end_pos] or distance < matrix[start_pos][end_pos]:
                        matrix[start_pos][end_pos] = distance
                    # We don't want distance, we only want to know if adjascent
                    if matrix[start_pos][end_pos] > 1:
                        matrix[start_pos][end_pos] = 0
                    break
                next_test = []
                for pos in test_array:
                    next_test += adjacency_list[pos]
                test_array = next_test
                distance += 1
            if matrix[start_pos][end_pos] == False:
                # If it's not connected, it's not adjacent
                matrix[start_pos][end_pos] = 0
    print('[')
    for index, row in enumerate(matrix):
        output = f'   {str(row)}'
        if index < len(matrix) -1:
            output += ','
        print(output)
    print(']')

    return matrix

if __name__ == '__main__':
    sample_list = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [2]
    }

    adjacency_list_to_matrix(sample_list)