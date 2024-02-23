def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        # If primes[p] is not changed, then it is a prime
        if primes[p]:
            # Update all multiples of p
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    
    # Print all prime numbers
    prime_numbers = []
    for p in range(2, n+1):
        if primes[p]:
            prime_numbers.append(p)
    
    return prime_numbers

# Example usage:
n = 100
print("Prime numbers up to", n, "are:", sieve_of_eratosthenes(n))