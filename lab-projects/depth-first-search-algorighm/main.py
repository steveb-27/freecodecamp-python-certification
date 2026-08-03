def dfs(adjacency_matrix, node_label):
    nodes_visited = []
    stack = [node_label]
    while stack:
        node = stack.pop()
        if node not in nodes_visited:
            nodes_visited.append(node)
            neighbors = [
                neighbor
                for neighbor, check in enumerate(adjacency_matrix[node]) if check == 1
            ]
            for neighbor in neighbors:
                stack.append(neighbor)

    return nodes_visited


if __name__ == '__main__':
    print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
    # expected [1,2,3,0]