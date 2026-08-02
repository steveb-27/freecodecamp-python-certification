def hanoi_solver(disks):
    if disks == 0:
        return '[] [] []'
    stacks = [list(range(disks, 0, -1)), [], []]
    solution = f"{stacks[0]} {stacks[1]} {stacks[2]}\n"

    def move_tower(size, source, target, swap):
        nonlocal solution
        if size == 1:
            # Base case: Just move the single disk
            disk = stacks[source].pop()
            stacks[target].append(disk)
            # Log the current state after this single move
            solution += f"{stacks[0]} {stacks[1]} {stacks[2]}\n"
        else:
            # 1. Move the sub-tower of size-1 out of the way to the swap space
            move_tower(size - 1, source, swap, target)

            # 2. Move the largest disk of this sub-process to its final space
            move_tower(1, source, target, swap)

            # 3. Move the sub-tower from the swap space to the final space
            move_tower(size - 1, swap, target, source)

    # Start the divide-and-conquer process
    move_tower(disks, 0, 2, 1)
    return solution.rstrip('\n')


if __name__ == '__main__':
    print(hanoi_solver(6))