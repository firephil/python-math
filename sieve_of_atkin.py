def sieve_of_atkin(limit):
    
    """Efficiently finds prime numbers up to a given limit using the Sieve of Atkin.

    Args:
        limit: The upper limit for finding primes.

    Returns:
        A list of prime numbers less than or equal to the limit.
    """

    if limit < 2:
        return []  

    primes = [2, 3]
    sieve = [False] * (limit + 1)

    x_limit = int(limit**0.5) + 1
    for x in range(1, x_limit):
        for y in range(1, x_limit):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] ^= True

    # Remove multiples of squares of primes
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False
        r += 2

    # Collect the primes
    for a in range(5, limit + 1):
        if sieve[a]:
            primes.append(a)

    return primes

# Example usage
limit = 100
primes = sieve_of_atkin(limit)
print(primes)