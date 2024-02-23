# fixed version of deepcodeseek small model

def run(limit):
    
    not_prime = {x for x in range(4, limit, 2)} 
    primes  = []

    for i in range(2, int(limit**0.5 + 1)): 
        if i in not_prime:
            continue
        for j in range( i*i ,limit+1, i): 
            not_prime.add(j)  
    primes = list(filter(lambda x: x not in not_prime, range(2, limit)))
    return primes

# LLAMA 2 70b
def sieve_of_eratosthenes(n):
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
    return [p for p in range(2, n + 1) if prime[p]]


# Mixstral 8x7B-32
def sieve_of_eratosthenes(n: int) -> list:
    """
    Generate all primes smaller than `n` using the Sieve of Eratosthenes algorithm.

    :param n: The upper bound for the primes to be generated.
    :return: A list of primes smaller than `n`.
    """
    if n < 2:
        return []

    # Initialize a boolean array to track the primality of each number up to `n`
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False

    # Iterate through each number up to the square root of `n`
    for ind, val in enumerate(is_prime[:int(n**0.5) + 1]):
        if val is True:
            # If the number is prime, mark all of its multiples as composite
            for multiple in range(ind*ind, n, ind):
                is_prime[multiple] = False

    # Return a list of the prime numbers
    return [x for x in range(2, n) if is_prime[x]]
