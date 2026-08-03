def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    stack = [[i] for i in range(n)]
    while stack:
        board = stack.pop()
        if len(board) == n:
            # instead of append, insert puts the solutions in the order the test expects
            solutions.insert(0,board)
            continue

        node = len(board)

        for column in range(n):
            if column in board:
                continue

            diagonal = False
            for y2, x2 in enumerate(board):
                x1 = column
                y1 = node
                if abs(x1 - x2) == (y1 - y2):
                    diagonal = True
                    break

            if not diagonal:
                stack.append(board + [column])

    return solutions


if __name__ == '__main__':
    print(dfs_n_queens(4))
    # should return [[1, 3, 0, 2], [2, 0, 3, 1]].