# Bottom-up tabulation
def fibonacci(n):
    if n < 0:
        return 'n must be a positive integer.'
    sequence = [0,1]
    for i in range(len(sequence),n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[n]

print(fibonacci(5))