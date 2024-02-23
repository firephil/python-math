# Not working correctly original from deepseek small model (700mb)

"""
The original code has a few issues:
1.The list comprehension is not necessary and is likely causing a syntax error. 

It seems like the author intended to append elements to the list that are not in the set, 
but this is already done in the previous loop.

2.The statement is missing in the inner loop, 
which causes the outer loop to skip checking multiples of a non-prime number.

3.The set should be initialized with to avoid checking even numbers greater than 2.

"""

def run(limit):  
    
    not_prime = set() 
    primes  = []

    for i in range(2, int(limit**0.5 + 1)): 
        if i in not_prime:
            for j in range( i*i ,limit+1, i): 
                not_prime.add(j)  
        [primes.append(x) for x in list(range(2, limit)) if x not in not_prime] 
    return primes

print(run(100))