"""Finds prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit: The upper limit for finding primes.

    Returns:
        A list of prime numbers less than or equal to the limit.
"""

def sieve_of_eratosthenes(limit):

    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            # Mark multiples of 'p' as composite (not prime)
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False

    # Collect the primes
    return [num for num, is_prime in enumerate(primes) if is_prime]

# Example usage
limit = 100
primes = sieve_of_eratosthenes(limit)
print(primes) 