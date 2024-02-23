def sieve_of_eratosthenes(n):

    primes = [True] * (n + 1)  # Initialize a boolean list to mark prime candidates
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            # Update all multiples of 'p' as non-prime (composite)
            for multiple in range(p * p, n + 1, p):
                primes[multiple] = False

    # Collect all marked primes
    return [num for num, is_prime in enumerate(primes) if is_prime]

print(sieve_of_eratosthenes(100))