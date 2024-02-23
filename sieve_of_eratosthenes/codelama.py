def run(n):
    # create a boolean array, where each element is True if the corresponding number is prime and False otherwise
    is_prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # mark all multiples of i as composite
            for j in range(i * i, n, i):
                is_prime[j] = False
    return [x for x in range(2, n) if is_prime[x]]

print (run(100))